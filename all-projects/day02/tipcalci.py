print("Welcome to the tip calculator")
bill=float(input("What was the total bill? \n"))
percent=float(input("What percentage tip would you like to give? 10,12 or 15? \n"))
people=float(input("how many people to split the bill? \n"))
tip=(percent*bill)/100
total_bill = bill+tip
each_person = float(total_bill/people)

print("Each person should pay :",round(each_person,2))


