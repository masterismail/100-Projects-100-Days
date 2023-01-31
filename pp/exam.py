# Store input numbers:  
num1 = int(input('Enter first number: '))  
num2 = int(input('Enter second number: '))  
  
# Add two numbers  
sum = float(num1) + float(num2)  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
# Subtract two numbers  
min = float(num1) - float(num2)
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Multiply two numbers  
mul = float(num1) * float(num2)
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
#Divide two numbers  
div = float(num1) / float(num2)
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  
#greaterorequal
print ("num1>num2 =",num1 >= num2)
#notEqual  
print("num1!=num2 =",num1 != num2)
#lessThanOrEqual  
print("num1<=num2 =",num1 <= num2)
#equal  
print("num1==num2 =",num1 == num2)
#greater
print("num1>num2 =",num1 > num2)
#LessThan
print("num1<num2 =",num1 < num2)  
#LogicalAND
print("true" and "true")
print("true" and "False")
#logicalOR
print("true" or "False")
#logicalNOT
print(not "true")
#BitAND
print("num1&num2=",int(num1) & int(num2))
#BitOr
print("num1/num2=",num1/num2)
#BitNot
print("~num2=",~num2)
#bitandOr
print("num1^num2=",num1^num2)