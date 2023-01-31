word_list=['i','s','m','a','i','l']
blank_list=['.','.','.','.','.']
word="ismail"
guess=input("enter")
for i in range(len(word)):
  if guess==word_list[i]:
    blank_list[i].replace(guess)
  else:
    print("chance gaya eak")   
