def cut(start: int, end: int):
    def wrapper(function):
        def inner_wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result[start:end]

        return inner_wrapper

    return wrapper


def test_cut_list():
    @cut(1, 5)
    def sample():
        return [0, 1, 2, 3, 4, 5, 6, 7]

    assert sample() == [1, 2, 3, 4]
