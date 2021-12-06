import sqlite3
import InputDB
import Output


print("Введите название страны, средство передвижение и стоимость проезда, для заполнения базы данных.")
a = input().split(" ")
InputDB.InputDB(a[0],a[1],a[2])

b = Output.OutputDB()
for i, n in enumerate(b):
    print(f"{i + 1}. ", *n)
