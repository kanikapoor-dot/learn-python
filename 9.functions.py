from datetime import datetime 

first_name = input("name : ")
last_name  = input("name : ")

def get_ini(name):
    return name[0].upper()

def time():
    return datetime.now()

print(get_ini(name=first_name) + get_ini(name=last_name) +" " + str(time()))
 