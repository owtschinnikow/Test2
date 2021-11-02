def foo(x:int, y:int=0, z:int=0) -> int:
    """
    Выводит число в десятичной форме
    :param x:
    :param y:
    :param z:
    :return:
    """
    return 100*x + 10*y + 1*z


def bar(*args, named_parameter = 'bar'):
    for arg in args:
        print(named_parameter, 'arg =', arg)


print('function bar_______________')
bar()
bar(['the', 'list', 'of', 'string'])
bar(1, 2, 3)
bar('jelly', 'fish')
bar('jelly', 'fish', named_parameter= 'SEPARATOR')


print('\n\n', 'function foo_______________', sep='')

print(foo(1, 2, 3))
print(foo(z=1, x=2, y=3))
print(foo(1, 2))
print(foo(7))

