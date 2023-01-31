word="Ismail"
word=word.upper()
word_list=[*word]
print(word_list)
blank_list=[]
for i in word:
 blank_list.append("_")
print(blank_list) #checking the blanks are correct or not
print(word_list)  #checking the word is in list or not
for i in range(8):
 guess=input("enter your guess")
 guess=guess.upper()
 print(guess) #checking the letter
 for i in range(len(word_list)):
    if guess==word_list[i]:
     blank_list[i]=guess
     print(blank_list)
    else:
     print("chance gaya eak")   
     