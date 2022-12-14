# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Image.Image

class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(800, 600)
        Game.setMinimumSize(QtCore.QSize(800, 600))
        Game.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/LD.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Game.setWindowIcon(icon)
        Game.setStyleSheet("QWidget{\n"
"    border-radius:20px;\n"
"    border-width: 5px;\n"
"}")
        self.timeLabel = QtWidgets.QLabel(Game)
        self.timeLabel.setGeometry(QtCore.QRect(150, 25, 500, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.timeLabel.setFont(font)
        self.timeLabel.setText("")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.wordLabel = QtWidgets.QLabel(Game)
        self.wordLabel.setGeometry(QtCore.QRect(50, 110, 700, 350))
        font = QtGui.QFont()
        font.setPointSize(100)
        self.wordLabel.setFont(font)
        self.wordLabel.setText("")
        self.wordLabel.setTextFormat(QtCore.Qt.AutoText)
        self.wordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wordLabel.setObjectName("wordLabel")
        self.nextBtn = QtWidgets.QPushButton(Game)
        self.nextBtn.setGeometry(QtCore.QRect(590, 520, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.nextBtn.setFont(font)
        self.nextBtn.setStyleSheet("QPushButton:hover\n"
"{\n"
"\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.493818, fy:0.511, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(221, 255, 253, 255))\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));\n"
"    border-style :ridge;\n"
"}")
        self.nextBtn.setObjectName("nextBtn")
        self.reNew = QtWidgets.QPushButton(Game)
        self.reNew.setGeometry(QtCore.QRect(30, 520, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.reNew.setFont(font)
        self.reNew.setStyleSheet("QPushButton:hover\n"
"{\n"
"\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.493818, fy:0.511, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(221, 255, 253, 255))\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));\n"
"    border-style :ridge;\n"
"}")
        self.reNew.setObjectName("reNew")
        self.backBtn = QtWidgets.QPushButton(Game)
        self.backBtn.setGeometry(QtCore.QRect(20, 20, 75, 30))
        self.backBtn.setStyleSheet("QPushButton:hover\n"
"{\n"
"\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.493818, fy:0.511, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(221, 255, 253, 255))\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(223, 223, 223, 255));\n"
"    border-width: 5px;    \n"
"    border-radius:10px;\n"
"}")
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "????????????"))
        self.nextBtn.setText(_translate("Game", "??????"))
        self.reNew.setText(_translate("Game", "??????"))
        self.backBtn.setText(_translate("Game", "??????"))

