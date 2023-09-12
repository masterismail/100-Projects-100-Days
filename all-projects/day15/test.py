from menu import resources , MENU 

def display_prompt(): #To display the MENU
  print("What would you like  \n 1.Espresso  \n 2.Latte \n 3.Cappuccino")

def check_espresso_resources(): #To check the availibility of  Espresso resources
  sum=0
  check = {"coffee":0,"water":0}
  if resources['water'] >= MENU['cappuccino']['ingredients']['water'] :
    check["coffee"]=1
  if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] :
    check["water"]=1
  for i in check:
    if check[i] == 1:
      continue
    else:
      print(f"{i} is not available")
  for values in check.values():
    sum=sum+values
    if sum==2:
     process_coins()

def check_latte_resources(): #To check the availibility of  Latte resources
    sum=0
    check = {"coffee":0,"milk":0,"water":0}
    if resources['water'] >= MENU['latte']['ingredients']['water'] :
      check["coffee"]=1
    if resources['milk'] >= MENU['latte']['ingredients']['milk'] :
      check["milk"]=1
    if resources['coffee'] >= MENU['latte']['ingredients']['coffee'] :
      check["water"]=1
    for i in check:
     if check[i] == 1:
      continue
     else:
      print(f"{i} is not available")
    for values in check.values():
     sum=sum+values
    if sum==3:
     process_coins()
def check_capppuccino_resources(): #To check the availibility of  cappuccino resources
    sum=0
    check = {"coffee":0,"milk":0,"water":0}
    if resources['water'] >= MENU['cappuccino']['ingredients']['water'] :
      check["coffee"]=1
    if resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] :
      check["milk"]=1
    if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] :
      check["water"]=1
    for i in check:
     if check[i] == 1:
      continue
     else:
      print(f"{i} is not available")
    for values in check.values():
     sum=sum+values
    if sum==3:
     process_coins()

def process_coins():
  print("please enter coins")
  total_cash = 0
  rupee_10 = int(input("how many 10 rupee note"))
  rupee_20 = int(input("how many 20 rupee note"))
  rupee_50 = int(input("how many 50 rupee note"))
  rupee_100 = int(input("how many 100 rupee note"))
  rupee_200 = int(input("how many 200 rupee note"))
  total_cash = (rupee_10*10)+ (rupee_100*100) + (rupee_20*20) + (rupee_50*50) + (rupee_200*200)
  if user_input == "espresso":
    
    if total_cash >=MENU['espresso']['cost']:
      return_cash = total_cash - MENU['espresso']['cost']
      print(f"your return cash is {return_cash}")
      resources['money']=resources['money']+MENU['espresso']['cost']
      make_coffee()
    else:
      print("not enough money")  
  elif user_input == "latte":
    if total_cash >=MENU['latte']['cost']:
      return_cash = total_cash - MENU['latte']['cost']
      print(f"your return cash is {return_cash}")
      resources['money']=resources['money']+MENU['latte']['cost']
      make_coffee()
    else:
      print("not enough money")
  elif user_input == "cappuccino":
    if total_cash >=MENU['cappuccino']['cost']:
      return_cash = total_cash - MENU['cappuccino']['cost']
      print(f"your return cash is {return_cash}")
      resources['money']=resources['money']+MENU['cappuccino']['cost']
      make_coffee()

    else:
      print("not enough money")        
def make_coffee():
  if user_input == "espresso":
    resources['water']=resources['water']-MENU['espresso']['ingredients']['water']
    resources['coffee']=resources['coffee']-MENU['espresso']['ingredients']['coffee']
    print("your espresso is ready")
  elif user_input == "latte":
    resources['water']=resources['water']-MENU['latte']['ingredients']['water']
    resources['coffee']=resources['coffee']-MENU['latte']['ingredients']['coffee']
    resources['milk']=resources['milk']-MENU['latte']['ingredients']['milk']
    print("your latte is ready")
  elif user_input == "cappuccino":
    resources['water']=resources['water']-MENU['cappuccino']['ingredients']['water']
    resources['coffee']=resources['coffee']-MENU['cappuccino']['ingredients']['coffee']
    resources['milk']=resources['milk']-MENU['cappuccino']['ingredients']['milk']
    print("your cappuccino is ready")  
display_prompt()
user_input = input("")
if user_input == "off":
  print("end execution")
elif user_input == "report" :
  for i in resources:
   print(f"{i} :{resources[i]} ")
elif user_input == "espresso" :
  check_espresso_resources()
 
elif user_input == "latte" :
  check_latte_resources()
 
elif user_input == "cappuccino" :
  check_capppuccino_resources()
  
