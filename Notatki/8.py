def calculate_common_divisor(a, b):
    common_divisors = set()
    for n in range(1, a+1) and range(1, b+1):
        if a % n == 0 and b % n == 0:
            common_divisors.add(n)

    return sorted(list(common_divisors))


test1 = calculate_common_divisor(16, 8)
print(test1)
