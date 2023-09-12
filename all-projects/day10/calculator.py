def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2            

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
for key in operations:
    print(f"{key}")
operation = input("enter the operation that you want to perform \n")
op_function = operations[operation]
answer = op_function(num1,num2)
print(answer)
opt = (input("do you want to continue? Y/N"))
while opt == "y":
    operation = input("enter the operation that you want to perform \n")
    newnum = int(input("enter a number"))
    op_function = operations[operation]
    answer1 = op_function(answer,newnum)
    print(answer1)
    opt = (input("do you want to continue? Y/N"))

