class AmericanDate:
    def __init__(self, g, m, d):
        self.g = g
        self.m = m       
        self.d = d
    
    def set_year(self, g):
        self.g = g
    
    def set_month(self, m):
        self.m = m
    
    def set_day(self, d):
        self.d = d
    
    def get_year(self):
        return self.g
    
    def get_month(self):
        if self.m[0] == '0':
            self.m = self.m[1:]        
        return self.m
    
    def get_day(self):
        if self.d[0] == '0':
            self.d = self.d[1:]        
        return self.d
    
    def format(self):
        if len(str(self.d)) < 2:
            self.d = '0' + str(self.d)
        if len(str(self.m)) < 2:
            self.m = '0' + str(self.m)
        return str(self.m) + '.' + str(self.d) + '.' + str(self.g)


class EuropeanDate:
    def __init__(self, g, m, d):
        self.g = g
        self.m = m       
        self.d = d
    
    def set_year(self, g):
        self.g = g
    
    def set_month(self, m):
        self.m = m
    
    def set_day(self, d):
        self.d = d
    
    def get_year(self):
        return self.g
    
    def get_month(self):
        if self.m[0] == '0':
            self.m = self.m[1:]        
        return self.m
    
    def get_day(self):
        if self.d[0] == '0':
            self.d = self.d[1:]        
        return self.d
    
    def format(self):
        if len(str(self.d)) < 2:
            self.d = '0' + str(self.d)
        if len(str(self.m)) < 2:
            self.m = '0' + str(self.m)
        return str(self.d) + '.' + str(self.m) + '.' + str(self.g)


american = AmericanDate(2000, 9, 3)
european = EuropeanDate(2000, 9, 3)
print(american.format())
print(european.format())
american.set_year(2012)
print(american.get_month())
print(american.format())
print(european.format())