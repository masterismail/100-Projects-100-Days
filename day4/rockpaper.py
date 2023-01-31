import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=[['draw','loose','win'],['win','draw','win'],['loose','win','draw']]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
elif choice==2:
    print(scissors)
else:
    print("enter correct input")

cc=random.randint(0,2)

if cc==0:
    print(f"the computer choose \n{rock}")
elif cc==1:
    print(f"the computer choose: \n{paper}")
elif choice==2:
    print(f"the computer choose: \n {scissors}")

print(list[choice][cc])