# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amount=0
if size=="S":
    amount=amount+15
    if add_pepperoni=="Y":
        amount=amount+2
if size=="M":
    amount=amount+20
    if add_pepperoni=="Y":
        amount=amount+3
if size=="L":
    amount=amount+25
    if add_pepperoni=="Y":
        amount=amount+3        
if extra_cheese=="Y":
    amount=amount+1
print(f"amount is ${amount}")            