import sqlite3

import xlsxwriter


def arrange(arrList):
    words = []
    for i in arrList:
        words.append(i[0])
    return words


def getWordList():
    conn = sqlite3.connect('Words.db')
    cur = conn.cursor()
    sql = 'select * from wordsList'
    result = cur.execute(sql).fetchall()
    conn.close()
    return arrange(result)


def getTableWordList(word):
    conn = sqlite3.connect('Words.db')
    cur = conn.cursor()
    dirList = {}
    for i in word:
        sql = 'select * from ' + i
        result = cur.execute(sql).fetchall()
        dirList[i] = arrange(result)
    conn.close()
    return dirList


def createTable(word: dir, url):
    xw = xlsxwriter.Workbook(url)
    for key, value in word.items():
        sheet = xw.add_worksheet(key)
        sheet.activate()
        for i in range(len(value)):
            sheet.write_row('A' + str(i + 1), [str(value[i])])
    xw.close()


def createTableInit(url):
    wordList = getWordList()
    wordDir = getTableWordList(wordList)
    print(wordDir)
    createTable(wordDir, url)
