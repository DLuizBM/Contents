-- Comentário
-- Criando tabela estado

-- criando coluna id do tipo int unsigned(sem sinal) não aceita nulo(not null)
    -- auto incrementado (AUTO_INCREMENT)

    -- nome vai ser um varchar de 45 posições (string de 45 caracteres)

    -- sigla dos estados, varchar de 2 posições

    -- região está enumerada(ENUM), significa que dentro desse campo, só pode haver os valores
    -- enumerados, ou seja, obrigatoriamente deve ser um dos 5

    -- populacao, decimal de 5 casas, sendo 2 de ponto flutuante

    -- PRIMARY KEY (id), definindo a pk como o id

    -- UNIQUE KEY(nome), UNIQUE KEY(sigla), nem o nome nem a sigla aceitam duplicidade

create table estados (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    nome VARCHAR(45) NOT NULL,
    sigla VARCHAR(2) NOT NULL,
    regiao ENUM('Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste') NOT NULL,
    populacao DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY(nome), 
    UNIQUE KEY(sigla)
);