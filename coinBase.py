from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
import os
from os import path
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import requests

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "coinbase.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.result_button.clicked.connect(self.coinbase)
        self.clear_button.clicked.connect(self.clear_textq)

    def coinbase(self):
        get_1 = str(self.lineEdit.text())
        get_2 = str(self.comboBox_1.currentText())
        get_3 = str(self.comboBox_2.currentText())

        searchPenCode = urllib.parse.quote_plus("{} {} to {}".format(get_1, get_2, get_3))
        url = 'https://www.google.com/search?q=' + searchPenCode
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
        print(title.text)
        self.lineEdit_2.setText(title.text)

    def clear_text(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
