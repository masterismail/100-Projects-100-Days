
def ask():
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))
 if direction=="encode":
#function to encrypt the give text
  def encrypt(text,shift):
   cipher_text=[]    
   for i in range(len(text)):
     new_asci=ord(text[i])
     print_asci=new_asci+shift
     if print_asci>122:
      print_asci=print_asci-122+97-1
      cipher_text.append(chr(print_asci))
     else:
      cipher_text.append(chr(print_asci))
   print(*cipher_text,sep='')   
#calling of the function to encrypt 
  encrypt(text,shift)
  opt=input("do you want to continue")
  if opt=="yes":
    ask()
  elif opt=="no":
    breakpoint
  else:
    print("enter correct option")    
 elif direction=="decode":
#DECRYPT
 #function to encrypt the give text
  def decrypt(text,shift):
   cipher_text=[]    
   for i in range(len(text)):
     new_asci=ord(text[i])
     print_asci=new_asci-shift
     if print_asci<97:
      print_asci=122-(97-print_asci)+1
      cipher_text.append(chr(print_asci))
     else:
      cipher_text.append(chr(print_asci))
   print(*cipher_text,sep='')   
#calling of the function to dencrypt 
  decrypt(text,shift)
  opt=input("do you want to continue")
  if opt=="yes":
    ask()
  elif opt=="no":
    breakpoint
  else:
    print("enter correct option")
 else:
  print("enter correct option")
ask()    
