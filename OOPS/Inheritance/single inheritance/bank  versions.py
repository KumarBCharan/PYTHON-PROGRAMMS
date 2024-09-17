class Bank_v1():
    bank_name="SBI"
    bank_ifsc=1245
    bank_roi=6
    bank_address="kizikistan"

    def __init__(self,n,a,b,ad):
        self.cname=n
        self.caccount=a
        self.cbalance=b
        self.caddress=ad
        
    def customer_details(self):
        print(f"name of the customer is {self.cname}")
        print(f"account of the customer is {self.caccount}")
        print(f"balance of the customer is {self.cbalance}")
        print(f"address of the customer is {self.caddress}")

    @staticmethod
    def get_int_value():
        intvalue=int(input("enter Int value"))
        return intvalue

    def withdraw(self):
        amount=self.get_int_value()
        if self.cbalance>amount:
            self.cbalance-=amount
            print("with draw successfull")
            print(f"Balance is {self.cbalance}")
        else:
            print("insufficient balance")
    def deposite(self):
        amount=self.get_int_value()
        if amount>0:
            print("deposite success")
            print(f"Balace is {self.cbalance}")
        else:
            print("Amount should be greater then one re")
    
#charan=Bank_v1("charan kumar B",142628,2500,"BAngalore")
#charan.withdraw()
class Bank_v2(Bank_v1):
    bank_address="Bangalore"
    bank_mobile=9346096771

    @classmethod
    def bank_details(cls):
        print(f"name of the bank is {cls.bank_name}")
        print(f"ifsc of the bank is {cls.bank_ifsc}")
        print(f"roi the bank is {cls.bank_roi}")
        print(f"address of the bank is {cls.bank_address}")
    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print("changed roi")

charan=Bank_v2("charan kumar B",2726,10000,"bglr")
charan.bank_details()
charan.change_roi()
charan.customer_details()        
charan.withdraw()
        
    
