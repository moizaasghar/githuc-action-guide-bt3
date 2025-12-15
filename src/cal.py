class calculator:
    def add(self, a,b):
        return a+b

    def sub(self, a,b):
        return a-b
    
    def mul(self, a,b):
        return a*b
    
    def divide(self, a,b):
        if b == 0:
            return "I can't divide it with zero"
        return  a/b