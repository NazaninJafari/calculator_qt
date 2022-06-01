from cmath import sqrt
from unittest import loader
import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Calcurator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.ui.sumbutton.clicked.connect(self.sum)
        self.ui.subbutton.clicked.connect(self.sub)
        self.ui.divbutton.clicked.connect(self.div)
        self.ui.mulbutton.clicked.connect(self.mul)
        self.ui.equal_button.clicked.connect(self.equal)
        self.ui.clear_button.clicked.connect(self.clear)
        self.ui.float_button.clicked.connect(self.dot)
        self.ui.pn_button.clicked.connect(self.pn_func)
        self.ui.sin_button.clicked.connect(self.sin_func)
        self.ui.cos_button.clicked.connect(self.cos_func)
        self.ui.tan_button.clicked.connect(self.tan_func)
        self.ui.cot_button.clicked.connect(self.cot_func)
        self.ui.sqrt_button.clicked.connect(self.sqrt_func)
        self.ui.fact_button.clicked.connect(self.factorial_func)
        self.ui.log_button.clicked.connect(self.log_func)
        
        self.ui.button0.clicked.connect(self.func_number0)
        self.ui.button1.clicked.connect(self.func_number1)
        self.ui.button2.clicked.connect(self.func_number2)
        self.ui.button3.clicked.connect(self.func_number3)
        self.ui.button4.clicked.connect(self.func_number4)
        self.ui.button5.clicked.connect(self.func_number5)
        self.ui.button6.clicked.connect(self.func_number6)
        self.ui.button7.clicked.connect(self.func_number7)
        self.ui.button8.clicked.connect(self.func_number8)
        self.ui.button9.clicked.connect(self.func_number9)
    
    def sum(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.neshan = '+'
    
    def sub(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.neshan = '-'
    
    def div(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.neshan = '/'
    
    def mul(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.neshan = '*'
    
    def equal(self):
        self.num2 = float(self.ui.textbox.text())
        if self.neshan == '+':
            result = self.num1 + self.num2
        elif self.neshan == '-':
            result = self.num1 - self.num2
        elif self.neshan == '/':
            if self.num2 == 0:
                self.ui.textbox.setText('Cannot divide by zero')
            else:
                result = self.num1 / self.num2
        elif self.neshan == '*':
            result = self.num1 * self.num2
        
        elif self.neshan == 'sin':
            result = math.sin(math.radians(self.num2))
        
        elif self.neshan == 'cos':
            result = math.cos(math.radians(self.num2))

        elif self.neshan == 'tan':
            result = math.tan(math.radians(self.num2))
        
        elif self.neshan == 'cot':
            num1 = math.sin(math.radians(self.num2))
            num2 = math.cos(math.radians(self.num2))
            result = num2 / num1
        
        self.ui.textbox.setText(str(result))
    
    def dot(self):
        for i in self.ui.textbox.text():
            if '.' not in self.ui.textbox.text():
                self.ui.textbox.setText(self.ui.textbox.text() + '.')
    #positif/negatif
    def pn_func(self):
        self.ui.textbox.setText(str(-1 * float(self.ui.textbox.text())))
 
    def sin_func(self):
        self.neshan = 'sin'

    def cos_func(self):
        self.neshan = 'cos'  

    def tan_func(self):
        self.neshan = 'tan'

    def cot_func(self):
        self.neshan = 'cot'

    def sqrt_func(self):
        self.num = float(self.ui.textbox.text())
        result = math.sqrt(self.num)
        self.ui.textbox.setText(str(result))
    
    def factorial_func(self):
        self.num = float(self.ui.textbox.text())
        result = math.factorial(self.num)
        self.ui.textbox.setText(str(result))
    
    def log_func(self):
        self.num = float(self.ui.textbox.text())
        if self.num == 0:
            self.ui.textbox.setText('Invalid input')
        else: 
            self.ui.textbox.setText(str(math.log(self.num, 10))) 
    
    def clear(self):
        self.ui.textbox.setText('')

    def func_number0(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '0')
    
    def func_number1(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '1')

    def func_number2(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '2')  

    def func_number3(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '3')

    def func_number4(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '4') 

    def func_number5(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '5')

    def func_number6(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '6')

    def func_number7(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '7')

    def func_number8(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '8')

    def func_number9(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '9')
                     

app = QApplication()
window = Calcurator()
app.exec()