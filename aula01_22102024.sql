--criando meu primeiro banco de dados
CREATE DATABASE senac_copacabana;

-- criando minha primeira tabela/ entidade

CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY, -- ou ID
  nome_aluno TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO alunos VALUES (1, 'Marina', 'F');
INSERT INTO alunos VALUES (2, 'Joanna', 'F');

-- consultando as injeções realizadas
SELECT * FROM alunos WHERE minha matricula==1