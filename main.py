from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QButtonGroup)
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import time
import question
import pyautogui


class Ui_Form(object):
    def __init__(self, Form):
        self.setupUi(Form)

    def setupUi(self, Form):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]

        # width_ = 1920
        # height_ = 1080

        # width_ = 1680
        # height_ = 1050

        print(width_)
        print(height_)

        Form.setObjectName("Form")
        Form.resize(int(width_ * 0.2), int(height_ * 0.25))
        Form.setFixedSize(int(width_ * 0.2), int(height_ * 0.25))
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(
            QtCore.QRect(int(width_ * 0.026), int(height_ * 0.05), int(width_ * 0.05), int(height_ * 0.02)))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(
            QtCore.QRect(int(width_ * 0.078), int(height_ * 0.05), int(width_ * 0.05), int(height_ * 0.02)))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(
            QtCore.QRect(int(width_ * 0.13), int(height_ * 0.05), int(width_ * 0.05), int(height_ * 0.02)))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(
            QtCore.QRect(int(width_ * 0.072), int(height_ * 0.018), int(width_ * 0.1), int(height_ * 0.037)))
        self.label.setObjectName("label")

        self.name_ = QtWidgets.QLineEdit(Form)
        self.name_.setGeometry(
            QtCore.QRect(int(width_ * 0.026), int(height_ * 0.09), int(width_ * 0.156), int(height_ * 0.027)))
        self.name_.setObjectName("name")
        self.name2_ = QtWidgets.QLineEdit(Form)
        self.name2_.setGeometry(
            QtCore.QRect(int(width_ * 0.026), int(height_ * 0.13), int(width_ * 0.156), int(height_ * 0.027)))
        self.name2_.setObjectName("name2")

        self.invis = QtWidgets.QLabel(Form)
        self.invis.setGeometry(
            QtCore.QRect(int(width_ * 0.026), int(height_ * 0.15), int(width_ * 0.156), int(height_ * 0.027)))
        self.invis.setObjectName("incorrect")

        self.invis.setStyleSheet(
            'color:red;\n'
            'text-align:center;\n'
        )

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(
            QtCore.QRect(int(width_ * 0.07), int(height_ * 0.17), int(width_ * 0.046), int(height_ * 0.027)))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)
        self.name_.setPlaceholderText("Name")
        self.radioButton.setText("English")
        self.radioButton_2.setText("Russian")
        self.radioButton_3.setText("Armenian")
        self.label.setText("Select Language")
        self.name2_.setPlaceholderText("Password")
        self.pushButton.setText("Sign in")
        self.name2_.setEchoMode(QLineEdit.Password)

        self.radioButton.setStyleSheet(
            f"font:{width_ // 130}px \"MS Shell Dlg 2\";\n"
        )

        self.radioButton_2.setStyleSheet(
            f"font:{width_ // 130}px \"MS Shell Dlg 2\";\n"

        )
        self.radioButton_3.setStyleSheet(
            f"font:{width_ // 130}px \"MS Shell Dlg 2\";\n"

        )
        self.label.setStyleSheet(
            f"font:{width_ // 130}px \"MS Shell Dlg 2\";\n"
        )

    def start(self):

        if len(self.name_.text()) >= 3 and len(self.name_.text()) <= 8:
            self.lang = 0
            if self.radioButton.isChecked():
                self.lang = 0
            elif self.radioButton_2.isChecked():
                self.lang = 1
            elif self.radioButton_3.isChecked():
                self.lang = 2

        else:
            self.invis.setText('name length must be more than 3 and less than 8')
            self.name_.clear()
            self.name2_.clear()
            return

        if self.lang == 0:
            self.texter = ['Math', 'Physics', 'History', 'Language', 'Start', 'Exit', 'Time', 'Next', 'Finish',
                           'Result', 0]
        elif self.lang == 1:
            self.texter = ["Матем", "Физика", "История", "Языки", 'Начало', 'Выход', 'Время', 'Следующий',
                           'Заканчивать', 'Результат', 1]
        elif self.lang == 2:
            self.texter = ['Մաթեմ', 'Ֆիզիկա', 'Պատմություն', 'Լեզուներ', 'Սկիզբ', 'ելք', 'Ժամանակ', 'Հաջորդը',
                           'Ավարտել', 'Արդյունք', 2]
        self.start_ = Example(self.texter, self.name_)
        self.start_.show()
        Form.close()


