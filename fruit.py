#class Fruit:
 #def __init__(self):
 #       self.color="blue"
#
#apple=Fruit()
#print(apple.color)


# Pass the color variable as a parameter through object





class Fruit:
    def __init__(self,color):
        self.color=color

apple=Fruit("red")
print(apple.color)
