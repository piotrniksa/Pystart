def count_vowels(text):
    return sum([1 if char in 'aąeęiouy' else 0 for char in text])


print(count_vowels('ala'))

print(count_vowels('programowanie'))
