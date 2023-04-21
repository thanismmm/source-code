i = 0
while i < 1:
    use = input("Enter Your Name:",).lower()
    pas = input("Enter Your Password:",).lower()
    con_pas = input("Re Enter The Password:",).lower()
    file = open("credential.txt", "a")
    read = open("credential.txt", "r")

    if pas == con_pas:
        for r in read:
            user = r.strip().split(":")
        pa = use + ":" + pas
        file.write(pa+"\n")
        print("Your Account Successfully Created!")
        print("Ur UserName Is: ",use)
        i = 1
        break
    else:
        print("Password Dosn't Match!")
        print("Please Retry The Password!")
        print("------------------------------")
