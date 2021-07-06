insert into estados (id, nome, sigla, regiao, populacao)
values(1000, 'Novo', 'NV', 'Sul', 2.13)

insert into estados (nome, sigla, regiao, populacao)
values('Mais Novo', 'MN', 'Sul', 2.54)
-- Notar que ao definir o id e após inserir novamente na tabela
-- o id segue sendo a sequência do últimi definido na tabela
-- sendo assim, o estado Mais Novo terá id = 1001

select * from estados

DELETE  FROM estados 
WHERE sigla = "MN"

select * from estados

DELETE  FROM estados 
WHERE id >= 1000

select * from estados

