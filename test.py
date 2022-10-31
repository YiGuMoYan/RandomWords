# import json
# import time
#
# from xpinyin import Pinyin
#
# p = Pinyin()
#
# # dataJson = {
# #     'data':
# #         [
# #             {
# #                 'name': '测试1',
# #                 'word': [1, 2, 3]
# #             }
# #         ]
# # }
# #
# # fileJson = open('words.json', 'w')
# # json.dump(dataJson, fileJson, indent=4, ensure_ascii=False)
# # # json.dumps(dataJson, fileJson)
# # fileJson.close()
#
# # fileJson = open('words.json', 'r')
# #
# # print(json.load(fileJson)['1']['name'])
# #
# # fileJson.close()
import xlrd
# import xlsxwriter
#
xl = xlrd.open_workbook('C:/Users/ASUS/Desktop/1.xlsx')
# #
# # tables = xl.sheets()
# # data = []
# #
# # for table in tables:
# #     dir = {}
# #     dir['name'] = table.name
# #     dir['word'] = table.col_values(0)
# #     data.append(dir)
# #     print(table.name)
# #     print(table.col_values(0))
# # dataJson = {}
# # dataJson['data'] = data
# #
# # fileJson = open('words.json', 'w')
# # json.dump(dataJson, fileJson, indent=4, ensure_ascii=False)
# # # json.dumps(dataJson, fileJson)
# # fileJson.close()
#
# #
# # xw = xlsxwriter.Workbook('Words.xlsx')
# # sheet = xw.add_worksheet('词义相近')
# # sheet.activate()
# # for i in range(len(word)):
# #     sheet.write_row('A' + str(i + 1), [str(word[i])])
# # xw.close()
#
#
# # cur = conn.cursor()
# #
# # sql = 'create table if not exists WordsList(Name text);'
# #
# # cur.execute(sql)
#
# # sql = 'create table if not exists ' + p.get_pinyin('词义相近', '_') + ' (words text)'
#
# # sql = 'create table if not exists 词义相近 (words text)'
#
# # cur.execute(sql)
#
#
# # for i in word:
# #     sql = 'insert into 词义相近 (words) values(\'' + i + '\');'
# #     cur.execute(sql)
# #
# # result = cur.execute('select * from 词义相近').fetchall()
# #
# # print(result)
#
# ##########################
# import sqlite3
#
# conn = sqlite3.connect('Words.db')
#
# cur = conn.cursor()
#
# jsonFile = open('words.json', 'r')
#
# jsonData = json.load(jsonFile)['data']
#
# # print(jsonData)
#
# sql = 'create table WordsList(Name text);'
# #
# cur.execute(sql)
#
# for i in jsonData:
#     sql = 'create table if not exists ' + i['name'] + ' (Words text);'
#     cur.execute(sql)
#     print(i['name'])
#     sql = '''insert into WordsList (Name) values ('%s');''' % (i['name'])
#     print(sql)
#     cur.execute(sql)
#     for j in i['words']:
#         sql = 'insert into ' + i['name'] + ' (words) values(\'' + j + '\');'
#         cur.execute(sql)
#
# # cur.execute('insert into WordsList (Name) values (\'只见一字\');')
#
# # result = cur.execute('select name from sqlite_master where type=\'table\';').fetchall()
# #
#
# conn.commit()
#
# result = cur.execute('select * from WordsList').fetchall()
#
# print(result)


# for i in range(10, -0.1, -0.1):
#     print(i)


import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.flag = False
        self.step = 30

        self.lab = QLabel(self)
        self.lab.setStyleSheet("font:200pt '楷体';color: rgb(255, 255, 255);")
        self.lab.setText(str(self.step))  # 设定起始数字
        self.lab.setAlignment(Qt.AlignCenter)
        self.lab.move(200, 150)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        self.timer_2 = QTimer(self)
        self.timer_2.timeout.connect(self.interpurt_even)
        self.timer_2.start(100)

        self.resize(700, 700)
        self.setWindowTitle('倒计时')
        self.show()

    # 定时器2
    def interpurt_even(self):
        if self.step < 6:
            self.lab.setStyleSheet("font:200pt '楷体';color: rgb(255, 0, 0);")
        else:
            self.lab.setStyleSheet("font:200pt '楷体';color: rgb(255, 255, 255);")

    # 定时器1
    def update_func(self):
        if self.step > 0:
            self.step -= 1

        else:
            self.timer.stop()
        self.lab.setText(str(self.step))

    # 检测键盘按键
    def keyPressEvent(self, event):

        print("按下：" + str(event.key()))

        if (event.key() == 16777220):
            self.flag = False
            self.timer.stop()
            self.step = 30
            self.lab.setText(str(self.step))

        if (event.key() == Qt.Key_Space):
            self.flag = bool(1 - self.flag)
            if self.flag == True:
                self.timer.start(1000)
            else:
                self.timer.stop()

        # 按下加号
        if (event.key() == 61):
            self.flag = False
            self.timer.stop()
            self.step += 10
            self.lab.setText(str(self.step))

        # 按下减号
        if (event.key() == 45):
            self.flag = False
            self.timer.stop()
            self.step -= 10
            self.lab.setText(str(self.step))

    # 窗口居中
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

    # 设置背景颜色
    def paintEvent(self, event):
        painter = QPainter(self)
        # todo 1 设置背景颜色
        painter.setBrush(QColor(0, 0, 0))
        painter.drawRect(self.rect())


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
