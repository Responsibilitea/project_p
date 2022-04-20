class Vector1:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other


v = Vector1(10)
print(20 + v)
