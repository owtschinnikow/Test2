def fib(n: int):
    """
    Функция вычисления фибинаци
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(5)
    5
    >>> fib(10)
    55
    >>> fib(20)
    6765

    :param n:
    :return:
    """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)