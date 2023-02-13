main_list=[]
highestbid=0
bidder=""
man_bid=""
def ask():
 name=input("What is your name ?")
 bid=input("What's your bid ?")
 main_list.append({"name":name,"bid":bid})
 other=input("Are there any other bidders ? Type 'yes' or 'no'")
 if other=="yes":
  ask()
len=int(len(main_list))
for i in range(len):
  bid=(main_list[i]["bid"])
  if int(bid)>int(highestbid):
    highestbid=bid  
    man_bid=main_list[i]["name"]
ask()
print(f"highest bid is{highestbid} and bidder is {man_bid}")

        

