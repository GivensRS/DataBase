import sqlite3
def OutputDB():
    test = sqlite3.connect('testdatabase.db')

    cursor = test.cursor()
    cursor.execute("SELECT * FROM Путешествия")
    results = cursor.fetchall()

    test.close()
    return results