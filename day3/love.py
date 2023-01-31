
name1=input("write first name")
name2=input("write second name")
tc=0
lc=0
name3=name1+name2
name3=name3.upper()
for i in range(len(name3)):
  if name3[i]=="T":
    tc=tc+1
  elif name3[i]=="R":
    tc=tc+1   
  elif name3[i]=="U":
    tc=tc+1
  elif name3[i]=="E":
    tc=tc+1 
for j in range(len(name3)):    
  if name3[j]=="L":
    lc=lc+1    
  elif name3[j]=="O":
    lc=lc+1
  elif name3[j]=="V":
    lc=lc+1
  elif name3[j]=="E":
    lc=lc+1          
finalcount=tc*10+lc
if finalcount<10 and finalcount>90:
    print(f"fYour score is **{finalcount}**, you go together like coke and mentos.")
if finalcount>40 and finalcount<50:
    print(f"Your score is **{finalcount}**, you are alright together.")
else:
    print(f"Your score is **{finalcount}**.")        