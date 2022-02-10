from PyQt5.QtWidgets import *

import sys

class FirstApp(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout=QVBoxLayout()

        Label =QLabel("First App")
        Line = QLineEdit()
        button=QPushButton("Close")

        layout.addWidget(Label)
        layout.addWidget(Line)
        layout.addWidget(button)
        self.setLayout(layout)

        button.clicked.connect(self.close)
        Line.textChanged.connect(Label.setText)





App =QApplication(sys.argv)

Dialog = FirstApp()

Dialog.show()

App.exec_()