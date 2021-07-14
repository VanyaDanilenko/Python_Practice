from os import pread
from googletrans import Translator
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
