class Summator:
    def transform(self, n):
        return n
    
    def sum(self, N):
        z = 0
        for i in range(1, N + 1):
            z = z + self.transform(i)
        return z


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

rl = Summator()
print(rl.sum(3))