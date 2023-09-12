import art
from art import *
import gamedata
from gamedata import *
import random
game = True
num_A = random.randint(0,len(data)-1)
num_B = random.randint(0,len(data)-1)
A = data[num_A]
B = data[num_B]

def checksame():      #to generate random name
    if A == B:
     checksame()

def display():
 print(logo)
 print(f"Compare A:{A['name']}, a  {A['description']}, from  {A['country']}")
 print(vs)
 print(f"Compare B:{B['name']}, a  {B['description']}, from  {B['country']}")
 print(A['follower_count'])
 print(B['follower_count'])


def compute():
 user_choice = input("enter \n")
 if user_choice == 'A' and A['follower_count'] > B['follower_count']:
    num_A = random.randint(0,len(data)-1)
    A = data[num_A]
    display()

   elif user_choice == 'B' and B['follower_count'] > A['follower_count']:
    num_B = random.randint(0,len(data)-1)
    B = data[num_B]
    display()

   else:
    print("you lost")


display()
compute()


