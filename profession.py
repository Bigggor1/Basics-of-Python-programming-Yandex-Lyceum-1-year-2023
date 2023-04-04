class Profile:
    def __init__(self, prof):
        self.prof = prof
    
    def info(self):
        return ''
    
    def describe(self):
        print(self.prof, self.info())


class Vacancy(Profile):
    def __init__(self, prof, money):
        self.money = money
        super().__init__(prof)
    
    def info(self):
        return f'Предлагаемая зарплата: {self.money}'


class Resume(Profile):
    def __init__(self, prof, exp):
        self.exp = exp
        super().__init__(prof)
    
    def info(self):
        return f'Стаж работы: {self.exp}'