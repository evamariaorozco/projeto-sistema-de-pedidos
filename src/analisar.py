import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


connection = sqlite3.connect('dados.db')


query = '''
SELECT c.nome AS cliente, SUM(p.preco * i.quantidade) AS total_gasto
FROM clientes c
JOIN pedidos pe ON c.id = pe.id_cliente
JOIN itens_pedido i ON pe.id = i.id_pedido
JOIN produtos p ON p.id = i.id_produto
GROUP BY c.nome;
'''


analisar = pd.read_sql_query(query, connection)
print(analisar)


plt.bar(analisar['cliente'], analisar['total_gasto'])
plt.title('Total gasto por cliente')
plt.ylabel('Valor (R$)')
plt.xlabel('Cliente')
plt.tight_layout()
plt.show()