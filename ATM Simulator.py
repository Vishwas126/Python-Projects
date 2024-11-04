accounts = {
    112233 : [1234,"Vishwas",10000,"9876543210"],
    445566 : [6789,"Jash",50000,"9123456789"],
    778899 : [2408,"Mahi",70000,"7963852741"]
    }
while True:
    print("ATM MEnu")
    print("Choose The required Options: ")
    print("1. Check Balanace ")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Pin Change ")
    print("5. Pin Generation ")
    print("6. Exit ")
    option = int(input("Choose Option: "))
    if option == 1:
        accno = int(input("Enter your Account Number: "))
        if accno not in accounts:
            print("Data Does not Exists !. Try again ")
        else:
            pin = int(input("Enter Your Pin : "))
            if pin != accounts[accno][0]:
                print(" Wrong Pin Entered. Try again ")
            else:
                print(f"Balance : {accounts[accno][2]}")
    elif option == 2:
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Data Does not Exists !. Try again ")
        else:
            money = int(input("Enter Money to Deposit: "))
            accounts[accno][2] += money
            print("Money Added to your Account Sucessfully !")
    elif option == 3:
        accno = int(input("Enter your Account number: "))
        if accno not in accounts:
            print("Data does not Exists !. Try again ")
        else:
            pin = int(input("Enter Your Pin :"))
            if pin != accounts[accno][0]:
                print("Wrong Pin entered !")
            else:
                wmoney = int(input("Enter amount to Withdraw: "))
                balance = accounts[accno][2]
                if wmoney > balance:
                    print("Insufficient Funds !.. Try again ")
                else:
                    print("Collect Your Cash ")
                    accounts[accno][2] -= wmoney
    elif option == 4:
        accno = int(input("Enter Your Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists!.. Try again")
        else:
            mobile = input("Enter your Mobile Number: ")
            if accounts[accno][3] != mobile:
                print("Check your mobile number and perform action Later !")
            else:
                pin = int(input("Enter Current Pin : "))
                if pin != accounts[accno][0]:
                    print("Wrong Pin entered !.. Try again ")
                else:
                    npin = int(input("Enter Your New Pin: "))
                    cpin = int(input("Re enter your new pin : "))
                    if npin != cpin:
                        print("Pin not Entered correctly !.. Try again")
                    else:
                        accounts[accno][0] = npin
                        print("Pin Reset Sucessfull ")
    elif option == 5:
        print("Welcome !....")
        accno = int(input("Enter Account number: "))
        if accno in accounts:
            print("Account Number already Exists !.. Try again ")
        else:
            name = input("Enter Your Name: ")
            mobile = input("Enter Your Mobile Number: ")
            pin = int(input("Enter New Pin: "))
            cpin = int(input("Re Enter pin: "))
            if pin != cpin:
                print("Pin Generation Unsucessfull !")
            else:
                accounts[accno] = [pin,name,0,mobile]
                print("Pin Generated Sucessfully !..")
    else:
        print("Thanks for choosing ATM ")
        break


