#functions to get the names and ages of users
def get_age():
    age = int(input("Please enter your age \n"))
    return age

def get_name():
    name = input ("Please enter your first name \n")
    return name

print ("Hello", get_name(),",", "you are", get_age(), "years old and it's nice having you on this years Global Code")