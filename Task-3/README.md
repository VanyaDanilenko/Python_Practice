<h1 align="center">Task-3</h1>

<h3 align="left">Viewing statistics on covid-19</h3>
<p align="left">Implement a window application that will provide statistics for 5+ countries, statistics can be taken any total_cases, and so on.</p>

<p align="left">An example of working on an operating system macos</p>
<kbd>
    <img src="../Images/Task-3_main.png" width="700px" alt="Task-3">
</kbd>

<br>
<br>

<p align="left">1. For a more comfortable work with the graphical interface, PyQt5 was chosen.</p>

<img width="300px" src="https://res.cloudinary.com/practicaldev/image/fetch/s--5x8ZbR8v--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/5b5e3vc30d0rqehp0wh5.jpg" alt="Task-3">

### Install PyQt5

```shell
$ pip3 install PyQt5
$ pip3 install pyqt5-tools
```

<br>
<br>

<p align="left">2. First of all, we create an interface in qt designer.</p>
<kbd>
    <img src="../Images/Task-3_2.png" width="700px" alt="Task-3">
</kbd>

<br>
<br>

<p align="left">3. Then create the user interface by adding all the necessary components.</p>

<kbd>
    <img width="auto" src="../Images/merge_from_ofoct.png" alt="Task-3">
</kbd>

<br>
<br>

<p align="left">4. When the interface is complete. You will need to translate it into (.py) code. To make it easier to build the project later.</p>

### Converting (.ui) in (.py)

```shell
$ pyuic5 C19.ui -o C19.py
```
<br>
<br>

<p align="left">5. An example of working with the program.</p>
<img width="700px" src="https://drive.google.com/uc?id=1hIPHfdRLOct5T4jchYM9ji_RCDEcJSf9" alt="Task-3">

<br>
<br>

<p align="left">Save file:</p>
<kbd>
    <img src="https://drive.google.com/uc?id=1aFyxoYieJHyyo1zVgTGWoQX_-m-S62OY" width="100px" title="Save file">
</kbd>

### Example

```python
from os import pread
from PyQt5 import QtWidgets, QtGui, uic, QtCore, QtSerialPort
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QTableView, QWidget, QLabel, QPushButton, QMessageBox, QDialog, QInputDialog, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QImage, QCursor, QPalette, QColor, QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt, QSize, QDir
from C19 import Ui_MainWindow
from decimal import *
import pyqtgraph as pg
import sys
import requests
import webbrowser
from pathlib import Path

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/europe"

headers = {
    'x-rapidapi-key': "01f8a8cfd9mshbca1824dd2b941dp1526f5jsn4e6523312a12",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        exceptions = ['id',
                      'one_Caseevery_X_ppl',
                      'one_Deathevery_X_ppl',
                      'one_Testevery_X_ppl',
                      'Deaths_1M_pop',
                      'Serious_Critical',
                      'Tests_1M_Pop',
                      'TotCases_1M_Pop',
                      ]

        def fillingTable():
            response = requests.request("GET", url, headers=headers)
            
            headerarr = []
            mainHarr = []

            self.ui.tableWidget.setColumnCount(100)
            self.ui.tableWidget.setRowCount(1000)

            for i in response.json()[0]:
                if i in exceptions:
                    continue
                else:
                    headerarr.append(i.capitalize())
                    mainHarr.append(i)

            self.ui.tableWidget.setHorizontalHeaderLabels(headerarr)

            for idx in range(len(response.json())):
                counter = 0
                for elin in response.json()[idx]:
                    if elin in exceptions:
                        continue
                    else:
                        self.ui.tableWidget.setItem(idx, counter, QtGui.QTableWidgetItem(str((response.json()[idx])[elin])))
                        counter+=1
                    
        def saveToFile():
            downloads_path = str(Path.home() / 'Downloads')

            f = open(downloads_path + '/C19-Get-all-European-countries(gjvue8e8y7r7r8).txt', 'a')
            f.write(str(response.json()))
            f.close()


        def goToSite():
            webbrowser.open('https://github.com/sergden2021/python-practice', new=2)

        def refreshButton_clicked():
            fillingTable()

        def searchButton_clicked():
            existCountry = False
            
            for i in range(1000):
                try:
                    country = self.ui.tableWidget.item(i, 1).text()
                    if country == self.ui.lineEdit.text():
                        self.ui.tableWidget.selectRow(i)
                        existCountry = True
                except:
                    break

            if existCountry == False:
                msg = QMessageBox()
                msg.setWindowTitle('Error!')
                msg.setText('Such a country has not been found!')
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec()
                
        self.ui.menubar.setStyleSheet('')

        self.ui.refreshButton.clicked.connect(refreshButton_clicked)
        self.ui.refreshButton.setShortcut('Ctrl+R')
        
        self.ui.searchButton.clicked.connect(searchButton_clicked)
        self.ui.searchButton.setShortcut('Shift+Ctrl+S')

        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(['Get all European countries'])

        def QuitEvent():
            msg = QMessageBox()
            msg.setWindowTitle('Save?')
            msg.setText("You haven't saved your document! Save it? ")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            msg.setDefaultButton(QMessageBox.Yes)
            retval = msg.exec()
            
            if retval == QMessageBox.Yes:
                saveToFile()
            if retval == QMessageBox.No:
                self.close()

        self.ui.actionSave_statistics.triggered.connect(saveToFile)
        self.ui.actionFor_more_informations.triggered.connect(goToSite)

        app.aboutToQuit.connect(QuitEvent)
        QtWidgets.QShortcut(QtGui.QKeySequence('Escape'), self, activated=QuitEvent)

        fillingTable()
        self.show()
        
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

window = Main()
app.exec_()
```
