import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from functions import *

app = QApplication(sys.argv)


window = QWidget()
window.setWindowTitle("Clash Royale Bot")
window.showMaximized()
window.setWindowIcon(QIcon('ClashIcon.png'))
window.setStyleSheet("background: #847577;")
window.setLayout(grid)

frame1()

window.show()
sys.exit(app.exec())
