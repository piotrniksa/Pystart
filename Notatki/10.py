def sum_list(list_1: list, list_2: list) -> list:
    total = []
    for a, b in zip(list_1, list_2):
        total.append(a + b)

    return total


lista_a = [2, 4, 6]
lista_b = [8, 6, 4]

print(sum_list(lista_a, lista_b))
