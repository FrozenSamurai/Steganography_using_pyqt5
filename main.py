# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Txt_in_Img_Encode import *
from Txt_in_Img_Decode import *
from Img_in_Img_Encode import *
from Img_in_Img_Decode import *
import sqlite3
from sqlite3 import Error
from Decodeddb import *

database = r"C:\Steganography\Stegnography_db.db"
Pass= 'qwerty'

class Ui_MainWindow(object):
    def opendb(self):
        main()

    def create_connection(self, db):
        conn = None
        try:
            conn = sqlite3.connect(db)
        except Error as e:
            print(e)

        return conn

    def dcdtxt_caller(self):
        e = self.textresultimg.toPlainText()
        e4 = self.textresultimg.toPlainText()
        txt = var2.decode(e4)
        conn = self.create_connection(database)
        with conn:
            print("1. Query all tasks")
            data = (e, "Text in Image",txt)
            # data = (name,c)
            self.insert_data_decode_history(conn, data)
            self.select_all_decode_history(conn)

    def dcdimg_caller(self):
        e = self.resultimg_2.toPlainText()
        conn = self.create_connection(database)
        with conn:
            print("1. Query all tasks")
            data = (e, "Image in Image","Decoded.png")
            # data = (name,c)
            self.insert_data_decode_history(conn, data)
            self.select_all_decode_history(conn)

    def encdtxt_caller(self):
        e = self.hideimgname.toPlainText()
        e2 = self.secretmsg.toPlainText()
        conn = self.create_connection(database)
        with conn:  # INSERT INTO MyTable(MyColumn) VALUES(datetime(CURRENT_TIMESTAMP, 'localtime'))
            print("1. Query all tasks")
            data = (e, "Text in Image",e2)
            # data = (name,c)
            self.insert_data_encode_history(conn, data)
            self.select_all_encode_history(conn)

    def encdimg_caller(self):
        e = self.hide_inimgname.toPlainText()
        e5 = self.hideimgname_2.toPlainText()
        conn = self.create_connection(database)
        with conn:
            print("1. Query all tasks",e5)
            data = (e, "Image in Image")
            # data = (name,c)
            self.insert_data_encode_history(conn, data)
            self.select_all_encode_history(conn)

    # decode_history db
    def select_all_decode_history(self, conn):
        cur = conn.cursor()
        print(sqlite3.sqlite_version)
        cur.execute("SELECT * FROM decoded_history")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def insert_data_decode_history(self, conn, data):
        sql = ''' INSERT INTO decoded_history("Date and Time","Name","TypeOfDecode","Decoded Data")
                VALUES(datetime(CURRENT_TIMESTAMP, 'localtime'),?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    # encode_history db
    def select_all_encode_history(self, conn):
        cur = conn.cursor()
        print(sqlite3.sqlite_version)
        cur.execute("SELECT * FROM encoded_history")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def insert_data_encode_history(self, conn, data):
        sql = ''' INSERT INTO encoded_history("Date and Time","Name","TypeOfEncode", "Encoded Data")
                VALUES(datetime(CURRENT_TIMESTAMP, 'localtime'),?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    #passcheck
    def checkPass(self):
        e1 = self.Password.toPlainText()
        if e1!=Pass:
            self.Incorrectpasslb.setText("INCORRECT PASSWORD, TRY AGAIN")
        else :
            self.button8()

    # GUI code
    def button1(self):
        self.main.hide()
        self.txtinimg.show()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()

    def back1(self):
        self.main.show()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.hide()

    def button2(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.show()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.hide()

    def button3(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.show()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.hide()

    def button4(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.show()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.hide()

    def button5(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.show()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.hide()

    def button6(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.show()
        self.Passframe.hide()
        self.Historymain.hide()

    def button7(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.show()
        self.Historymain.hide()

    def button8(self):
        self.main.hide()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.show()

    def read(self):
        e1 = self.hideimgname.toPlainText()
        # var.img_opn(e1)
        e2 = self.secretmsg.toPlainText()
        # var.usr_msg(e2)
        e3 = self.newimgname.toPlainText()
        # var.new_img_name(e3)
        var.encode(e1, e2, e3)
        self.encdtxt_caller()

    def read_2(self):
        e4 = self.textresultimg.toPlainText()
        decodedtxt = var2.decode(e4)
        ui.decodetxtlb.setText(decodedtxt)
        print(decodedtxt)
        self.dcdtxt_caller()

    def read_3(self):
        e5 = self.hideimgname_2.toPlainText()
        e6 = self.hide_inimgname.toPlainText()
        var3.encode(e5, e6)
        self.encdimg_caller()

    def read_4(self):
        e7 = self.resultimg_2.toPlainText()
        var4.decode(e7)
        self.dcdimg_caller()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 300)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.main.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.txtbt = QtWidgets.QPushButton(self.main)
        self.txtbt.setGeometry(QtCore.QRect(110, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtbt.setFont(font)
        self.txtbt.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.txtbt.setObjectName("txtbt")
        self.imgbt = QtWidgets.QPushButton(self.main)
        self.imgbt.setGeometry(QtCore.QRect(110, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.imgbt.setFont(font)
        self.imgbt.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.imgbt.setObjectName("imgbt")
        self.History = QtWidgets.QPushButton(self.main)
        self.History.setGeometry(QtCore.QRect(10, 220, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.History.setFont(font)
        self.History.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.History.setObjectName("History")
        self.txtinimg = QtWidgets.QFrame(self.centralwidget)
        self.txtinimg.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.txtinimg.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.txtinimg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtinimg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txtinimg.setObjectName("txtinimg")
        self.txtenc = QtWidgets.QPushButton(self.txtinimg)
        self.txtenc.setGeometry(QtCore.QRect(130, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtenc.setFont(font)
        self.txtenc.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.txtenc.setObjectName("txtenc")
        self.txtdcd = QtWidgets.QPushButton(self.txtinimg)
        self.txtdcd.setGeometry(QtCore.QRect(130, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtdcd.setFont(font)
        self.txtdcd.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.txtdcd.setObjectName("txtdcd")
        self.label = QtWidgets.QLabel(self.txtinimg)
        self.label.setGeometry(QtCore.QRect(100, 160, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.backtomain = QtWidgets.QPushButton(self.txtinimg)
        self.backtomain.setGeometry(QtCore.QRect(20, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backtomain.setFont(font)
        self.backtomain.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.backtomain.setObjectName("backtomain")
        self.encodetxt = QtWidgets.QFrame(self.centralwidget)
        self.encodetxt.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.encodetxt.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.encodetxt.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.encodetxt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.encodetxt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.encodetxt.setObjectName("encodetxt")
        self.label_2 = QtWidgets.QLabel(self.encodetxt)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.encodetxt)
        self.label_3.setGeometry(QtCore.QRect(16, 110, 181, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.encodetxt)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 291, 31))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.encodetxt)
        self.label_7.setGeometry(QtCore.QRect(90, 20, 111, 16))
        self.label_7.setObjectName("label_7")
        self.backtotxtinimg = QtWidgets.QPushButton(self.encodetxt)
        self.backtotxtinimg.setGeometry(QtCore.QRect(20, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backtotxtinimg.setFont(font)
        self.backtotxtinimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.backtotxtinimg.setObjectName("backtotxtinimg")
        self.okenctxt = QtWidgets.QPushButton(self.encodetxt)
        self.okenctxt.setGeometry(QtCore.QRect(220, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okenctxt.setFont(font)
        self.okenctxt.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.okenctxt.setObjectName("okenctxt")
        self.hideimgname = QtWidgets.QTextEdit(self.encodetxt)
        self.hideimgname.setGeometry(QtCore.QRect(10, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hideimgname.setFont(font)
        self.hideimgname.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.hideimgname.setObjectName("hideimgname")
        self.secretmsg = QtWidgets.QTextEdit(self.encodetxt)
        self.secretmsg.setGeometry(QtCore.QRect(10, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secretmsg.setFont(font)
        self.secretmsg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.secretmsg.setObjectName("secretmsg")
        self.newimgname = QtWidgets.QTextEdit(self.encodetxt)
        self.newimgname.setGeometry(QtCore.QRect(10, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newimgname.setFont(font)
        self.newimgname.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.newimgname.setObjectName("newimgname")
        self.decodetxt = QtWidgets.QFrame(self.centralwidget)
        self.decodetxt.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.decodetxt.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.decodetxt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decodetxt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decodetxt.setObjectName("decodetxt")
        self.label_5 = QtWidgets.QLabel(self.decodetxt)
        self.label_5.setGeometry(QtCore.QRect(40, 50, 241, 21))
        self.label_5.setObjectName("label_5")
        self.decodetxtlb = QtWidgets.QLabel(self.decodetxt)
        self.decodetxtlb.setGeometry(QtCore.QRect(60, 120, 201, 51))
        self.decodetxtlb.setObjectName("decodetxtlb")
        self.label_8 = QtWidgets.QLabel(self.decodetxt)
        self.label_8.setGeometry(QtCore.QRect(110, 10, 91, 31))
        self.label_8.setObjectName("label_8")
        self.backtotxtinimg_2 = QtWidgets.QPushButton(self.decodetxt)
        self.backtotxtinimg_2.setGeometry(QtCore.QRect(20, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backtotxtinimg_2.setFont(font)
        self.backtotxtinimg_2.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.backtotxtinimg_2.setObjectName("backtotxtinimg_2")
        self.okdcdtxt = QtWidgets.QPushButton(self.decodetxt)
        self.okdcdtxt.setGeometry(QtCore.QRect(230, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okdcdtxt.setFont(font)
        self.okdcdtxt.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.okdcdtxt.setObjectName("okdcdtxt")
        self.textresultimg = QtWidgets.QTextEdit(self.decodetxt)
        self.textresultimg.setGeometry(QtCore.QRect(40, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textresultimg.setFont(font)
        self.textresultimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.textresultimg.setObjectName("textresultimg")
        self.imginimg = QtWidgets.QFrame(self.centralwidget)
        self.imginimg.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.imginimg.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.imginimg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imginimg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imginimg.setObjectName("imginimg")
        self.encimg = QtWidgets.QPushButton(self.imginimg)
        self.encimg.setGeometry(QtCore.QRect(110, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.encimg.setFont(font)
        self.encimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.encimg.setObjectName("encimg")
        self.dcdimg = QtWidgets.QPushButton(self.imginimg)
        self.dcdimg.setGeometry(QtCore.QRect(110, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dcdimg.setFont(font)
        self.dcdimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.dcdimg.setObjectName("dcdimg")
        self.label_9 = QtWidgets.QLabel(self.imginimg)
        self.label_9.setGeometry(QtCore.QRect(80, 180, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.backtomain_2 = QtWidgets.QPushButton(self.imginimg)
        self.backtomain_2.setGeometry(QtCore.QRect(20, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backtomain_2.setFont(font)
        self.backtomain_2.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.backtomain_2.setObjectName("backtomain_2")
        self.encodeimg = QtWidgets.QFrame(self.centralwidget)
        self.encodeimg.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.encodeimg.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.encodeimg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.encodeimg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.encodeimg.setObjectName("encodeimg")
        self.label_10 = QtWidgets.QLabel(self.encodeimg)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 301, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.encodeimg)
        self.label_11.setGeometry(QtCore.QRect(20, 150, 281, 41))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.encodeimg)
        self.label_13.setGeometry(QtCore.QRect(100, 20, 111, 16))
        self.label_13.setObjectName("label_13")
        self.backtoimginimg = QtWidgets.QPushButton(self.encodeimg)
        self.backtoimginimg.setGeometry(QtCore.QRect(30, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backtoimginimg.setFont(font)
        self.backtoimginimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.backtoimginimg.setObjectName("backtoimginimg")
        self.okencimg = QtWidgets.QPushButton(self.encodeimg)
        self.okencimg.setGeometry(QtCore.QRect(230, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okencimg.setFont(font)
        self.okencimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.okencimg.setObjectName("okencimg")
        self.hideimgname_2 = QtWidgets.QTextEdit(self.encodeimg)
        self.hideimgname_2.setGeometry(QtCore.QRect(50, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hideimgname_2.setFont(font)
        self.hideimgname_2.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.hideimgname_2.setObjectName("hideimgname_2")
        self.hide_inimgname = QtWidgets.QTextEdit(self.encodeimg)
        self.hide_inimgname.setGeometry(QtCore.QRect(40, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hide_inimgname.setFont(font)
        self.hide_inimgname.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.hide_inimgname.setObjectName("hide_inimgname")
        self.decodeimg = QtWidgets.QFrame(self.centralwidget)
        self.decodeimg.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.decodeimg.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.decodeimg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decodeimg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decodeimg.setObjectName("decodeimg")
        self.label_12 = QtWidgets.QLabel(self.decodeimg)
        self.label_12.setGeometry(QtCore.QRect(20, 80, 271, 21))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.decodeimg)
        self.label_15.setGeometry(QtCore.QRect(110, 20, 91, 31))
        self.label_15.setObjectName("label_15")
        self.backtoimginimg_2 = QtWidgets.QPushButton(self.decodeimg)
        self.backtoimginimg_2.setGeometry(QtCore.QRect(30, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backtoimginimg_2.setFont(font)
        self.backtoimginimg_2.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.backtoimginimg_2.setObjectName("backtoimginimg_2")
        self.okdcdimg = QtWidgets.QPushButton(self.decodeimg)
        self.okdcdimg.setGeometry(QtCore.QRect(210, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okdcdimg.setFont(font)
        self.okdcdimg.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.okdcdimg.setObjectName("okdcdimg")
        self.resultimg_2 = QtWidgets.QTextEdit(self.decodeimg)
        self.resultimg_2.setGeometry(QtCore.QRect(40, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resultimg_2.setFont(font)
        self.resultimg_2.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.resultimg_2.setObjectName("resultimg_2")

        self.Passframe = QtWidgets.QFrame(self.centralwidget)
        self.Passframe.setGeometry(QtCore.QRect(0, 0, 321, 271))
        self.Passframe.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.Passframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Passframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Passframe.setObjectName("Passframe")
        self.label_6 = QtWidgets.QLabel(self.Passframe)
        self.label_6.setGeometry(QtCore.QRect(120, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(self.Passframe)
        self.label_14.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.Password = QtWidgets.QTextEdit(self.Passframe)
        self.Password.setGeometry(QtCore.QRect(130, 120, 171, 31))
        self.Password.setObjectName("Password")
        self.okCheckpass = QtWidgets.QPushButton(self.Passframe)
        self.okCheckpass.setGeometry(QtCore.QRect(210, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okCheckpass.setFont(font)
        self.okCheckpass.setObjectName("okCheckpass")
        self.backfrmhis = QtWidgets.QPushButton(self.Passframe)
        self.backfrmhis.setGeometry(QtCore.QRect(30, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backfrmhis.setFont(font)
        self.backfrmhis.setObjectName("backfrmhis")
        self.Incorrectpasslb = QtWidgets.QLabel(self.Passframe)
        self.Incorrectpasslb.setGeometry(QtCore.QRect(40, 180, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Incorrectpasslb.setFont(font)
        self.Incorrectpasslb.setText("")
        self.Incorrectpasslb.setObjectName("Incorrectpasslb")
        self.Historymain = QtWidgets.QFrame(self.centralwidget)
        self.Historymain.setGeometry(QtCore.QRect(0, 0, 321, 271))
        self.Historymain.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.Historymain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Historymain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Historymain.setObjectName("Historymain")
        self.label_16 = QtWidgets.QLabel(self.Historymain)
        self.label_16.setGeometry(QtCore.QRect(110, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.Encddb = QtWidgets.QPushButton(self.Historymain)
        self.Encddb.setGeometry(QtCore.QRect(90, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Encddb.setFont(font)
        self.Encddb.setObjectName("Encddb")
        self.dcddb = QtWidgets.QPushButton(self.Historymain)
        self.dcddb.setGeometry(QtCore.QRect(90, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dcddb.setFont(font)
        self.dcddb.setObjectName("dcddb")
        self.clearbt = QtWidgets.QPushButton(self.Historymain)
        self.clearbt.setGeometry(QtCore.QRect(224, 240, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clearbt.setFont(font)
        self.clearbt.setObjectName("clearbt")
        self.Backtomainm = QtWidgets.QPushButton(self.Historymain)
        self.Backtomainm.setGeometry(QtCore.QRect(20, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Backtomainm.setFont(font)
        self.Backtomainm.setObjectName("Backtomainm")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # listners
        self.txtbt.clicked.connect(self.button1)
        self.imgbt.clicked.connect(self.button2)
        self.txtenc.clicked.connect(self.button3)
        self.txtdcd.clicked.connect(self.button4)
        self.backtomain.clicked.connect(self.back1)
        self.backtotxtinimg.clicked.connect(self.button1)
        self.backtotxtinimg_2.clicked.connect(self.button1)
        self.encimg.clicked.connect(self.button5)
        self.dcdimg.clicked.connect(self.button6)
        self.backtomain_2.clicked.connect(self.back1)
        self.backtoimginimg.clicked.connect(self.button2)
        self.backtoimginimg_2.clicked.connect(self.button2)
        self.okenctxt.clicked.connect(self.read)
        self.okdcdtxt.clicked.connect(self.read_2)
        self.okencimg.clicked.connect(self.read_3)
        self.okdcdimg.clicked.connect(self.read_4)
        self.History.clicked.connect(self.button7)
        self.backfrmhis.clicked.connect(self.back1)
        self.okCheckpass.clicked.connect(self.checkPass)
        self.Backtomainm.clicked.connect(self.back1)

        self.main.show()
        self.txtinimg.hide()
        self.encodetxt.hide()
        self.decodetxt.hide()
        self.imginimg.hide()
        self.encodeimg.hide()
        self.decodeimg.hide()
        self.Passframe.hide()
        self.Historymain.hide()

        # database connectivity
        # conn = self.create_connection(database)
        # with conn:
        #     print("1. Query all tasks")

        #     # data = (name,c)
        # self.insert_data(conn,data)
        # self.select_all_student(conn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganography"))
        self.txtbt.setText(_translate("MainWindow", "Text in Image"))
        self.imgbt.setText(_translate("MainWindow", "Image in Image"))
        self.History.setText(_translate("MainWindow", "History"))
        self.txtenc.setText(_translate("MainWindow", "Encode"))
        self.txtdcd.setText(_translate("MainWindow", "Decode"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#000000;\">TEXT IN IMAGE</span></p></body></html>"))
        self.backtomain.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter image name(with extension) :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter data to be encoded : </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Enter the name of new image(with extension) : </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">ENCODE</span></p></body></html>"))
        self.backtotxtinimg.setText(_translate("MainWindow", "Back"))
        self.okenctxt.setText(_translate("MainWindow", "OK"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter image name(with extension) :</span></p></body></html>"))
        self.decodetxtlb.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Decoded Text : </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">DECODE</span></p></body></html>"))
        self.backtotxtinimg_2.setText(_translate("MainWindow", "Back"))
        self.okdcdtxt.setText(_translate("MainWindow", "OK"))
        self.encimg.setText(_translate("MainWindow", "Encode"))
        self.dcdimg.setText(_translate("MainWindow", "Decode"))
        self.label_9.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">IMAGE IN IMAGE</span></p></body></html>"))
        self.backtomain_2.setText(_translate("MainWindow", "Back"))
        self.label_10.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter the name of the image which you want to hide</span></p><p align=\"center\"><span style=\" font-weight:600;\">(with extension) :</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter the name of the image in which you want to hide</span></p><p align=\"center\"><span style=\" font-weight:600;\">(with extension) :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">ENCODE</span></p></body></html>"))
        self.backtoimginimg.setText(_translate("MainWindow", "Back"))
        self.okencimg.setText(_translate("MainWindow", "OK"))
        self.label_12.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Enter image name(with extension) :</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">DECODE</span></p></body></html>"))
        self.backtoimginimg_2.setText(_translate("MainWindow", "Back"))
        self.okdcdimg.setText(_translate("MainWindow", "OK"))
        self.label_6.setText(_translate("MainWindow", "HISTORY"))
        self.label_14.setText(_translate("MainWindow", "Enter Password"))
        self.okCheckpass.setText(_translate("MainWindow", "OK"))
        self.backfrmhis.setText(_translate("MainWindow", "Back"))
        self.label_16.setText(_translate("MainWindow", "HISTORY"))
        self.Encddb.setText(_translate("MainWindow", "ENCODED HISTORY"))
        self.dcddb.setText(_translate("MainWindow", "DECODED HISTORY"))
        self.clearbt.setText(_translate("MainWindow", "Clear History"))
        self.Backtomainm.setText(_translate("MainWindow", "Back"))

if __name__ == "__main__":
    var = encode_class()
    var2 = decode_class()
    var3 = encimgclass()
    var4 = dcdimgclass()
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())