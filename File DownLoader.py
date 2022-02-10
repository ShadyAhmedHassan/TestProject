from PyQt5.QtWidgets import *

import sys

class MyFileDownLoader(QDialog):
    def __init__(self):
        QDialog.__init__(self)


App =QApplication(sys.argv)

Dialog = MyFileDownLoader()

Dialog.show()

App.exec_()