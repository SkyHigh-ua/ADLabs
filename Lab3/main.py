import sys
import csv
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from ui_interface import Ui_MainWindow
from ISF import IndexStraightFile

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self.window)
        self.setupUi(self)
        self.setWindowTitle('Lab3')
        self.addbtn.clicked.connect(lambda _: self.adddata())
        self.removebtn.clicked.connect(self.removedata)
        self.searchbtn.clicked.connect(self.search)
        self.actionImport.triggered.connect(self.importdata)
        self.tableWidget.itemChanged.connect(self.onchange)
        self.filehandler = IndexStraightFile('./Lab3')

    def adddata(self, data="NULL"):
        self.addingbool = True
        rows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rows)
        self.tableWidget.setItem(rows, 1, QTableWidgetItem())
        self.tableWidget.item(rows, 1).setText(data)
        self.tableWidget.setVerticalHeaderItem(rows, QTableWidgetItem())
        self.tableWidget.verticalHeaderItem(rows).setText(str(self.filehandler.GetId()))
        key = self.filehandler.input(data)
        self.tableWidget.setItem(rows, 0, QTableWidgetItem())
        self.tableWidget.item(rows, 0).setText(str(key))
        self.addingbool = False

    def removedata(self):
        selecteditems = self.tableWidget.selectedItems()
        for item in selecteditems:
            try:
                row = self.tableWidget.row(item)
                self.filehandler.delete(self.tableWidget.verticalHeaderItem(row).text())
                if self.tableWidget.rowCount():
                    self.tableWidget.removeRow(row)
            except RuntimeError:
                continue

    def onchange(self, item):
        if not self.addingbool:
            if item.text() != '':
                self.filehandler.edit(self.tableWidget.verticalHeaderItem(item.row()).text(), item.text())
            else:
                self.filehandler.edit(self.tableWidget.verticalHeaderItem(item.row()).text(), "NULL")
                self.tableWidget.item(item.row(), 1).setText("NULL")

    def search(self):
        self.searchbtn.setIcon(QIcon("test/Lab3/icons/x-circle.svg"))
        self.searchbtn.clicked.disconnect(self.search)
        self.searchbtn.clicked.connect(self.stopsearch)
        if not self.textarea.text().isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText(f"Not valid search [{self.textarea.text()}]")
            msg.setWindowTitle("Fail")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.buttonClicked.connect(self.stopsearch)
            msg.exec()
        else:
            res = self.filehandler.search(self.textarea.text())
            if res is not None:
                for row in range(self.tableWidget.rowCount()):
                    if int(self.tableWidget.verticalHeaderItem(self.tableWidget.row(self.tableWidget.item(row, 0))).text()) == int(res[0]) and self.tableWidget.item(row, 0).text() == res[1] and self.tableWidget.item(row, 1).text() == res[2]:
                        continue
                    else:
                        self.tableWidget.hideRow(row)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText(f"Item with key {self.textarea.text()} not found")
                msg.setWindowTitle("Fail")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.buttonClicked.connect(self.stopsearch)
                msg.exec()

    def stopsearch(self):
        self.searchbtn.setIcon(QIcon("test/Lab3/icons/search.svg"))
        self.searchbtn.clicked.disconnect(self.stopsearch)
        self.searchbtn.clicked.connect(self.search)
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.showRow(row)

    def importdata(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', ".", "CSV files (*.csv)")
        if fname[0]:
            with open(fname[0], 'r') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader, None)
                self.tableWidget.horizontalHeaderItem(1).setText(header[1])
                for row in reader:
                    self.adddata(row[1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
