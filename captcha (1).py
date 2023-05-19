from PyQt6.QtWidgets import  QLabel, QVBoxLayout, QPushButton, QLineEdit, QDialog, QMessageBox, QMainWindow
from PyQt6.QtCore import QTimer
a = "svk2d"

class CaptchaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)
        self.timer_label = QLabel("Таймер: 5")
        self.timer_counter = 5
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        self.setLayout(layout)
        with open("style.css", "r") as css:
            self.setStyleSheet(css.read())

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)

        if captcha.lower() == a:
            self.close()
        else:
            self.textbox.setDisabled(True)
            self.timer_counter = 1900
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        self.timer_counter = 5
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0 :
            self.timer.stop()
            self.textbox.setDisabled(False)

