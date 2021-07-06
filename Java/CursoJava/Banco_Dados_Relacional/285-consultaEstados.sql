-- select * from estados

-- select nome, sigla as 'Nome do Estado' from estados
-- WHERE regiao = 'Sul'

select nome, regiao from estados
WHERE populacao >= 10
order by populacao desc