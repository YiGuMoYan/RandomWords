import random
import sys

from PyQt5.QtCore import QStringListModel, QTimer
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel

import SqliteMethds
import createDatabase
import createTable
from ConfigForm import Ui_config
from ConfigSettingForm import Ui_configSetting
from GameForm import Ui_Game
from SelectStartForm import Ui_SelectStart
from WelcomeForm import Ui_welcomeForm
import pyperclip


class Welcome(QMainWindow, Ui_welcomeForm):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        self.setupUi(self)
        self.config.clicked.connect(self.pushConfigBut)
        self.start.clicked.connect(self.pushStartBut)
        self.about.clicked.connect(self.pushAbout)

    def pushConfigBut(self):
        configWin.show()
        configWin.lineEdit.setText('')
        self.hide()

    def pushStartBut(self):
        selectStart.listModel.setStringList(SqliteMethds.getWordsList())
        selectStart.show()
        self.hide()

    def pushAbout(self):
        infoMsg = '成语竞猜\n策划：金乾波老师  臧彤老师\n设计\\开发\\测试：吴易轩\n有任何使用疑问请发送邮箱至 3194775246@qq.com'
        QMessageBox(QMessageBox.Information, '关于', infoMsg).exec_()


class Config(QWidget, Ui_config):
    def __init__(self, parent=None):
        super(Config, self).__init__(parent)
        self.setupUi(self)
        self.confirm.clicked.connect(self.isPass)
        self.backBtn.clicked.connect(self.backWelcome)

    def isPass(self):
        passWord = self.lineEdit.text()
        if passWord == '6bnvl20d':
            configSettingWin.show()
            self.hide()
        else:
            QMessageBox(QMessageBox.Critical, '错误', '秘钥错误').exec_()
            print('密码错误')

    def backWelcome(self):
        welcomeWin.show()
        self.hide()


class ConfigSetting(QWidget, Ui_configSetting):
    def __init__(self, parent=None):
        super(ConfigSetting, self).__init__(parent)
        self.setupUi(self)
        self.inputFile = QFileDialog()
        self.inputUrl = ''
        self.outputFile = QFileDialog()
        self.outputUrl = ''
        self.backBtn.clicked.connect(self.backWelcome)
        self.inputExcle.clicked.connect(self.inputExclFile)
        self.outputExcle.clicked.connect(self.outPutExclFile)
        self.origin.clicked.connect(self.takeOrigin)
        self.copy.clicked.connect(self.takeCopy)

    def backWelcome(self):
        welcomeWin.show()
        self.hide()

    def inputExclFile(self):
        self.inputUrl = self.inputFile.getOpenFileName(self, '请选择导入的Excel文件', '.', '*.xlsx')[0]
        if self.inputUrl:
            createDatabase.createDatabaseInit(self.inputUrl)
            QMessageBox(QMessageBox.Information, '成功', '导入成功').exec_()

    def outPutExclFile(self):
        self.outputUrl = self.outputFile.getSaveFileName(self, '请选择导出的Excel文件', '.', '*.xlsx')[0]
        if self.outputUrl:
            createTable.createTableInit(self.outputUrl)
            QMessageBox(QMessageBox.Information, '成功', '导出成功').exec_()

    @staticmethod
    def takeOrigin():
        createDatabase.createOriginDatabase()
        QMessageBox(QMessageBox.Information, '成功', '已恢复初始数据').exec_()

    @staticmethod
    def takeCopy(self):
        pyperclip.copy('http://42.192.137.54:7646/')
        QMessageBox(QMessageBox.Information, '成功', '已复制链接').exec_()


class SelectStart(QWidget, Ui_SelectStart):
    def __init__(self, parent=None):
        super(SelectStart, self).__init__(parent)
        self.setupUi(self)
        self.listModel = QStringListModel()
        self.listModel.setStringList(SqliteMethds.getWordsList())
        self.listView.setModel(self.listModel)
        self.startBtn.clicked.connect(self.pushStartBtn)
        self.radioButton.clicked.connect(self.pushRadioButton)
        self.listView.clicked.connect(self.pushViewList)
        self.backBtn.clicked.connect(self.pushBakeBtn)
        self.selectList = []

    def pushViewList(self):
        if self.radioButton.isChecked():
            self.radioButton.setChecked(False)

    def pushStartBtn(self):
        for i in self.listView.selectedIndexes():
            self.selectList.append(i.data())
        if not len(self.selectList) == 0:
            print(self.selectList)
            game.initGame(self.selectList, self.timeBox.value())
            game.show()
            self.hide()
        else:
            QMessageBox(QMessageBox.Warning, '警告', '请至少选择一个词库').exec_()

    def pushRadioButton(self):
        if self.radioButton.isChecked():
            self.listView.selectAll()

    def pushBakeBtn(self):
        welcomeWin.show()
        self.hide()


class Game(QWidget, Ui_Game):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.setupUi(self)
        self.wordsList = []
        self.words = []
        self.wordsTemp = []
        self.gameTime = -1
        self.timeTemp = -1
        self.isPlay = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.nextBtn.clicked.connect(self.playGame)
        self.reNew.clicked.connect(self.pushReNew)
        self.backBtn.clicked.connect(self.pushBack)

    def initGame(self, wordsList, gameTime):
        self.wordsList = wordsList
        self.gameTime = gameTime
        self.words = SqliteMethds.getWords(self.wordsList)
        self.wordsTemp.extend(self.words)
        self.timeTemp = self.gameTime
        self.isPlay = False
        self.timer.stop()
        self.wordLabel.setText('')
        self.nextBtn.setText('开始')
        self.timeLabel.setText('剩余 ' + str(round(self.gameTime, 1)) + ' 秒')
        self.nextBtn.setEnabled(True)

    def playGame(self):
        if self.isPlay:
            num = random.randint(0, len(self.wordsTemp) - 1)
            self.wordLabel.setText(self.wordsTemp[num])
            self.wordsTemp.remove(self.wordsTemp[num])
            if len(self.wordsTemp) < (len(self.words) / 10):
                self.wordsTemp.extend(self.words)
        else:
            self.isPlay = True
            self.timer.start(100)
            self.nextBtn.setText('下一个')
            num = random.randint(0, len(self.wordsTemp) - 1)
            self.wordLabel.setText(self.wordsTemp[num])
            self.wordsTemp.remove(self.wordsTemp[num])

    def updateTime(self):
        if self.timeTemp > 0.1:
            self.timeTemp -= 0.1
            text = '剩余 ' + str(round(self.timeTemp, 1)) + ' 秒'
            self.timeLabel.setText(text)
        else:
            self.timeLabel.setText('剩余 0 秒')
            self.isPlay = False
            self.nextBtn.setEnabled(False)
            self.timer.stop()
            self.timeLabel.setStyleSheet("color:red")
            self.timeLabel.setText('时间到了！！！')

    def pushReNew(self):
        self.timeLabel.setStyleSheet("color:black")
        self.initGame(self.wordsList, self.gameTime)

    def pushBack(self):
        selectStart.show()
        self.hide()

    def keyPressEvent(self, event):
        print("按下：" + str(event.key()))
        if event.key() == 16777220 and self.isPlay:
            self.playGame()


if __name__ == '__main__':
    SqliteMethds.setWordDatabase()
    app = QApplication(sys.argv)
    welcomeWin = Welcome()
    welcomeWin.show()
    configWin = Config()
    configSettingWin = ConfigSetting()
    selectStart = SelectStart()
    game = Game()
    sys.exit(app.exec_())
