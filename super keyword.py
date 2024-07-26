class A():
    def __init__(self):
        print("A")

    def apple(self):
        print("This is A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

    def Bag(self):
        print("This is B")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

    def care(self):
        print("This is C")

obj1=C()


# Super Keyword used to access the parent class constructor function

#          1.super keyword use pannanumna parent class la inherit pannirukanaum.
#          2.apdi inherit panni erundha parent class sa access pannalam. 
    
