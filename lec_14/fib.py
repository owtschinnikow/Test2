def fib(n: int):
    """
    Вычисляет число Фибонаачи номер n.
    Выбрасывает исключение TypeError, если вызвана не для целочисленного типа.
    Выбрасыват исключение ValueError, если число отричательное или больше допустимого по контракту.
    :param n: целое число от 0 до 9999
    :return: целое число от 0 до ...

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
    """
    if not isinstance(n, int):
        raise TypeError("Работает только с int type")
    if n < 0:
        raise ValueError("Не может быть негативным")
    if n >= 10000:
        raise ValueError("Cant be more then 9999")
    f = [0, 1] + [0]*(n - 1)
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)