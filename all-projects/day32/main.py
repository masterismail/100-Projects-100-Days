#monday motivation email sender


import smtplib
import os
import datetime as dt
import random
import math

my_email = "gdsc.smec@gmail.com"
password = os.environ.get('password')



now = dt.datetime.now()

day = now.weekday()

if day == 3:
    
    with open ("all-projects/day32/Birthday Wisher (Day 32) start/quotes1.txt") as quotes_file:
     all_quotes = quotes_file.readlines()
     random_quote = random.choice(all_quotes)
    
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email , password=password)
    connection.sendmail(from_addr=my_email, 
                    to_addrs="mohammedismail523261@gmail.com", 
                    msg=f"Subject:This is subject \n\n this is motivation {random_quote}")
    connection.close()



