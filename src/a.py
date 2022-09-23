class x:
    def __init__(self, m):
        self.m = m

    def c(self):
        print(self.m)


class y(x):
    pass


a = y(5)
a.c()
