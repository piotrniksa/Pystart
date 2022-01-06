def get_factorial(number: int) -> int:
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1

    return factorial


print(get_factorial(5))
