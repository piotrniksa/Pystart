def euklides_while(a: int, b: int) -> int:
    while b != 0:
        c = a % b
        a, b = b, c

    return a


def test_euklides():
    assert euklides_while(8, 4) == 4
    assert euklides_while(27, 36) == 9
