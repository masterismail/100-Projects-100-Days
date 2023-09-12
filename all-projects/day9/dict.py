final_dict={}
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
for i in student_scores:
  score=student_scores[i]
  if score >=91 and score  <= 100: 
    Grade = "Outstanding"
    final_dict[i]=Grade
  elif score >=81 and score  <= 90: 
    Grade = "Exceeds Expectations"
    final_dict[i]=Grade
  elif score >=71 and score  <= 80: 
    Grade = "Acceptable"
    final_dict[i]=Grade
  elif score <=70 : 
    Grade = "Fail"
    final_dict[i]=Grade
print(final_dict)  
  
