#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon
#function imports
from functions import frame1, frame2, grid

#initiallize GUI application
app = QApplication(sys.argv)

#window and settings
window = QWidget()
window.setWindowTitle("Clash Royale Bot")
window.showMaximized()
window.setWindowIcon(QIcon('ClashIcon.png'))
#place window in (x,y) coordinates
# window.move(2700, 200)
window.setStyleSheet("background: #847577;")

#display frame 1
frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec()) #terminate the app
