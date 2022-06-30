"""
Hooks: São testes em si. Ou seja, a execução dos testes. 

setup() -> é executado antes dos testes. É útil para criarmos instâncias de objetos
e outros dados;

tearDown() -> é executado ao final de cada métodos de teste. É útil para excluir dados ou 
fechar conexões com banco de dados.
"""

import unittest

class TesteModule(unittest.TestCase):

    def setup(self):
        # configurações de setUp
        pass

    def test_one(self):
        # setUp vai rodar antes do testes
        # tearDown vai rodar após o teste
        pass

    def test_two(self):
        # setUp vai rodar antes do testes
        # tearDown vai rodar após o teste
        pass

    def tearDown(self):
        # configurações de tearDown
        pass
