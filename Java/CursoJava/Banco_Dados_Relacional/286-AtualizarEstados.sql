update estados
set nome = 'Maranhão'
WHERE sigla = 'MA'

select * from estados WHERE sigla = "MA"

update estados
set nome = 'Paraná', populacao = 11.32
WHERE sigla = 'PR'

select nome, populacao from estados WHERE sigla = 'PR'