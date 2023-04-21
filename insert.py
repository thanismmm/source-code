from authentication import signin

uid = input("Enter Your User Id:",)
pword = input("Enter Your Password:",)
f = "credential.txt"
if signin(uid,pword,f) == True:
    i = 0
    while i < 1:
        id = input("Enter Your Id Number:",)
        name = input("Enter your Name:",).lower()
        age = input("Enter Your Age:",)
        location = input("Enter Your Location:",).lower()
        stoploop = input("Do You Add More Student Data (y/n):",).lower()
        print("----------------------------------------------------")
        file = open("Students.txt", "a")
        # idd = file.write(f"{id}\t{name}\t\t{age}\t\t{dob}\n")
        value = id+":"+name+":"+age+":"+location
        file.write(value+"\n")
        if stoploop == "y":
            i = 0
        else:
            i = 1
    print("Thank You!")
else:
    print("invalid user id and password!")