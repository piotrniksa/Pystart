from datetime import datetime


class Book:
    def __init__(self, title, kind, authors, description, summary, rating):
        self.title = title
        self.kind = kind
        self.authors = authors
        self.description = description
        self.summary = summary
        self.rating = rating


class Author:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date


bonifacy = Author('Bonifacy', 'Smith', datetime(1910, 10, 10))
john = Author('John', 'Smith', datetime(1905, 5, 15))
book = Book(
    'Przykładowy tytuł',
    'Kryminał',
    [bonifacy, john],
    'Opis książki',
    'Streszczenie',
    5.0
)
