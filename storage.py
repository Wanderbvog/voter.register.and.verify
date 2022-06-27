#Let's see how should the voters' hash stored
from vrv import *
hashlist=["hashes of registered voters"]; 
counter = 3

while counter != 0:
    vhash = voter_registry() # prompt user input
    hashlist.append(vhash)
    counter-=1 
    if counter != 0:
        print("Next please!")
    else:
        print("Server full!")

#Main programme entry point
for i in hashlist:
    print(i) #in reality they should be stored into a dataframe