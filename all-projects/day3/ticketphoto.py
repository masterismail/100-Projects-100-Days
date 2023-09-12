amount=0
free=0
height=int(input("Whats your height"))
photo=input("do you want a picture")
if height>120:
    age=int(input("whats your age?"))
    if age<55 and age>45:
        print("free hai chicha  aish karo!!.")
        free=free+1
    elif age<12:
     print("rate 5$")
     amount=amount+5
    elif age<=18 and age>=12: 
        print("rate 7$")
        amount=amount+7
    elif age>18 :
        print("rate 12$")
        amount=amount+12
    if photo=="Y" and free==1:            
     print("total amount is ",amount)
    elif photo=="Y" and free==0:
        amount=amount+3
        print(f"your to total amount is ${amount}")     
else:
    print("sorry you coudnt take the ride")        