class Example(QWidget):
    def __init__(self, barer, name_):
        super().__init__()
        self.initUI(barer, name_)

    def initUI(self, barer, name_):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]

        self.setGeometry(-1, -1, width_, height_)
        self.setFixedSize(width_, height_)

        self.setWindowTitle('Test')
        self.pixmap = QPixmap('image/b.png')
        self.image1 = QLabel(self)
        self.image1.move(0, 0)
        self.image1.resize(width_, height_)
        self.image1.setPixmap(self.pixmap)

        self.pixmap2 = QPixmap('image/lock.png')
        self.image2 = QLabel(self)
        self.image2.move(int(width_ * 0.64), int(height_ * 0.34))
        self.image2.resize(int(width_ * 0.026), int(height_ * 0.046))

        self.pixmap3 = QPixmap('image/lock.png')
        self.image3 = QLabel(self)
        self.image3.move(int(width_ * 0.64), int(height_ * 0.48))
        self.image3.resize(int(width_ * 0.026), int(height_ * 0.046))

        self.pixmap4 = QPixmap('image/lock.png')
        self.image4 = QLabel(self)
        self.image4.move(int(width_ * 0.64), int(height_ * 0.62))
        self.image4.resize(int(width_ * 0.026), int(height_ * 0.046))

        self.btn = QPushButton(barer[4], self)

        self.btn.move(int(width_ * 0.57), int(height_ * 0.37))
        self.btn.resize(int(width_ * 0.1), int(height_ * 0.09))

        self.btn.setStyleSheet("background-color: rgb(157, 157, 157);\n"
                               "color: rgb(255, 255, 255);\n"
                               f"font: {width_ // 80}px \"MS Shell Dlg 2\";\n"
                               'border-radius: 20px;\n')

        self.btn.clicked.connect(lambda: self.start123(barer, name_))

    def start123(self, barer, name_):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]

        self.image2.setPixmap(self.pixmap2)
        self.image3.setPixmap(self.pixmap3)
        self.image4.setPixmap(self.pixmap4)

        self.btn1 = QPushButton(barer[0], self)
        self.btn1.resize(int(width_ * 0.1), int(height_ * 0.09))
        self.btn1.move(int(width_ * 0.57), int(height_ * 0.32))

        self.btn2 = QPushButton(barer[1], self)
        self.btn2.resize(int(width_ * 0.1), int(height_ * 0.09))
        self.btn2.move(int(width_ * 0.57), int(height_ * 0.46))

        self.btn3 = QPushButton(barer[2], self)
        self.btn3.resize(int(width_ * 0.1), int(height_ * 0.09))
        self.btn3.move(int(width_ * 0.57), int(height_ * 0.18))

        self.btn0 = QPushButton(barer[3], self)
        self.btn0.resize(int(width_ * 0.1), int(height_ * 0.09))
        self.btn0.move(int(width_ * 0.57), int(height_ * 0.6))

        self.btn.hide()
        self.btn0.show()
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn0.setStyleSheet("background-color: rgba(157, 157, 157,0.7);\n"
                                "color: rgb(255, 255, 255);\n"
                                f"font: {width_ // 85}px \"MS Shell Dlg 2\";\n"
                                'border-radius: 20px;\n')
        self.btn1.setStyleSheet("background-color: rgba(157, 157, 157,0.7);\n"
                                "color: rgb(255, 255, 255);\n"
                                f"font: {width_ // 85}px \"MS Shell Dlg 2\";\n"
                                'border-radius: 20px;\n')
        self.btn2.setStyleSheet("background-color: rgba(157, 157, 157,0.7);\n"
                                "color: rgb(255, 255, 255);\n"
                                f"font: {width_ // 85}px \"MS Shell Dlg 2\";\n"
                                'border-radius: 20px;\n')
        self.btn3.setStyleSheet("background-color: rgba(157, 157, 157,1);\n"
                                "color: rgb(255, 255, 255);\n"
                                f"font: {width_ // 85}px \"MS Shell Dlg 2\";\n"
                                'border-radius: 20px;\n')
        self.btn3.clicked.connect(lambda: self.open_form(barer, name_))

    def keyPressEvent(self, event):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]
        if event.key() == 16777216:
            self.setGeometry(int(width_ * 0.3), int(height_ * 0.37), int(width_ * 0.3), int(height_ * 0.37))
            self.setFixedSize(int(width_ * 0.3), int(height_ * 0.37))
            time.sleep(.5)
            sys.exit(app.exec())

    def open_form(self, barer, name_):
        ui = SecondForm(barer, name_)
        ui.show()
        self.hide()


