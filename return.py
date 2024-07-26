s_username="EMC"
s_password=123

username=str(input("Enter the Name:"))
password=int(input("Enter the password:"))

def validate():
    if( s_username==username and s_password==password ):
        return True
    else:
        return False

login=validate()
print(login)

