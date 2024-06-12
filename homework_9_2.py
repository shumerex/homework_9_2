def create_math_function(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y


add = create_math_function('+')
print(add(3, 4))

multiply = create_math_function('*')
print(multiply(2, 5))


square_lambda = lambda x: x ** 2
print(square_lambda(5))


def square_def(x):
    return x ** 2

print(square_def(5))


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rectangle = Rect(3, 4)
print(rectangle())