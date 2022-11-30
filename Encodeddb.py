import sys


from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from PyQt5.QtWidgets import (

    QApplication,

    QMainWindow,

    QMessageBox,

    QTableWidget,

    QTableWidgetItem,

)


class Encodeddb(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("Encoded DataBase")

        self.resize(450, 250)

        # Set up the view and load the data

        self.view = QTableWidget()

        self.view.setColumnCount(5)

        self.view.setHorizontalHeaderLabels(
            ["Sr.No.", "Date and Time", "Name", "TypeOfEncode", "Encoded Data"])

        query = QSqlQuery("SELECT * FROM encoded_history")

        while query.next():

            rows = self.view.rowCount()

            self.view.setRowCount(rows + 1)

            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))

            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))

            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))

            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))

            self.view.setItem(rows, 4, QTableWidgetItem(query.value(4)))

        self.view.resizeColumnsToContents()

        self.setCentralWidget(self.view)


def createConnection():

    con = QSqlDatabase.addDatabase("QSQLITE")

    con.setDatabaseName("C:\Steganography\Stegnography_db.db")

    if not con.open():

        QMessageBox.critical(

            None,

            "QTableView Example - Error!",

            "Database Error: %s" % con.lastError().databaseText(),

        )

        return False

    return True


app = QApplication(sys.argv)

if not createConnection():

    sys.exit(1)

win = Encodeddb()

win.show()

sys.exit(app.exec_())
