class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


x = A("1", "2", "3")
print(x.__dict__)
print(x)
y = x.__dict__.pop("a")
print(y)
x.__dict__.update({"c": "4"})
print(x.__dict__)
