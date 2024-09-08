#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:00:51 2020

@author: swayam
"""
#Simple email bot I developed (Can send up to 500 emails within 1 minute before being timed out)
#Sadly won't work anymore and it's out of my control, Google removed the third-party access from modules feature for account security
#To help keep your account secure, from May 30, 2022, ​​Google no longer supports the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password.

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

