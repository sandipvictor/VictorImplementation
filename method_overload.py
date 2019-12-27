class Method_over:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    def add(self, a=None, b=None, c=None,d=None):
        if a != None and b != None and c != None and d !=None:
            return a + b + c +d

        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        else:
            return a



M = Method_over(12,12)
print(M.add(12,23,12,34))
