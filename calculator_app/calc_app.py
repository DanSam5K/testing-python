class Calculator(object):
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        """Take two integers and add them together to produce the result.
        >>> calc = Calculator()
        >>> calc.add(1, 1)
        2
        >>> calc.add(25, 125)
        150
        >>> calc.add(1.1, 1.1)
        Traceback (most recent call last):
        ...
        ValueError: Invalid value for 1.1 or 1.1
        """
        if type(x) == int and type(y) == int:
            self.result = x + y
            return self.result
        else:
            raise ValueError(f"Invalid value for {x} or {y}")

    def subtract(self, x, y):
        if type(x) == int and type(y) == int:
            self.result = x - y
            return self.result
        else:
            raise ValueError(f"Invalid value for {x} or {y}")

    def multiply(self, x, y):
        if type(x) == int and type(y) == int:
            self.result = x * y
            return self.result
        else:
            raise ValueError(f"Invalid value for {x} or {y}")

if __name__ == '__main__': # pragma: no cover
    import doctest
    doctest.testmod()