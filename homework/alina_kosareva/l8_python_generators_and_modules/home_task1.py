import random

salary = int(input("Please,input your salary: "))
bonus = random.choice([True,False])

if bonus:
  general_salary = salary + int(random.random() * 100)
  print(f"{salary}, {bonus} = '${general_salary}'")

else :
  print(f"{salary}, {bonus} - '${salary}'")
