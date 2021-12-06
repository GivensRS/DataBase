import sqlite3

def InputDB(country, trans, cost):
    test = sqlite3.connect('testdatabase.db')

    cursor = test.cursor()
    cursor.execute("insert into Путешествия values (:country, :trans, :money)",
                   {"country": country, "trans": trans, "money": int(cost)})
    test.commit()

    test.close()