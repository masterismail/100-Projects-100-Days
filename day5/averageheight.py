# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum=0
for i in student_heights:
    sum=sum+i
total=int(len(student_heights))
average=sum/total
print(round(average))
#Write your code below this row 👇




