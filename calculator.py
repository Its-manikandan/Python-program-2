class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Add",self.num1+self.num2)


    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sub(self):
        print("Sub",self.num1-self.num2)


    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def mul(self):
        print("Mul",self.num1*self.num2)


    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def div(self):
        print("Div",self.num1/self.num2)

obj=calculator(2,9)
obj.add()

obj1=calculator(2,9)
obj1.sub()

obj2=calculator(2,9)
obj2.mul()

obj3=calculator(2,9)
obj3.div()

