import sqlite3


def arrange(arrList):
    words = []
    for i in arrList:
        words.append(i[0])
    return words


def getWordsList():
    conn = sqlite3.connect('Words.db')
    cur = conn.cursor()
    sql = 'select * from wordsList'
    result = cur.execute(sql).fetchall()
    print(result)
    conn.close()
    return arrange(result)


def getWords(wordsList):
    words = []
    conn = sqlite3.connect('Words.db')
    cur = conn.cursor()
    for i in wordsList:
        sql = 'select * from ' + i
        words.extend(arrange(cur.execute(sql).fetchall()))
    conn.close()
    return words

def setWordDatabase():
    conn = sqlite3.connect('Words.db')
    cur = conn.cursor()
    sql = 'create table if not exists wordsList(Name text);'
    cur.execute(sql)
    conn.commit()
    conn.close()