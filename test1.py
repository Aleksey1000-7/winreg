# первое окно...........................................................................................................
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QStackedLayout, QHBoxLayout, QVBoxLayout, QRadioButton
from sqlalchemy import *
from engine import session
from captcha import CaptchaDialog
from PyQt6.QtCore import Qt
import codecs


class MainWindow(QMainWindow):

    def quit(self):
        quit()
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,170)
        self.layout = QVBoxLayout()
        lbl = QLabel("Укажите свой логин")

        self.Line = QLineEdit()
        lbl_2 = QLabel("Укажите свой пароль")
        self.Line_2 = QLineEdit()
        self.Line.setPlaceholderText ("login")
        self.Line_2.setPlaceholderText("password")
        btn = QPushButton("Войти в систему")
        btn_ss = QPushButton("Выход с приложения")
        lbl.setObjectName("lbl")
        btn_ss.clicked.connect(self.quit)
        btn.clicked.connect(self.btn_click)
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.Line)
        self.layout.addWidget(lbl_2)
        self.layout.addWidget(self.Line_2)
        self.layout.addWidget(btn)
        self.layout.addWidget(btn_ss)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def btn_click(self):
        self.sw = TestWindow()
        sql = text('SELECT * from auth ')
        obj = session.execute(sql)
        for row in obj:
            for login in row:
                for password in row:
                    if self.Line.text() == login and self.Line_2.text() == password:
                        self.sw.show()
                        self.window4.close()

                    else:
                        self.window4 = CaptchaDialog()
                        self.window4.show()

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,150)

        self.name = QLabel("Введите свое Имя и Фамилию")
        self.edit = QLineEdit()
        self.course = QLabel("Введите Группу")
        self.edit1 = QLineEdit()
        box = QVBoxLayout()
        wid = QWidget()
        wid.setLayout(box)
        box.addWidget(self.name)
        box.addWidget(self.edit)
        box.addWidget(self.course)

        box.addWidget(self.edit1)

        lbl1 = QLabel("1.Какой цвет светофора разрешает движение?")
        self.rb1 = QRadioButton(text="Зелёный")
        rb2 = QRadioButton(text="Красный")
        rb3 = QRadioButton(text="Фиолетовый")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        lbl2 = QLabel("2.Основателем какой компании был Стив Джобс?")
        rb1_1 = QRadioButton(text="Fix Price")
        self.rb2_1 = QRadioButton(text="Apple")
        rb3_1 = QRadioButton(text="BMW")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(lbl2)
        vbox2.addWidget(rb1_1)
        vbox2.addWidget(self.rb2_1)
        vbox2.addWidget(rb3_1)

        lbl3 = QLabel("3.Что тяжелее Боинг ИЛ-108 или Виталий Рудницкий?")
        self.rb1_2 = QRadioButton(text="Конечно Виталик ты его пузо видел  ")
        rb2_2 = QRadioButton(text="Одинаково")
        rb3_2 = QRadioButton(text="Боинг ИЛ-108")
        vbox3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox3)
        vbox3.addWidget(lbl3)
        vbox3.addWidget(self.rb1_2)
        vbox3.addWidget(rb2_2)
        vbox3.addWidget(rb3_2)

        lbl4 = QLabel("4.Проверь удачу, 2 + 2?")
        rb1_3 = QRadioButton(text="не решается")
        rb2_3 = QRadioButton(text="2")
        self.rb3_3 = QRadioButton(text="Наум")
        vbox4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox4)
        vbox4.addWidget(lbl4)
        vbox4.addWidget(rb1_3)
        vbox4.addWidget(rb2_3)
        vbox4.addWidget(self.rb3_3)

        lbl5 = QLabel("5.Спустя сколько лет выходит 2 сурс с момента выхода CS:GO?")
        rb1_4 = QRadioButton(text="13")
        self.rb2_4 = QRadioButton(text="11")
        rb3_4 = QRadioButton(text="1")
        vbox5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox5)
        vbox5.addWidget(lbl5)
        vbox5.addWidget(rb1_4)
        vbox5.addWidget(self.rb2_4)
        vbox5.addWidget(rb3_4)

        lbl6 = QLabel("Готовы увидеть свои результаты?")
        lbl6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rb3_5 = QPushButton("Да")
        rb3_5.clicked.connect(self.activate_tab_v)
        rb3_5.clicked.connect(self.result)
        vbox6 = QVBoxLayout()
        widget6 = QWidget()
        widget6.setLayout(vbox6)
        vbox6.addWidget(lbl6)
        vbox6.addWidget(rb3_5)


        lbl7 = QLabel("Результаты теста:")
        self.v6 = QLabel()
        self.v2 = QLabel()
        self.v3 = QLabel()
        self.v4 = QLabel()
        self.v5 = QLabel()
        self.res = QLabel()
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addWidget(self.v6)
        vbox7.addWidget(self.v2)
        vbox7.addWidget(self.v3)
        vbox7.addWidget(self.v4)
        vbox7.addWidget(self.v5)
        vbox7.addWidget(self.res)
        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save)
        vbox7.addWidget(btn_save)


        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)

        self.btnb = QPushButton("back")
        self.btn = QPushButton("next")

        self.btnb.clicked.connect(self.activate_tab_b)
        self.btn.clicked.connect(self.activate_tab_v)
        self.stacklayout.addWidget(wid)
        self.button_layout.addWidget(self.btnb)
        self.button_layout.addWidget(self.btn)

        self.stacklayout.addWidget(widget)

        self.stacklayout.addWidget(widget2)

        self.stacklayout.addWidget(widget3)

        self.stacklayout.addWidget(widget4)

        self.stacklayout.addWidget(widget5)

        self.stacklayout.addWidget(widget6)

        self.stacklayout.addWidget(widget7)



        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            self.setStyleSheet(css.read())

    def activate_tab_v(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)



    def activate_tab_b(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)

    def result(self):
        if self.rb1.isChecked():
            self.v6.setText("1.Верно")
            a = 1
        else:
            self.v6.setText("1.Не верно")
            a = 0
        if self.rb2_1.isChecked():
            self.v2.setText("2.Верно")
            b = a + 1
        else:
            self.v2.setText("2.Не верно")
            b = a
        if self.rb1_2.isChecked():
            self.v3.setText("3.Верно")
            t = b + 1
        else:
            self.v3.setText("3.Не верно")
            t = b
        if self.rb3_3.isChecked():
            self.v4.setText("4.Верно")
            d = t + 1
        else:
            self.v4.setText("4.Не верно")
            d = t
        if self.rb2_4.isChecked():
            self.v5.setText("5.Верно")
            self.e = d + 1
        else:
            self.v5.setText("5.Не верно")
            self.e = d

        self.setFixedSize(400, 200)
        self.res.setText(f"Ваш результат:{self.e}")
    def save(self):
        info = f"Фамилия и Имя:{self.edit.text()} \n"
        cour = f"Группа:{self.edit1.text()} \n"
        txt = f"Ваш результат:{self.v6.text()} \n"
        txt1 = f"Ваш результат:{self.v2.text()} \n"
        txt2 = f"Ваш результат:{self.v3.text()} \n"
        txt3 = f"Ваш результат:{self.v4.text()} \n"
        txt4 = f"Ваш результат:{self.v5.text()} \n"
        txt5 = f"Ваш результат:{self.e} \n"

        with open("results.txt", "w", encoding="utf-8") as f:
            f.write(info)
            f.write(cour)
            f.write(txt)
            f.write(txt1)
            f.write(txt2)
            f.write(txt3)
            f.write(txt4)
            f.write(txt5)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


