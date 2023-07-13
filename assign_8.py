class A():
    def __init__(self,a = 10,b = 20,c = 30) :
        self.a = a
        self._b = b
        self.__c = c
    def display(self):
        print(self.a)
        print(self._b)
        print(self.__c)

class B(A):
    def display(self):
        print(self.a)
        print(self._b)
        try :
            print(self.__c)
        except AttributeError:
            print("Cannot access a private variable of base class in child class")
        print("Exiting code..")

obj = B(23,345,45)
obj.display()