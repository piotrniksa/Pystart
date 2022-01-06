def even_filter(list_1: list) -> list:
    return [n for n in list_1 if n % 2 == 0]


print(even_filter([1, 2, 3, 4, 5, 6, 7, 8]))
