import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
import sqlite3


class Espresso(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.reader = self.all_read()
        self.loadTable()

    def all_read(self):
        try:
            conn = sqlite3.connect('coffee.sqlite')
            cur = conn.cursor()
            tmp = cur.execute("SELECT * FROM all_coffee").fetchall()
            conn.close()
            return tmp
        except:
            print('Ошибка чтения базы')

    def loadTable(self):
        title = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена',
                 'объем упаковки']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.reader):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            row = [i for i in row]
            if row[2] is None:
                row[2] = 'Растворимый'
            elif row[2] == 1:
                row[2] = 'Светлая'
            elif row[2] == 2:
                row[2] = 'Средняя'
            elif row[2] == 3:
                row[2] = 'Темная'
            elif row[2] == 4:
                row[2] = 'Высшая'
            if row[3]:
                row[3] = 'Молотый'
            else:
                row[3] = 'Растворимый'
            print(row)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setColumnWidth(4, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
