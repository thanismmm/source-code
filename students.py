from authentication import signin
i = 0
while i < 1:
    uid = input("Enter Your User Id:",)
    pwod = input("Enter Your Password:",)
    f = "credential.txt"
    namelist = open("Students.txt", "r")
    age = []
    if signin(uid,pwod,f) == True:
        print("Welcome Back Mr."+uid)
        bolt_undli = '\x1B[1;4m'
        bolt_undli_close = '\x1B[0m'
        print(bolt_undli + "student id" + bolt_undli_close + "\t",
              bolt_undli + "student Name" + bolt_undli_close + "\t",
              bolt_undli + "student Age" + bolt_undli_close + "\t",
              bolt_undli + "student Location" + bolt_undli_close + "\t", "\n")
        for name in namelist:
            va = name.strip().split(":")
            age.append(int(va[2]))
            print(va[0] + "\t\t " + va[1] + "\t\t\t " + va[2] + "\t\t\t\t " + va[3])
        print("\n" + '\x1B[1m' + "No. of Students:" + '\x1B[0m', "\t\t\t", len(age))
        print('\x1B[1m' + "Lowest Age Of Students:" + '\x1B[0m', "\t", min(age))
        print('\x1B[1m' + "Highest Age Of Students:" + '\x1B[0m', "\t", max(age))
        i = 1
        break
    else:
        print("Invalid User Id & Password")
        print("Re enter User id & Password Correctly ")
        print("----------------------------------------")

