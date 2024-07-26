class student:
    def __init__(self):
        self.name="Manikandan"
        self.reg_no="410621243017"

    def display(self):
        print(self.name)
        print(self.reg_no)

s1=student()
s2=student()
s2.name="Manoj"
s2.reg_no="410621243018"
print(s1.name)
print(s1.reg_no)
print(s2.name)
print(s2.reg_no)
s1.display()
s2.display()
