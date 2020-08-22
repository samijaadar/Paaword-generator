import random

x=0
password=""
while(x!=4):
    # generate random lowercase letter
    low1 = chr(random.randint(97, 122))

    # generate random uppercase letter
    up1 = chr(random.randint(65, 90))

    # generate random integer letter
    num1 = chr(random.randint(48, 57))

    # generate random symboles
    sym1 = chr(random.randint(33, 47))
    password=password+low1+up1+num1+sym1
    x=x+1


print(password)
