tuples = [
    (2, 4, 55),
    (14,),
    (1, 2, 3, 4, 5, 6, 7, 8),
    (14, 16, 22, 45, 61, 67, 1, 44),
    (9, 8, 7, 6, 4)
]

result = [sum(item) if len(item) % 2 == 0 else sum(item) / len(item) for item in tuples if 1 < len(item) < 6]

print(result)
