def delete_vowels(word: str) -> str:
    new_word = ''
    for char in word.lower():
        if char not in 'aąeęiouy':
            new_word += char
    return new_word


def test_delete_vowels():
    assert delete_vowels('blok') == 'blk'
    assert delete_vowels('Uczę się programowania') == 'cz s prgrmwn'
