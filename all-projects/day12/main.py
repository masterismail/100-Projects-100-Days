import random
chance=0
number = random.randint(1,100)
print(number)
level=input("Select the level of difficulty \n 1 \n 2 \n 3 \n")
if level == "1":
    chance=chance+10
    print(chance)
elif level == "2":
    chance=chance+5
elif level=="3":
    chance=chance+3
while(chance>0):
 guess = int(input("guess the number"))
 if guess>number:
   print("too high")
   chance=chance-1
 elif guess<number:
    print("too low")
    chance=chance-1
 elif guess==number:
    print("you won")
    break

