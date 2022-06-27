#Voting Registry as a proof of concept
import datetime
import hashlib
def voter_registry(): 
    print ("Name on your ID card")
    name = input()

    id_no = input("Your ID no., bracket included:")
    #if id_no != registered ID no. in exist data base (which in exile gov setting should be anonomyously stored)
       #print("Verification fail. Perhaps you are not our citizens")
        #exit()

    print("M or F")
    gender = input().upper()
    checkGender=False
    counter=5
    while not checkGender:#Should have a counter here to prevent abuse
        if gender != "M" and gender != "F":
            print("Try again, please enter M if you are male, and F if female")
            counter-=1
            gender = input().upper()
            if counter==0:
                print("Please go away, you troll!")
                exit()
        else: 
            checkGender=True


    today = datetime.datetime.now()
    print("Year of birth")
    year=int(input())
    print("Month of birth")
    month=int(input())
    print("Birth day")
    day=int(input())
    birthday = str(datetime.datetime(year, month, day))
    age = today.year - year - ((today.month, today.day) < (month, day))
    if age <18 :
        print("Our dear little future citizen, you are yet to reach the voting age, thanks but sorry") #Minimum voting age is 18 years old
        exit()
    else:
        phone_no = input("Enter your phone no.")
        #There should be a SMS verification function, that if verification code input != code sent, then exit
        #The code of SMS verification come from here: https://developer.telesign.com/enterprise/docs/sms-api-tutorial-send-an-sms-with-a-verification-code
    #from __future__ import print_function
    #from telesign.messaging import MessagingClient
    #from telesign.util import random_with_n_digits

    #customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    #api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

    #phone_number = phone_no
    #message_type = "OTP"

        #verify_code = random_with_n_digits(5)
        #message = "Your code is {}".format(verify_code)

        #messaging = MessagingClient(customer_id, api_key, rest_endpoint="https://rest-ww.telesign.com")
        #response = messaging.message(phone_number, message, message_type)

        #user_entered_verify_code = raw_input("Please enter the verification code you were sent: ")

    #if verify_code == user_entered_verify_code.strip():
        #print("Your code is correct.")
    #Should have also a open-question to answer as to make it hard to spoof(e.g. What is your favorite food?)
        string = name+id_no+gender+birthday+phone_no
    voter=hashlib.sha512(string.encode()).hexdigest()
    return voter 
    #else:
        #print("Your code is incorrect.")
        #exit()
VotR = "66b1c8cf3a116b1315949c8229a7caef012d8cf411358daaa37aff4963aa24deba94d6a0ab2554f19250fc6c8da395ef4229be21b0a6da92fa3d0f379277b222"
#"VotR" is the hash generated from the use case as a demo to allow the function to run, which is supposed to be stored separatedly from the verification system
#In reality, should be a request to the registry server to find the registered matching hash.
#Use case here:
#Name: Pak Shun Hang Tyndale
        #ID_no: C198964(3)
        #Sex: M 
        #Birthdate: 2001-02-24
        #Phone: 69612831
def voter_verify():
    VerifyHash = voter_registry()
    if VerifyHash != VotR: #In reality, a request for matching hash should be sent to the registration database
        print("Verification fail")
        exit()
    else: 
        print("Verification success!")
        #Proceed to Voting page/Weighting registry
#Main Entry
#For Voting registration:
#voter_registry()
#For voter verification:
#voter_verify()
