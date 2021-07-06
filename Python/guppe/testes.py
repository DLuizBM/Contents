import unittest

from atividades import comer, dormir


# a classe herda de unittest
class AtividadesTestes(unittest.TestCase):
    def test_comer(self):
        # lembrando que o self é a classe herdade unittest.TestCase
        # unittest.TestCase.assertEqual( poderia ser feito dessa forma
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo'
        )

        self.assertEqual(
            # comer='pizza', saudave=False -> argumentos nomeados
            comer(comida='pizza', saudave=False),
            'Estou comendo pizza porque só se vive uma vez'
        )


# se o nome da minha aplicação for main
# significa que estamos executando o arquivo diretamente, esse arquivo
if __name__ == '__main__':
    unittest.main()