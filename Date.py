import datetime as dt


class Date:
    def __init__(self, m, d):
        self.my_date = dt.datetime(1999, m, d, 0, 0, 0)
    
    def __sub__(self, other):
        return (self.my_date - other.my_date).days