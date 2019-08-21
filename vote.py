#The python program to identify who is allowed to vote in my family

voters=['denis','aaron','chuga','cap','meshack','juma','petro'] #This is the list of my family members
qvoter=[]#The new list which later append the 
for voter in voters:
    print("Hello "+voter.upper()+" welcome")
    insert_age=input("How old are you?: ")

    print("Your age is "+insert_age+" Years old")
    age=int(insert_age)


    if age > 17:
       print("YOU ARE ALLOWED  TO VOTE")
       answer=input("DO YOU HAVE AN IDENTITY CARD?: [write Y/N]: ")

       if answer=='Y':
          print("Goodlucky")

       else:
          print("Search for it Immediately before 15th october 2019")

       qvoter.append(voter)

    else:
       print("YOU ARE NOT ALLOWED TO VOTE:")
    response=input("Do you allow me to ask others? : [write y/n] : ")

    if response=='y':
       print("Thank you "+voter.lower()+" ")
    else:
        break
    print()

print("*****Thank you all for your participation***** \n")
print("The following below are allowed to vote: ")

for voter in qvoter:
    print(voter.upper())
