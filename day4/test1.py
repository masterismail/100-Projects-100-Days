import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num=random.randint(0,len(names))
print(names)
print(f"the person who pays the bill is {names[num]}")


