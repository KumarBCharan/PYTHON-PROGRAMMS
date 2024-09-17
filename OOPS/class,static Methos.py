class Bank:
    bank_name="SBI"
    bank_ifsc=1245
    bank_roi=6
    bank_address="kizikistan"
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    @classmethod
    def bank_details(cls):
        print(cls)
        print(f"Name of the bank is: {cls.bank_name}")
        print(f"Ifsc of the bank is: {cls.bank_ifsc}")
        print(f"Roi of the bank is: {cls.bank_roi}")
        print(f"Addres of the bank is: {cls.bank_address}")
    def customer_details(self):
        print(f"name os the customer is {self.name}")
        print(f"account os the customer is {self.account}")
        print(f"balance os the customer is {self.balance}")
        print(f"address os the customer is {self.address}")
    @classmethod
    def modify_roi(cls):
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print("modified roi is:",cls.bank_roi)
    @staticmethod
    def get_int_value():
        intvalue=int(input("ENter int value"))
        return intvalue
    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print("withdraw successfull")
            print(f"BAlance is {self.balance}")
        else:
            print("in sufficient balance")
    def  deposite(self):
        amount=self.get_int_value()
        if amount>0:
            self.balance+=amount
                
            print("deposite successfull")
            print(f"BAlance is {self.balance}")
        else:
            print("amount should be >0")
                
charan=Bank("Charan Kumar B",123456,26000,"Bangalore")
mahesh=Bank("mahesh kumar V",297822,50000,"chennai")

#charan.withdraw()
#mahesh.withdraw()
#charan.deposite()
mahesh.deposite()
#print(mahesh.balance)
#Bank.bank_details()
#Bank.modify_roi()
#print(Bank.bank_roi)
#print(charan.bank_roi)
#print(mahesh.bank__roi)

