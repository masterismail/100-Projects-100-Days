# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("all-projects/day30/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def takes_input():
  
 word = input("Enter a word: ").upper()
 try:
   output_list = [phonetic_dict[letter] for letter in word]
 except:
  print("Sorry, only letters in the alphabet please.")
  takes_input()
 else:
  output_list = [phonetic_dict[letter] for letter in word]
  print(output_list)
   

takes_input()