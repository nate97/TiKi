import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi


class DemoImpl(QMainWindow):
    def __init__(self, *args):
        super(DemoImpl, self).__init__(*args)

        loadUi('ui/TiKi Music.ui', self)



app = QApplication(sys.argv)
widget = DemoImpl()
widget.show()
sys.exit(app.exec_())