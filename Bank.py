print("------------------- Bank Managment system ---------------------")
class Account:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            self.history.append(f"deposited {amount}")
            print("Deposited Successful!")                                    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount")
        else:
            self.balance -= amount
            self.history.append(f"withdraw {amount}")
            print("Withdrawal Successful!")                                     
                                                                                 
    def check_balance(self):
        print("Your current balance =", self.balance)


    def show_details(self):
        print("Name =", self.name)
        print("Account Number =", self.acc_no)
        print("Balance =", self.balance)


    def show_history(self):
        print("\nTransection History:")
        for transection in self.history:
            print(transection)
            
    def save_account():
        with open("account.txt", "a") as file:
            file.write(f"Name : {self.name}, Acc_no : {self.acc_no}, Balance : {self.balance}\n")


acc1 = Account("ismail", "21232", 0)

while True:
    print("===========\n Bank Menu\n===========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Show details")
    print("5. Transection history")
    print("6. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:
        amount = int(input("Enter your amount: "))
        acc1.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter your amount:"))
        acc1.withdraw(amount)

    elif choice == 3:
        acc1.check_balance()

    elif choice == 4:
        acc1.show_details()

    elif choice == 5:
        acc1.show_history()

    elif choice == 6:
        print("Thanks for using the bank")
        break

    else:
        print("Invalid choice")