import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton
from PyQt6.QtCore import Qt

def oplatadolga():
    label1.setText("нет долгов")
    label2.setText("Ваш баланс: 4800р")
    label2.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")
    label1.setStyleSheet("color: blue; font-size: 24px; font-weight: bold;")
    button.setStyleSheet("background-color: gray; color: white; font-size: 18px;")
    button.setText("оплачено")

app = QApplication(sys.argv)

window = QLabel()
window.setWindowTitle("Банк")
window.resize(800, 600)
window.move(100, 100)

label1 = QLabel("Ваша задолженность: 200р", window)
label1.setGeometry(0, 200, 800, 50)
label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
label1.setStyleSheet("color: red; font-size: 24px; font-weight: bold;")

label2 = QLabel("Ваш баланс: 5000р", window)
label2.setGeometry(0, 260, 800, 50)
label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
label2.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")

button = QPushButton("оплатить", window)
button.setGeometry(300, 500, 200, 50)
button.setStyleSheet("background-color: green; color: white; font-size: 18px;")
button.clicked.connect(oplatadolga)

window.show()
sys.exit(app.exec())