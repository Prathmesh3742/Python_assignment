import math as m

class math_operations :
    def __init__(self,a = 20,b = 30) :
        self.a = a
        self.b = b
    
    def power(self):
        print(f"Square root of {self.a}: ",m.sqrt(self.a))
        print(f"Square root of {self.b}: ",m.sqrt(self.b))
        print(f"{self.a} rays to {self.b}:",m.pow(self.a,self.b))

    def trigno(self):
        print(f"Sine of {self.a} :",m.sin(self.a))
        print(f"Sine of {self.b} :",m.sin(self.b))
        print(f"Cosine of {self.a} :",m.cos(self.a))
        print(f"Cosine of {self.b} :",m.cos(self.b))
        print(f"Tan of {self.a} :",m.tan(self.a))
        print(f"Tan of {self.b} :",m.tan(self.b))