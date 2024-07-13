class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, to_account):
        if self.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account({self.account_number}, Balance: {self.balance})"


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f"Customer({self.customer_id}, Name: {self.name}, Accounts: {[str(account) for account in self.accounts]})"


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, customer_id, name):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
            return True
        return False

    def add_account(self, customer_id, account_number, balance=0):
        if customer_id in self.customers:
            account = Account(account_number, balance)
            self.customers[customer_id].add_account(account)
            self.accounts[account_number] = account
            return True
        return False

    def deposit_money(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        return False

    def withdraw_money(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return False

    def transfer_money(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            return self.accounts[from_account_number].transfer(amount, self.accounts[to_account_number])
        return False

    def list_customers(self):
        return [str(customer) for customer in self.customers.values()]


def main():
    bank = Bank()
    while True:
        print("Welcome to the eShikhon Bank PLC")
        print("1. Add Customer")
        print("2. Add Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. List Customers")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter Customer ID: "))
            name = input("Enter Customer Name: ")
            if bank.add_customer(customer_id, name):
                print("Customer added successfully.")
            else:
                print("Customer ID already exists.")

        elif choice == '2':
            customer_id = int(input("Enter Customer ID: "))
            account_number = int(input("Enter Account Number: "))
            balance = float(input("Enter Initial Balance: "))
            if bank.add_account(customer_id, account_number, balance):
                print("Account added successfully.")
            else:
                print("Customer ID does not exist.")

        elif choice == '3':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Amount to Deposit: "))
            if bank.deposit_money(account_number, amount):
                print("Money deposited successfully.")
            else:
                print("Account number does not exist.")

        elif choice == '4':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Amount to Withdraw: "))
            if bank.withdraw_money(account_number, amount):
                print("Money withdrawn successfully.")
            else:
                print("Account number does not exist or insufficient balance.")

        elif choice == '5':
            from_account_number = int(input("Enter From Account Number: "))
            to_account_number = int(input("Enter To Account Number: "))
            amount = float(input("Enter Amount to Transfer: "))
            if bank.transfer_money(from_account_number, to_account_number, amount):
                print("Money transferred successfully.")
            else:
                print("Transfer failed. Check account numbers and balance.")

        elif choice == '6':
            print("\nCustomers:")
            for customer in bank.list_customers():
                print(customer)

        elif choice == '7':
            print("Exiting the eShikhon Bank PLC. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()