class SecondForm(QWidget):
    def __init__(self, barer, name_):
        super().__init__()
        self.initUI(barer, name_)

    def initUI(self, barer, name_):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]
        self.setGeometry(-1, -1, width_, height_)
        self.setFixedSize(width_, height_)
        self.setStyleSheet("background-color: white;\n")
        self.setWindowTitle(barer[2])
        self.vernagir = QLabel(self)
        self.vernagir.setText(barer[2])
        self.vernagir.move(int(width_ * 0.025), int(height_ * 0.14))
        if barer[-1] != 2:
            self.vernagir.move(int(width_ * 0.07), int(height_ * 0.14))
        self.font = QtGui.QFont()
        self.font.setItalic(True)
        self.font.setWeight(75)
        self.vernagir.setFont(self.font)
        self.vernagir.setStyleSheet('color: gray;\n'
                                    f'font-size: {width_ // 40}px \n')

        self.pixmap = QPixmap('image/tigran.jpg')
        self.image = QLabel(self)
        self.image.move(int(width_ * 0.026), int(height_ * 0.28))
        self.image.resize(int(width_ * 0.31), int(height_ * 0.556))
        self.image.setPixmap(self.pixmap)

        self.btn10 = QPushButton(barer[5], self)
        self.btn10.resize(int(width_ * 0.07), int(height_ * 0.07))
        self.btn10.move(int(width_ * 0.89), int(height_ * 0.04))

        self.btn10.setStyleSheet("background-color: rgb(255, 120, 120);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 f"font: {width_ // 80}px \"MS Shell Dlg 2\";\n"
                                 'border-radius: 20px;\n')
        self.btn10.show()
        self.btn10.clicked.connect(self.endd)

        fnt = QFont('Open Sans', width_ // 100, QFont.Bold)

        self.lbl = QLabel(self)
        self.lbl.setFont(fnt)
        self.lbl.move(int(width_ * 0.9), int(height_ * 0.14))
        self.lbl.resize(int(width_ * 0.15), int(height_ * 0.037))

        self.harcer(barer, name_)
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.showTime(barer))
        timer.start(1000)

        self.currentTime = QTime(0, 15, 0, 0)
        self.displayTxt = self.currentTime.toString('hh:mm:ss')
        self.all = int(self.displayTxt[:2]) * 3600 + int(self.displayTxt[3:5]) * 60 + int(self.displayTxt[6:])
        self.showTime(barer)

    def endd(self):
        sys.exit(app.exec_())

    def harcer(self, barer, name_):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()
        hbox8 = QHBoxLayout()

        bg1 = QButtonGroup(self)
        bg2 = QButtonGroup(self)
        bg3 = QButtonGroup(self)
        bg4 = QButtonGroup(self)
        bg5 = QButtonGroup(self)
        bg6 = QButtonGroup(self)
        bg7 = QButtonGroup(self)
        bg8 = QButtonGroup(self)

        self.label1 = QLabel(self)
        self.label1.move(int(width_ * 0.34), int(height_ * 0.03))
        self.label1.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label1.setObjectName("label1")

        self.rb1 = QtWidgets.QRadioButton(self)
        self.rb1.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb1.move(int(width_ * 0.38), int(height_ * 0.12))
        self.rb1.setObjectName("rb1")

        self.rb2 = QtWidgets.QRadioButton(self)
        self.rb2.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb2.move(int(width_ * 0.49), int(height_ * 0.12))
        self.rb2.setObjectName("rb2")

        self.rb3 = QtWidgets.QRadioButton(self)
        self.rb3.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb3.move(int(width_ * 0.38), int(height_ * 0.17))
        self.rb3.setObjectName("rb3")

        self.rb4 = QtWidgets.QRadioButton(self)
        self.rb4.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb4.move(int(width_ * 0.49), int(height_ * 0.17))
        self.rb4.setObjectName("rb4")

        self.label2 = QLabel(self)
        self.label2.move(int(width_ * 0.34), int(height_ * 0.23))
        self.label2.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label2.setFont(font)
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label2.setObjectName("label2")

        self.rb21 = QtWidgets.QRadioButton(self)
        self.rb21.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb21.move(int(width_ * 0.38), int(height_ * 0.32))
        self.rb21.setObjectName("rb21")

        self.rb22 = QtWidgets.QRadioButton(self)
        self.rb22.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb22.move(int(width_ * 0.49), int(height_ * 0.32))
        self.rb22.setObjectName("rb22")

        self.rb23 = QtWidgets.QRadioButton(self)
        self.rb23.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb23.move(int(width_ * 0.38), int(height_ * 0.37))
        self.rb23.setObjectName("rb23")

        self.rb24 = QtWidgets.QRadioButton(self)
        self.rb24.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb24.move(int(width_ * 0.49), int(height_ * 0.37))
        self.rb24.setObjectName("rb24")

        self.label3 = QLabel(self)
        self.label3.move(int(width_ * 0.34), int(height_ * 0.43))
        self.label3.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label3.setFont(font)
        self.label3.setTextFormat(QtCore.Qt.AutoText)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label3.setObjectName("label3")

        self.rb31 = QtWidgets.QRadioButton(self)
        self.rb31.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb31.move(int(width_ * 0.38), int(height_ * 0.52))
        self.rb31.setObjectName("rb31")

        self.rb32 = QtWidgets.QRadioButton(self)
        self.rb32.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb32.move(int(width_ * 0.49), int(height_ * 0.52))
        self.rb32.setObjectName("rb32")

        self.rb33 = QtWidgets.QRadioButton(self)
        self.rb33.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb33.move(int(width_ * 0.38), int(height_ * 0.57))
        self.rb33.setObjectName("rb33")

        self.rb34 = QtWidgets.QRadioButton(self)
        self.rb34.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb34.move(int(width_ * 0.49), int(height_ * 0.57))
        self.rb34.setObjectName("rb34")

        self.label4 = QLabel(self)
        self.label4.move(int(width_ * 0.34), int(height_ * 0.63))
        self.label4.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label4.setFont(font)
        self.label4.setTextFormat(QtCore.Qt.AutoText)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label4.setObjectName("label4")

        self.rb41 = QtWidgets.QRadioButton(self)
        self.rb41.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb41.move(int(width_ * 0.38), int(height_ * 0.72))
        self.rb41.setObjectName("rb41")

        self.rb42 = QtWidgets.QRadioButton(self)
        self.rb42.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb42.move(int(width_ * 0.49), int(height_ * 0.72))
        self.rb42.setObjectName("rb42")

        self.rb43 = QtWidgets.QRadioButton(self)
        self.rb43.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb43.move(int(width_ * 0.38), int(height_ * 0.77))
        self.rb43.setObjectName("rb43")

        self.rb44 = QtWidgets.QRadioButton(self)
        self.rb44.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb44.move(int(width_ * 0.49), int(height_ * 0.77))
        self.rb44.setObjectName("rb44")

        self.label5 = QLabel(self)
        self.label5.move(int(width_ * 0.63), int(height_ * 0.03))
        self.label5.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label5.setFont(font)
        self.label5.setTextFormat(QtCore.Qt.AutoText)
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label5.setObjectName("label5")

        self.rb51 = QtWidgets.QRadioButton(self)
        self.rb51.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb51.move(int(width_ * 0.67), int(height_ * 0.12))
        self.rb51.setObjectName("rb51")

        self.rb52 = QtWidgets.QRadioButton(self)
        self.rb52.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb52.move(int(width_ * 0.78), int(height_ * 0.12))
        self.rb52.setObjectName("rb52")

        self.rb53 = QtWidgets.QRadioButton(self)
        self.rb53.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb53.move(int(width_ * 0.67), int(height_ * 0.17))
        self.rb53.setObjectName("rb53")

        self.rb54 = QtWidgets.QRadioButton(self)
        self.rb54.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb54.move(int(width_ * 0.78), int(height_ * 0.17))
        self.rb54.setObjectName("rb54")

        self.label6 = QLabel(self)
        self.label6.move(int(width_ * 0.63), int(height_ * 0.23))
        self.label6.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label6.setFont(font)
        self.label6.setTextFormat(QtCore.Qt.AutoText)
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label6.setObjectName("label6")

        self.rb61 = QtWidgets.QRadioButton(self)
        self.rb61.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb61.move(int(width_ * 0.67), int(height_ * 0.32))
        self.rb61.setObjectName("rb61")

        self.rb62 = QtWidgets.QRadioButton(self)
        self.rb62.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb62.move(int(width_ * 0.78), int(height_ * 0.32))
        self.rb62.setObjectName("rb62")

        self.rb63 = QtWidgets.QRadioButton(self)
        self.rb63.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb63.move(int(width_ * 0.67), int(height_ * 0.37))
        self.rb63.setObjectName("rb63")

        self.rb64 = QtWidgets.QRadioButton(self)
        self.rb64.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb64.move(int(width_ * 0.78), int(height_ * 0.37))
        self.rb64.setObjectName("rb64")

        self.label7 = QLabel(self)
        self.label7.move(int(width_ * 0.63), int(height_ * 0.43))
        self.label7.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label7.setFont(font)
        self.label7.setTextFormat(QtCore.Qt.AutoText)
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label7.setObjectName("label7")

        self.rb71 = QtWidgets.QRadioButton(self)
        self.rb71.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb71.move(int(width_ * 0.67), int(height_ * 0.52))
        self.rb71.setObjectName("rb71")

        self.rb72 = QtWidgets.QRadioButton(self)
        self.rb72.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb72.move(int(width_ * 0.78), int(height_ * 0.52))
        self.rb72.setObjectName("rb72")

        self.rb73 = QtWidgets.QRadioButton(self)
        self.rb73.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb73.move(int(width_ * 0.67), int(height_ * 0.57))
        self.rb73.setObjectName("rb73")

        self.rb74 = QtWidgets.QRadioButton(self)
        self.rb74.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb74.move(int(width_ * 0.78), int(height_ * 0.57))
        self.rb74.setObjectName("rb74")

        self.label8 = QLabel(self)
        self.label8.move(int(width_ * 0.63), int(height_ * 0.63))
        self.label8.resize(int(width_ * 0.22), int(height_ * 0.074))
        font = QtGui.QFont()
        font.setPointSize(width_ // 150)
        self.label8.setFont(font)
        self.label8.setTextFormat(QtCore.Qt.AutoText)
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label8.setObjectName("label8")

        self.rb81 = QtWidgets.QRadioButton(self)
        self.rb81.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb81.move(int(width_ * 0.67), int(height_ * 0.72))
        self.rb81.setObjectName("rb81")

        self.rb82 = QtWidgets.QRadioButton(self)
        self.rb82.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb82.move(int(width_ * 0.78), int(height_ * 0.72))
        self.rb82.setObjectName("rb82")

        self.rb83 = QtWidgets.QRadioButton(self)
        self.rb83.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb83.move(int(width_ * 0.67), int(height_ * 0.77))
        self.rb83.setObjectName("rb83")

        self.rb84 = QtWidgets.QRadioButton(self)
        self.rb84.resize(int(width_ * 0.07), int(height_ * 0.0185))
        self.rb84.move(int(width_ * 0.78), int(height_ * 0.77))
        self.rb84.setObjectName("rb84")

        self.label1.setText(question.hh(barer))
        self.rb1.setText(question.h1(barer))
        self.rb2.setText(question.h2(barer))
        self.rb3.setText(question.h3(barer))
        self.rb4.setText(question.h4(barer))

        self.label2.setText(question.hh(barer))
        self.rb21.setText(question.h1(barer))
        self.rb22.setText(question.h2(barer))
        self.rb23.setText(question.h3(barer))
        self.rb24.setText(question.h4(barer))

        self.label3.setText(question.hh(barer))
        self.rb31.setText(question.h1(barer))
        self.rb32.setText(question.h2(barer))
        self.rb33.setText(question.h3(barer))
        self.rb34.setText(question.h4(barer))

        self.label4.setText(question.hh(barer))
        self.rb41.setText(question.h1(barer))
        self.rb42.setText(question.h2(barer))
        self.rb43.setText(question.h3(barer))
        self.rb44.setText(question.h4(barer))

        self.label5.setText(question.hh(barer))
        self.rb51.setText(question.h1(barer))
        self.rb52.setText(question.h2(barer))
        self.rb53.setText(question.h3(barer))
        self.rb54.setText(question.h4(barer))

        self.label6.setText(question.hh(barer))
        self.rb61.setText(question.h1(barer))
        self.rb62.setText(question.h2(barer))
        self.rb63.setText(question.h3(barer))
        self.rb64.setText(question.h4(barer))

        self.label7.setText(question.hh(barer))
        self.rb71.setText(question.h1(barer))
        self.rb72.setText(question.h2(barer))
        self.rb73.setText(question.h3(barer))
        self.rb74.setText(question.h4(barer))

        self.label8.setText(question.hh(barer))
        self.rb81.setText(question.h1(barer))
        self.rb82.setText(question.h2(barer))
        self.rb83.setText(question.h3(barer))
        self.rb84.setText(question.h4(barer))

        self.line = QtWidgets.QFrame(self)
        self.line.move(int(width_ * 0.6), int(height_ * 0.074))
        self.line.resize(1, int(height_ * 0.74))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.setStyleSheet('border: 5px solid black;\n')

        self.myButton = QPushButton(barer[7], self)
        self.myButton.move(int(width_ * 0.56), int(height_ * 0.85))
        self.myButton.resize(int(width_ * 0.08), int(height_ * 0.05))

        self.myButton.setStyleSheet(
            'background-color:grey;\n'
            'color:white;\n'
            f'font-size:{width_ // 120}px;\n'
        )

        self.tiv = 1
        self.score = 0
        self.myButton.clicked.connect(lambda: self.Npage(self.tiv, barer, name_))

        bg1.addButton(self.rb1)
        bg1.addButton(self.rb2)
        bg1.addButton(self.rb3)
        bg1.addButton(self.rb4)
        bg2.addButton(self.rb21)
        bg2.addButton(self.rb22)
        bg2.addButton(self.rb23)
        bg2.addButton(self.rb24)
        bg3.addButton(self.rb31)
        bg3.addButton(self.rb32)
        bg3.addButton(self.rb33)
        bg3.addButton(self.rb34)
        bg4.addButton(self.rb41)
        bg4.addButton(self.rb42)
        bg4.addButton(self.rb43)
        bg4.addButton(self.rb44)
        bg5.addButton(self.rb51)
        bg5.addButton(self.rb52)
        bg5.addButton(self.rb53)
        bg5.addButton(self.rb54)
        bg6.addButton(self.rb61)
        bg6.addButton(self.rb62)
        bg6.addButton(self.rb63)
        bg6.addButton(self.rb64)
        bg7.addButton(self.rb71)
        bg7.addButton(self.rb72)
        bg7.addButton(self.rb73)
        bg7.addButton(self.rb74)
        bg8.addButton(self.rb81)
        bg8.addButton(self.rb82)
        bg8.addButton(self.rb83)
        bg8.addButton(self.rb84)

        hbox1.addWidget(self.rb1)
        hbox1.addWidget(self.rb2)
        hbox1.addWidget(self.rb3)
        hbox1.addWidget(self.rb4)
        hbox2.addWidget(self.rb21)
        hbox2.addWidget(self.rb22)
        hbox2.addWidget(self.rb23)
        hbox2.addWidget(self.rb24)
        hbox3.addWidget(self.rb31)
        hbox3.addWidget(self.rb32)
        hbox3.addWidget(self.rb33)
        hbox3.addWidget(self.rb34)
        hbox4.addWidget(self.rb41)
        hbox4.addWidget(self.rb42)
        hbox4.addWidget(self.rb43)
        hbox4.addWidget(self.rb44)
        hbox5.addWidget(self.rb51)
        hbox5.addWidget(self.rb52)
        hbox5.addWidget(self.rb53)
        hbox5.addWidget(self.rb54)
        hbox6.addWidget(self.rb61)
        hbox6.addWidget(self.rb62)
        hbox6.addWidget(self.rb63)
        hbox6.addWidget(self.rb64)
        hbox7.addWidget(self.rb71)
        hbox7.addWidget(self.rb72)
        hbox7.addWidget(self.rb73)
        hbox7.addWidget(self.rb74)
        hbox8.addWidget(self.rb81)
        hbox8.addWidget(self.rb82)
        hbox8.addWidget(self.rb83)
        hbox8.addWidget(self.rb84)

        self.show()

    def Npage(self, tiv, barer, name_):
        def double_(self):

            if self.rb1.text()[-1] == ' ' and self.rb1.isChecked():
                self.score += 1
            if self.rb21.text()[-1] == ' ' and self.rb21.isChecked():
                self.score += 1
            if self.rb31.text()[-1] == ' ' and self.rb31.isChecked():
                self.score += 1
            if self.rb41.text()[-1] == ' ' and self.rb41.isChecked():
                self.score += 1
            if self.rb51.text()[-1] == ' ' and self.rb51.isChecked():
                self.score += 1
            if self.rb61.text()[-1] == ' ' and self.rb61.isChecked():
                self.score += 1
            if self.rb71.text()[-1] == ' ' and self.rb71.isChecked():
                self.score += 1
            if self.rb81.text()[-1] == ' ' and self.rb81.isChecked():
                self.score += 1

            if self.rb2.text()[-1] == ' ' and self.rb2.isChecked():
                self.score += 1
            if self.rb22.text()[-1] == ' ' and self.rb22.isChecked():
                self.score += 1
            if self.rb32.text()[-1] == ' ' and self.rb32.isChecked():
                self.score += 1
            if self.rb42.text()[-1] == ' ' and self.rb42.isChecked():
                self.score += 1
            if self.rb52.text()[-1] == ' ' and self.rb52.isChecked():
                self.score += 1
            if self.rb62.text()[-1] == ' ' and self.rb62.isChecked():
                self.score += 1
            if self.rb72.text()[-1] == ' ' and self.rb72.isChecked():
                self.score += 1
            if self.rb82.text()[-1] == ' ' and self.rb82.isChecked():
                self.score += 1

            if self.rb3.text()[-1] == ' ' and self.rb3.isChecked():
                self.score += 1
            if self.rb23.text()[-1] == ' ' and self.rb23.isChecked():
                self.score += 1
            if self.rb33.text()[-1] == ' ' and self.rb33.isChecked():
                self.score += 1
            if self.rb43.text()[-1] == ' ' and self.rb43.isChecked():
                self.score += 1
            if self.rb53.text()[-1] == ' ' and self.rb53.isChecked():
                self.score += 1
            if self.rb63.text()[-1] == ' ' and self.rb63.isChecked():
                self.score += 1
            if self.rb73.text()[-1] == ' ' and self.rb73.isChecked():
                self.score += 1
            if self.rb83.text()[-1] == ' ' and self.rb83.isChecked():
                self.score += 1

            if self.rb4.text()[-1] == ' ' and self.rb4.isChecked():
                self.score += 1
            if self.rb24.text()[-1] == ' ' and self.rb24.isChecked():
                self.score += 1
            if self.rb34.text()[-1] == ' ' and self.rb34.isChecked():
                self.score += 1
            if self.rb44.text()[-1] == ' ' and self.rb44.isChecked():
                self.score += 1
            if self.rb54.text()[-1] == ' ' and self.rb54.isChecked():
                self.score += 1
            if self.rb64.text()[-1] == ' ' and self.rb64.isChecked():
                self.score += 1
            if self.rb74.text()[-1] == ' ' and self.rb74.isChecked():
                self.score += 1
            if self.rb84.text()[-1] == ' ' and self.rb84.isChecked():
                self.score += 1

            print(self.score)

        double_(self)

        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]
        self.tiv = tiv
        self.tiv += 1

        self.label1.setText(question.hh(barer))
        self.rb1.setText(question.h1(barer))
        self.rb2.setText(question.h2(barer))
        self.rb3.setText(question.h3(barer))
        self.rb4.setText(question.h4(barer))

        self.label2.setText(question.hh(barer))
        self.rb21.setText(question.h1(barer))
        self.rb22.setText(question.h2(barer))
        self.rb23.setText(question.h3(barer))
        self.rb24.setText(question.h4(barer))

        self.label3.setText(question.hh(barer))
        self.rb31.setText(question.h1(barer))
        self.rb32.setText(question.h2(barer))
        self.rb33.setText(question.h3(barer))
        self.rb34.setText(question.h4(barer))

        self.label4.setText(question.hh(barer))
        self.rb41.setText(question.h1(barer))
        self.rb42.setText(question.h2(barer))
        self.rb43.setText(question.h3(barer))
        self.rb44.setText(question.h4(barer))

        self.label5.setText(question.hh(barer))
        self.rb51.setText(question.h1(barer))
        self.rb52.setText(question.h2(barer))
        self.rb53.setText(question.h3(barer))
        self.rb54.setText(question.h4(barer))

        self.label6.setText(question.hh(barer))
        self.rb61.setText(question.h1(barer))
        self.rb62.setText(question.h2(barer))
        self.rb63.setText(question.h3(barer))
        self.rb64.setText(question.h4(barer))

        self.label7.setText(question.hh(barer))
        self.rb71.setText(question.h1(barer))
        self.rb72.setText(question.h2(barer))
        self.rb73.setText(question.h3(barer))
        self.rb74.setText(question.h4(barer))

        self.label8.setText(question.hh(barer))
        self.rb81.setText(question.h1(barer))
        self.rb82.setText(question.h2(barer))
        self.rb83.setText(question.h3(barer))
        self.rb84.setText(question.h4(barer))

        if self.tiv == 5:
            double_(self)
            self.myButton.hide()
            self.myButton = QPushButton(barer[8], self)
            self.myButton.move(int(width_ * 0.56), int(height_ * 0.85))
            self.myButton.resize(int(width_ * 0.08), int(height_ * 0.05))
            self.myButton.clicked.connect(lambda: self.close())
            self.myButton.clicked.connect(lambda: self.Finish(barer, name_))
            self.myButton.show()
            self.myButton.setStyleSheet(
                'background-color:grey;\n'
                'color:white;\n'
                f'font-size:{width_ // 120}px;\n'
            )

        self.rb1.setChecked(True)
        self.rb21.setChecked(True)
        self.rb31.setChecked(True)
        self.rb41.setChecked(True)
        self.rb51.setChecked(True)
        self.rb61.setChecked(True)
        self.rb71.setChecked(True)
        self.rb81.setChecked(True)

    def Finish(self, barer, name_):

        super().__init__()
        uic.loadUi("end.ui", self)

        self.lib = ['st place', 'Game Over', 'Leaderboard']
        if barer[-1] == 1:
            self.lib = ['-е место', 'Игра окончена', 'Таблица лидеров']
        if barer[-1] == 2:
            self.lib = ['-ին տեղ', 'Խաղն ավարտված է', 'Առաջատարների ցուցանակ']

        self.label_3.setText(f'{barer[9]}: {self.score}/40 {name_.text()}')

        self.label_4.setText(self.lib[1])
        self.label_5.setText(self.lib[2])
        self.label_2.setText(f"1{self.lib[0]}: 40/40 Davit ")
        self.label_6.setText(f"2{self.lib[0]}: 40/40 Karlen")
        self.label_7.setText(f"3{self.lib[0]}: 40/40 User123")

        self.show()

    def showTime(self, barer):
        self.all2 = self.all
        self.hour = self.all2 // 3600
        self.all2 -= self.hour * 3600
        self.minute = self.all2 // 60
        self.all2 -= self.minute * 60
        self.second = self.all2

        self.lbl.setText(f'{self.hour}:{self.minute}:{self.second}')

        self.all -= 1
        if self.all < 0:
            sys.exit(app.exec())

    def keyPressEvent(self, event):
        width_ = pyautogui.size()[0]
        height_ = pyautogui.size()[1]
        if event.key() == 16777216:
            time.sleep(.5)
            sys.exit(app.exec())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_Form(Form)
    Form.show()

    sys.exit(app.exec_())