class laptop:
    def __init__(self):
        self.ram=""
        self.procesor=""

    def display(self):
        print("ram",self.ram)
        print("processor",self.processor)

hp=laptop()
dell=laptop()

hp.ram="12gb"
hp.processor="I5"
hp.display()  

dell.ram="12gb"
dell.processor="I5"
dell.display()  
