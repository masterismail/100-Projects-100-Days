import art
from art import *
import gamedata
from gamedata import *
import random

def GenA():      #to generate random name
   A = random.choice(data)
   print(f"Compare A:{A['name']}, a  {A['description']}, from  {A['country']}")
   followers = A['follower_count']
   return followers
def GenB():      #to generate random name
   B = random.choice(data)
   print(f"Compare B:{B['name']}, a  {B['description']}, from  {B['country']}")
   followers = B['follower_count']
   return followers

def display():
 print(logo)
 followerA = GenA()


 print(vs)
 followerB = GenB()

 user_choice = input(int("enter a or b"))
 print(followerA)
 print(followerB)
 if user_choice == 'A' and followerA>followerB:
   GenA()
 if user_choice == 'B' and followerB>followerA:
   GenB()
 else:
   print("you lost")
   
