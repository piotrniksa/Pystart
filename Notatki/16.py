def find_divisors(a):
    return{d for d in range(2, a + 1) if a % d == 0}


def gratest_common_divisor(a: int, b: int) -> int:
    div_a = find_divisors(a)
    div_b = find_divisors(b)

    return max(div_a & div_b)


print(gratest_common_divisor(4, 8))
print(gratest_common_divisor(25, 30))
