-- criando minha primeira tabela/entidade
CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  nome_aluno TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO alunos VALUES (1, 'Marina', 'F');
INSERT INTO alunos VALUES (2, 'Joana', 'F');


-- consultando as injeções realizadas
SELECT * FROM alunos WHERE matricula=1

 CREATE TABLE professores (
  inscricao INTEGER PRIMARY KEY,
  nome_professor TEXT NOT NULL,
  genero TEXT NOT NULL
);


-- injeção de dados-teste
INSERT INTO professores VALUES (1,'Elton', 'M');
INSERT INTO professores VALUES (2,'Anderson', 'M');

-- consultando as injeções realizadas
SELECT * FROM alunos ;
SELECT * FROM professores ;