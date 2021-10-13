ch=str(input("\"Do you want to recharge?\n y-Yes and any for No"))
if ch=='Y'.casefold():
    opt=int(input("Press 1 for prepaid and any key for postpaid"))
if opt==1:
    no=int(input("Enter mobile no"))
operator=int(input("Choose your operator\n1. Jio \n2. Airtel\n3.Vi\n"))
amt=int(input("Choose a recharge amt\n100 : 1.5 GB data/day for 84 days\n 399 : 1 GB data"))
confirm=int(input("Press 1 to confirm and any key to cancel"))
if confirm==1:
    print("Your recharge for no {} for amt {} has been succesfull!".format(no,amt))