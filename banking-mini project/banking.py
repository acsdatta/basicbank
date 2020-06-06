#create banking system (savings a/c, existing a/c, withdrawl, deposit, display avialablebalance , exit)
from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass = ABCMeta):
    @abstractmethod
    def createaccount():
        return 0
    
    @abstractmethod
    def authentication():
        return 0
    
    @abstractmethod
    def deposit():
        return 0
    
    @abstractmethod
    def withdrawl():
        return 0

    @abstractmethod
    def displaybalance():
        return 0

class Savinsaccount(Account):
    def __init__(self):
        self.accountdetails = {}
        
    def createaccount(self, name, initialdeposit):
        self.accountnumber = randint(10000, 99999)
        self.accountdetails[self.accountnumber] = [name, initialdeposit]
        print("Account is created, Your Account Number is : ",self.accountnumber)

    def authentication(self, name, accountnumber):
        if accountnumber in self.accountdetails.keys():
            if self.accountdetails[self.accountnumber][0] == name:
                print("Authenticated Successfully")
                self.accountnumber = accountnumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False
                
        
    def deposit(self, depositamt):
        self.accountdetails[self.accountnumber][1] += depositamt
        self.displaybalance()

        
    def withdrawl(self, withdrawlamt):
        if withdrawlamt > self.accountdetails[self.accountnumber][1]:
            print("Insuficient balance")
        else:
            self.accountdetails[self.accountnumber][1] -= withdrawlamt
            self.displaybalance()

        
    def displaybalance(self):
        self.accountdetails[self.accountnumber][1]
        print("Avilable balance : ", self.accountdetails[self.accountnumber][1])
        
        pass
savingsaccount = Savinsaccount()
while True:
    print("Enter choice 1 for create account : ")
    print("Enter choice 2 for existing account : ")
    print("Enter choice 3 exit : ")
    choice = int(input())
    if choice is 1 :
        print("Enter Name : ")
        name = input()
        print("Enter Amount for initialdeposit : ")
        initialdeposit = int(input())
        savingsaccount.createaccount(name, initialdeposit)
    elif choice is 2:
        print("Enter name : ")
        name = input()
        print("Enter Account number : ")
        accountnumber = int(input())
        authenticationdetails = savingsaccount.authentication(name, accountnumber)
        if authenticationdetails is True:
            while True:
                print("Enter choice 1 to withdrawal amount : ")
                print("Enter choice 2 to Deposit amount : ")
                print("Enter choice 3 to Available balance : ")
                print("Enter choice 4 to go back : ")
                choice = int(input())
                if choice is 1:
                    print("Enter Withdrawal amount: ")
                    withdrawlamt = int(input())
                    savingsaccount.withdrawl(withdrawlamt)
                elif choice is 2:
                    print("Enter Deposit amount : ")
                    depositamt = int(input())
                    savingsaccount.deposit(depositamt)
                elif choice is 3:
                    savingsaccount.displaybalance()
                elif choice is 4:
                    break
        else:
            exit()
    elif choice is 3:
        print("THANKYOU FOR BANKING")
        exit()

                    
