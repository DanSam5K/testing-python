class Calculator(object):
    def __init__(self):
        self.result = 0

    def add(self, x, y):
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

