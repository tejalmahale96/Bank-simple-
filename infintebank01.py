balance=1000.00
while True:
    print("1 for withdrow\n2 for Deposite\n3 for Exit")
    c=int(input("Enter your choice => "))
    if c==1:
        amt=float(input("Enter amount for Withdrow => "))
        if amt > balance or balance <= 1000:
            print("Not enough fund")
        else:
            balance-=amt
        print("your current balance is {}".format(balance))
    elif c==2:
        amt=float(input("Enter amount for Deposite => "))
        balance+=amt
        print("your current balance is {}".format(balance))
    elif c==3:
        print("Invalid choice")
    ch=input("Do you want to perform more transactions (y/n) => ")
    if ch=='Y' or ch=='y':
        continue
    else:
        break
                  
