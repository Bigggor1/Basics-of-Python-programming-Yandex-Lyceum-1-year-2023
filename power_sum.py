class Summator:
    def transform(self, n):
        return n 
    
    def sum(self, N):
        z = 0
        for i in range(1, N + 1):
            z = z + self.transform(i)
        return z


class PowerSummator(Summator):
    def __init__(self, g):
        self.g = g
    
    def transform(self, n):
        return n ** self.g    


class SquareSummator(PowerSummator):
    def transform(self, n):
        return n ** 2


class CubeSummator(PowerSummator):
    def transform(self, n):
        return n ** 3

tl = PowerSummator(2)
print(tl.sum(3))