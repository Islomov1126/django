from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolButton(QMainWindow):

    def __init__(self):
        super(ToolButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ToolButton")
        self.setGeometry(400,400,300,260)

        self.table = QTableWidget(self)
        self.table.setGeometry(400, 30, 1300, 600)

        #Column count
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Id', 'name', 'city', 'email', 'logo'])
        self.table.hideColumn(0)

        self.table.setFont(QFont('new roman times', 14))
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)        
        import requests

        url = "http://127.0.0.1:8000/apiv0/publishers/"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        row = self.table.rowCount()

        for item in list(response.json()):
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(item['id']))
            self.table.setItem(row, 1, QTableWidgetItem(item['name']))
            self.table.setItem(row, 2, QTableWidgetItem(item['city']))
            self.table.setItem(row, 3, QTableWidgetItem(item['email']))
            self.table.setItem(row, 4, QTableWidgetItem(item['logo']))

            row += 1
            
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToolButton()
    ex.show()
    sys.exit(app.exec_()) 