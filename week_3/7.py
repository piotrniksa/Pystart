from math import sqrt, floor


def is_prime(number):
    for div in range(2, floor(sqrt(number))+1):
        if number % div == 0:
            return False

    return True


print(9, is_prime(9))
print(29, is_prime(29))
