class goa():
    name=""
    drink=""
    def party(self):
        print("Lets Enjoy")
    def beach(self):
        print("bechhh")

Firstperson=goa()
Secondperson=goa()

Firstperson.name="Ramesh"
Secondperson.name="Suresh"

Firstperson.drink="yes"
Secondperson.drink="No"

print(Firstperson.name)
print("Drink",Firstperson.drink)
Firstperson.party()

print(Secondperson.name)
print("Drink",Secondperson.drink)
Secondperson.beach()
