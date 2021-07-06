from BackEndChallenge import Services as services
from BackEndChallenge import Repository as repository
#input_letters = input("Digite as letras disponíveis nesta jogada: ")
#array = services.search_word(input_letters.lower())
#print(len(array))
from collections import Counter
str = "adão"
str2 = Counter(str)
print(Counter(str))
dic = {'a': 2, 'c': 4}
dic2 = {'c': 4, 'a': 2}
print(dic == dic2)
for key, value in str2.items():
    print(key)
    print(value)
#print(len(repository.words))