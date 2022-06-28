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
        print("In one word, told us your favorite food.") #Actually can be any other questions, and should be updated frequently to make the secret more diverse, and can be added more questions to enhance security.
        secret = input().upper()
        string = name+id_no+gender+birthday+secret
    voter=hashlib.sha512(string.encode()).hexdigest()
    return voter 
  
VotR = "66b1c8cf3a116b1315949c8229a7caef012d8cf411358daaa37aff4963aa24deba94d6a0ab2554f19250fc6c8da395ef4229be21b0a6da92fa3d0f379277b222"
#"VotR" is the hash generated from the use case as a demo to allow the function to run, which is supposed to be stored separatedly from the verification system
#In reality, should be a request to the registry server to find the registered matching hash.
#Use case here:
#Name: Pak Shun Hang Tyndale
        #ID_no: C198964(3)
        #Sex: M 
        #Birthdate: 2001-02-24
        #secret: 69612831 (Originally "phone_no., just keep the value unchange to maintain the same hash)
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
