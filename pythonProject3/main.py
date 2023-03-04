# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout
#
#
# class Calculator(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Калькулятор гиперпанка")
#         self.setGeometry(300, 300, 300, 300)
#         self.setFixedSize(300, 300)
#
#         # Создаем виджет калькулятора
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#
#         # Создаем вертикальный лейаут
#         vbox = QVBoxLayout()
#
#         # Создаем поле ввода
#         self.input_field = QLineEdit()
#         self.input_field.setReadOnly(True)
#         vbox.addWidget(self.input_field)
#
#         # Создаем сетку кнопок
#         grid = QGridLayout()
#         vbox.addLayout(grid)
#
#         # Создаем кнопки для цифр и операций
#         buttons = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"]
#         positions = [(i, j) for i in range(4) for j in range(4)]
#         for position, button in zip(positions, buttons):
#             button_widget = QPushButton(button)
#             button_widget.setObjectName("button")
#             button_widget.clicked.connect(lambda state, x=button: self.input_field.setText(self.input_field.text() + x))
#             grid.addWidget(button_widget, *position)
#
#         # Добавляем лейаут на виджет
#         central_widget.setLayout(vbox)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     calc = Calculator()
#     calc.show()
#     sys.exit(app.exec_())

#
# x = 2**3-4
# print(x)
#
#
# print(("A" !="A") or not (2>=3))

class Dog:
    def walk(self):
        return "*walking"
    def speak(self):
        return "Woof!"
class JackRussellTerrier(Dog):
        def talk(self):
            return super().speak()

bobo = JackRussellTerrier()
print(bobo.talk())


colors = ['red' , 'green']
print('yellow' in colors)


# for num in range(1,5):
#     print(num)

x = 0
while x<10:
    x=x+1
print(x)


from add import adder