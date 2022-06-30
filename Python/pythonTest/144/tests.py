import unittest
from activities import eat, sleep

class ActivitiesTests(unittest.TestCase):
    """
    self.assertEqual(
        function(parameters),
        resultado esperado da função
    )
     
    Se o retorno da função for igual ao resultado esperado, então, passou no teste

    Obs: por convenção, coloca-se o nome do test de test_functio, pois ao executar o unittest.main()
    o programa vai buscar todos os testes que comecem com "test"
    """
    
    def test_eat_healthy(self):
        #docstrings
        """Testing return with healthy food"""
        self.assertEqual(
            eat('quiabo', True),
            'Estou comendo quiabo porque é saudável.'
        )

    def test_eat_not_healthy(self):
        """Testing return with not healthy food"""
        self.assertEqual(
            eat('pizza', False),
            'Estou comendo pizza, pois só se vive uma vez.'
        )
    
    def test_sleep_few_hours(self):
        """Testing return with few hours"""
        self.assertEqual(
            sleep(4),
            'Dormi muito pouco.'
        )
    
    def test_sleep_too_much_hours(self):
        """Testing return with too much hours"""
        self.assertEqual(
            sleep(10),
            'Dormi demais.'
        )

if __name__ == '__main__':
    unittest.main()

