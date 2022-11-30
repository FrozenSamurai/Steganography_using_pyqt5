import sys


from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import PyQt5.QtWidgets


class Decodeddb(PyQt5.QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Decoded DataBase")

        self.resize(450, 250)

        # Set up the view and load the data

        self.view = PyQt5.QtWidgets.QTableWidget()

        self.view.setColumnCount(5)

        self.view.setHorizontalHeaderLabels(
            ["Sr.No.", "Date and Time", "Name", "TypeOfDecode", "Decoded Data"])

        query = QSqlQuery("SELECT * FROM decoded_history")

        while query.next():

            rows = self.view.rowCount()

            self.view.setRowCount(rows + 1)

            self.view.setItem(
                rows, 0, PyQt5.QtWidgets.QTableWidgetItem(str(query.value(0))))

            self.view.setItem(
                rows, 1, PyQt5.QtWidgets.QTableWidgetItem(query.value(1)))

            self.view.setItem(
                rows, 2, PyQt5.QtWidgets.QTableWidgetItem(query.value(2)))

            self.view.setItem(
                rows, 3, PyQt5.QtWidgets.QTableWidgetItem(query.value(3)))

            self.view.setItem(
                rows, 4, PyQt5.QtWidgets.QTableWidgetItem(query.value(4)))

        self.view.resizeColumnsToContents()

        self.setCentralWidget(self.view)


def createConnection():

    con = QSqlDatabase.addDatabase("QSQLITE")

    con.setDatabaseName("C:\Steganography\Stegnography_db.db")

    if not con.open():

        PyQt5.QtWidgets.QMessageBox.critical(

            None,

            "QTableView Example - Error!",

            "Database Error: %s" % con.lastError().databaseText(),

        )

        return False

    return True


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)

    if not createConnection():
        # print(error)
        sys.exit(1)

    win1 = Decodeddb()

    win1.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
