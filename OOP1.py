class OddEvenSeparator:
    def __init__(self):
        self.listing = []
    def add_number(self, number):
        self.listing.append(number)
    def even(self):
        a = []
        for i in self.listing:
            if i % 2 != 0:
                a.append(i)
        return a
    def odd(self):
        a = []
        for i in self.listing:
            if i % 2 == 0:
                a.append(i)
        return a


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))