from tkinter import *
import math

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()
def func_cos():
    global expression
    input_text.set(math.cos(int(expression)) if expression.isdecimal() else 'error')
    expression = ""
 
def func_sin():
    global expression
    input_text.set(math.sin(int(expression)) if expression.isdecimal() else 'error')
    expression = ""
 
def func_tan():
    global expression
    input_text.set(math.tan(int(expression)) if expression.isdecimal() else 'error')
    expression = ""
 
def func_ctan():
    global expression
    input_text.set(math.ctg(int(expression)) if expression.isdecimal() else 'error')
    expression = ""
 
def func_log():
    global expression
    input_text.set(math.log(int(expression)) if expression.isdecimal() else 'error')
    expression = ""
 
def func_ln():
    global expression
    input_text.set(math.ln(int(expression)) if expression.isdecimal() else 'error')
    expression = ""
 
def func_pt():
    global expression
    input_text.set(float(expression)/100 if expression.isdecimal() else 'error')
    expression = ""
 
def to_bin():
    global expression
    input_text.set(bin(int(expression))[2:].zfill(8) if expression.isdecimal() else 'error')
    expression = ""
    
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
