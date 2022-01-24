from json import load, dump

try:
    with open('books.json') as data:
        library = load(data)
except FileNotFoundError:
    library = []

choice = input('Witaj w Twojej bibliotece. Dostępne polecenia: [w]ypisz / [d]odaj: ')
if choice == "w":
    print('Książki w Twojej bibliotece: ')
    for book in library:
        print(f'{book["author"]} - "{book["title"]}". Liczba stron: {book["number_of_pages"]}.')
elif choice == "d":
    author = input('Podaj imię i nazwisko autora: ')
    title = input('Podaj tytuł książki: ')
    number_of_pages = int(input('Podaj liczbę stron: '))

    library.append({
        "author": author,
        "title": title,
        "number_of_pages": number_of_pages
    })
    with open('books.json', "w") as data:
        dump(library, data)
