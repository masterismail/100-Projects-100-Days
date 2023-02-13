student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#TODO-1: Create an empty dictionary called student_grades.
student_grades={}


#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
  score=student_scores[i]
  if score >=91 and score  <= 100: 
    Grade = "Outstanding"
    student_grades[i]=Grade
  elif score >=81 and score  <= 90: 
    Grade = "Exceeds Expectations"
    student_grades[i]=Grade
  elif score >=71 and score  <= 80: 
    Grade = "Acceptable"
    student_grades[i]=Grade
  elif score <=70 : 
    Grade = "Fail"
    student_grades[i]=Grade
    

# 🚨 Don't change the code below 👇
print(student_grades)