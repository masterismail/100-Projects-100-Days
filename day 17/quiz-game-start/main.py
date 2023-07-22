question_bank = []
from data import question_data
from question_model import question

for i in range(8):
  q=question(question_data[i]['text'],question_data[i]['answer'])
  question_bank.append(q)

print(question_bank)



