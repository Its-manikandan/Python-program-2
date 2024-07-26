class teacher:
    def __init__(self,name,reg_no):
        self.name=name
        self.reg_no=reg_no

#parameter name ,reg_no kuduthutu keela
        #self.name=name
        #self.reg_no=reg_no  dhan kudukanum
        

    def display(self):
        print(self.name)
        print(self.reg_no)

#inga dhan value assign pannanum        
#                 |
#                 |
#                 |
t1=teacher("Malli",11)
t1.display()
t2=teacher("valli",12)
t2.display()
