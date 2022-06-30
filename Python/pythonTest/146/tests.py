import unittest
from Robot import Robot

class RobotTest(unittest.TestCase):

    def setUp(self):
        """
        Com setUp podemos criar um objeto que pode ser utilizado em todos os testes, evitando assim
        a repetição de código. Basta criar utilizando o self e utilizar para recuperar esse objeto.
        """
        self.optimus = Robot(name='Optimus', battery=50)
        print("SetUp sendo executado.")
    
    def test_charge(self):
        #optimus = Robot(name='Optimus', battery=50)
        self.optimus.charge()
        self.assertEqual(self.optimus.battery, 100) 

    def test_say_name(self):
        #optimus = Robot(name='Optimus')
        self.assertEqual(self.optimus.say_name(), "Oi, eu sou o robô Optimus.")
        self.assertEqual(self.optimus.battery, 49, "A bateria deveria estar em 49%")
        #self.assertEqual(o que deve ser testado, resultado esperado do teste, mensagem em caso de erro)

    def tearDown(self):
        """Executado depois do teste."""
        print("Tear down sendo executado.")

if __name__ == '__main__':
    unittest.main()