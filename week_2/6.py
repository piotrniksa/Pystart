books = ['W pustyni i w puszczy', 'Krzyżacy', 'Potop']

for book in books:
    print(book)

for book in enumerate(books):
    print(book)

for number, book in enumerate(books):
    print(number, book)

for number, book in enumerate(books, start=1):
    print(number, book)

for number, book in enumerate(reversed(books), start=1):
    print(number, book)
