import sqlite3

connection = sqlite3.connect('dados.db')
cursor = connection.cursor()

with open('sql/schema.sql', 'r') as f:
    cursor.executescript(f.read())

with open('sql/populate.sql', 'r') as f:
    cursor.executescript(f.read())

connection.commit()
connection.close()

print('Database criada com sucesso!')

