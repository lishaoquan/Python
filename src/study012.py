# -*- coding: utf-8 -*-
def fact(n):
    '''
    Test fact method
    >>> a1 = fact(-1)
    Traceback (most recent call last):
       ...
    ValueError
    >>> a2 = fact(1)
    >>> a2
    1
    >>> a3 = fact(2)
    >>> a3
    2
    >>> a4 = fact(3)
    >>> a4
    6
    >>> a5 = fact(4)
    >>> a5
    24
    '''
    if n < 1:
     raise ValueError()
    if n == 1:
     return 1
    return n * fact(n - 1)
if __name__ == '__main__':
 import doctest
 doctest.testmod()
