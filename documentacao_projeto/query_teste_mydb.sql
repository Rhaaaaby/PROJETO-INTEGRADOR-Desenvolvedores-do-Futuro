use mydb;

select * from Usuario;

select * from Produto;

select * from Categoria;

SELECT * FROM Cadastro_Produto;

INSERT INTO Cadastro_Produto (Nome, Descricao) VALUES ('Teste', 'Cadastro para teste');

-- Adicionando categorias manualmente

INSERT INTO Categoria (id_Categoria, Nome, Descricao) VALUES
(1, 'Alimentos', 'Alimentos diversos'),
(2, 'Roupas', 'Roupas diversas'),
(3, 'Livros', 'Livros diversos'),
(4, 'Brinquedos', 'Brinquedos diversos');

-- Adicionando tempo automático no banco:
ALTER TABLE Produto 
ALTER COLUMN Criado_em DATETIME NOT NULL;

ALTER TABLE Produto 
ADD CONSTRAINT DF_Produto_Criado_em DEFAULT GETDATE() FOR Criado_em;