#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QListView)
from PyQt5.QtGui import QFont   
from PyQt5.QtGui import QStandardItemModel, QStandardItem



class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
        
    def initUI(self):
        
        # Basic button
        btn = QPushButton('Button', self)
        btn.move(0, 0)       
        btn.clicked.connect(self.blah)

        
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('TiKi Music Player')    
        self.show()
        
        
        
    def blah(self):
        print ('BLAHHHHH')
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())