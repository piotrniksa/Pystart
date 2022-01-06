def filter_vowels2(word):
    vowels = set()
    for letter in word.lower():
        if letter in 'aeiouy':
            vowels.add(letter)

    return vowels


def filter_vowels(word):
    return {char for char in word if char in 'aeiouy'}


print(filter_vowels('Piotr Niksa uczy się programować.'))
