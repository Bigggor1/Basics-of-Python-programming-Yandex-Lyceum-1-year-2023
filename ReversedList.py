class ReversedList:
    def __init__(self, lst):
        self.lst = lst
    
    def __len__(self):
        return len(self.lst)
    
    def __getitem__(self, key):
        return self.lst[0 - key - 1]