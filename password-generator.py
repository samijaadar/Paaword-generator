import random


#generate random lowercase letter
low1=chr(random.randint(97,122))
low2=chr(random.randint(97,122))
low3=chr(random.randint(97,122))
#generate random uppercase letter
up1=chr(random.randint(65,90))
up2=chr(random.randint(65,90))
up3=chr(random.randint(65,90))
#generate random integer letter
num1=chr(random.randint(48,57))
num2=chr(random.randint(48,57))
num3=chr(random.randint(48,57))
#generate random symboles
sym1=chr(random.randint(33,47))
sym2=chr(random.randint(33,47))
sym3=chr(random.randint(33,47))

password=low1+low2+low3+up1+up2+up3+num1+num2+num3+sym1+sym2+sym3
print(password)