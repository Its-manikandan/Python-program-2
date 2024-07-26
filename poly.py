class animal():
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog Barks")

class bird(animal):
    def sound(self):
        print("Birds Sing")

lion=animal()
lion.sound()

alex=dog()
alex.sound()

cheeki=bird()
cheeki.sound()
