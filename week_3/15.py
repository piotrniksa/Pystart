def word_filter(list_2: list) -> list:
    return [word for word in list_2 if 8 > len(word) > 4]


print(word_filter((['jabłko', 'gruszka', 'ananas', 'kiwi', 'pomarańcza'])))
