from BackEndChallenge import Repository as repository

array_with_word_with_letters = []


def treat_letter(letters):
    new_letters = ""
    for test_letter in letters:
        if test_letter in repository.letters_with_accent:
            for letter in letters:
                if letter == 'á' or letter == 'ã' or letter == 'â':
                    new_letters += 'a'
                elif letter == 'ç':
                    new_letters += 'c'
                elif letter == 'í':
                    new_letters += 'i'
                elif letter == 'ú':
                    new_letters += 'u'
        else:
            new_letters += test_letter
    return new_letters


def search_word(letters):
    treated_letters = treat_letter(letters)
    for word in repository.words:
        for letter in treated_letters:
            treated_word = treat_letter(word.lower())
            if letter in treated_word and treated_word not in array_with_word_with_letters:
                array_with_word_with_letters.append(treated_word)
    return array_with_word_with_letters





