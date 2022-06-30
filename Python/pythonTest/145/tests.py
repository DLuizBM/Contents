from Activities import is_funny
import unittest

class ActivitiesTests(unittest.TestCase):

    def test_is_funny(self):
        self.assertFalse(is_funny("Sérgio Malandro"))
        
    def test_is_funny_Jim(self):
        self.assertTrue(is_funny("Jim Carreys"), 'Essa pessoa não é engraçada.')
        # self.assertTrue(function_teste, mensagem em caso de erro) 
    
if __name__ == '__main__':
    unittest.main()