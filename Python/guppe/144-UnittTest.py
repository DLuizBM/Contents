"""
INTRODUÇÃO AO UNITTEST

Teste Unitários: É a forma de se testar unidades
individuais como métodos, classes, funcionalidades. O objetivo
é mostrar que cada unidade atende sua especificação e encontrar
bugs.

#OBS: testes unitários não são específicos de python, qualquer linguagem
pode fazer, isso está ligado a qualidade do software desenvolvido

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os assertions presentes no módulo.

Para rodar os testes utilizamos unittest.main()

Vamos criar 2 arquivos, o primeiro com funções (Atividades)
o segundo com testes.

TestCase: Caso de teste para sua unidade

#OBS: Verficar as assertion na documentação
ex:
assertEqual(a, b) verifica se a == b
assertNotEqual(a, b) verifica se a != b
etc...

Por convenção, todos os testes em um test case, devem ter seu nome
iniciado com test_

"""