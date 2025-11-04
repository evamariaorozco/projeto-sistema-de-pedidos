import pandas as pd
import sqlite3


novos = pd.read_csv('data/novos_pedidos.csv')


connection = sqlite3.connect('dados.db')
cursor = connection.cursor()


for _, row in novos.iterrows():
    cursor.execute('INSERT INTO pedidos (id_cliente, data) VALUES (?, ?)', (row['id_cliente'], row['data']))
    id_pedido = cursor.lastrowid
    cursor.execute('INSERT INTO itens_pedido (id_pedido, id_produto, quantidade) VALUES (?, ?, ?)',
                    (id_pedido, row['id_produto'], row['quantidade']))

connection.commit()
connection.close()

print('Novos pedidos inseridos com sucesso!')