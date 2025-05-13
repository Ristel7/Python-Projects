print("State Bank of India")
print("1 - Balance Enquiry")
print("2 - Cash Withdrawal")
print("3 - Cash Deposit")
print("4 - Mini Statement")
options = input("Enter your choice: ")
li = ["Balance Enquiry", "Cash Withdrawal", "Cash Deposit", "Mini Statement"]
if options in li:
    if options == "Balance Enquiry":
        print("Your balance is: 10000")
    elif options == "Cash Withdrawal":
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= 10000:
            print("Please collect your cash")
        else:
            print("Insufficient balance")
    elif options == "Cash Deposit":

        amount = int(input("Enter amount to deposit: "))
        print("Your new balance is: ", 10000 + amount)
    elif options == "Mini Statement":
        print("Last 5 transactions are: ")
        print("1. Cash Deposit - 5000")
        print("2. Cash Withdrawal - 2000")
        print("3. Cash Deposit - 3000")
        print("4. Cash Withdrawal - 1000")
        print("5. Cash Deposit - 2000")
else:
    print("Invalid choice")
