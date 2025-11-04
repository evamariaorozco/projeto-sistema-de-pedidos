INSERT INTO clientes (nome, cidade) VALUES
('Ana Silva', 'São Paulo'),
('Luciano Lucena', 'João Pessoa'),
('Carla Souza', 'Belo Horizonte');

INSERT INTO produtos (nome, preco) VALUES
('Notebook', 3500.00),
('Mouse', 80.00),
('Teclado', 120.00);

INSERT INTO pedidos (id_cliente, data) VALUES
(1, '2025-10-01'),
(2, '2025-10-02');

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1);