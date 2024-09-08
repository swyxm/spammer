#Created on Sun May 16 2020

import smtplib
from getpass import getpass
import random

while True:
    senderEmail = input("Enter your gmail address in its entirety.")     
    if "@gmail.com" in senderEmail:   
        recipientEmail = input("Enter the recipient's gmail address in its entirety.")
        if "@gmail.com" in recipientEmail:
            password = input('Please enter your email password (not stored):  ')
            getpass(password)
            message = input("What would you like to say? Type enter when done: ")
    else:
        continue
    
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, password)
    print ('Sent!')
    server.sendmail(senderEmail, recipientEmail, message)

