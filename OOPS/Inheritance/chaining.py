class Bank_v1:
    bank_name="SBI"
    bank_ifsc=1245
    bank_roi=6
    bank_address="kizikistan"

    def __init__(self,n,a,b,ad):
        self.Cname=n
        self.Caccount=a
        self.Cbalance=b
        self.Caddress=ad

    def customer_details(self):
        print(f"name of the customer is {self.Cname}")
        print(f"account of the customer is {self.Caccount}")
        print(f"balance of the customer is {self.Cbalance}")
        print(f"address of the customer is {self.Caddress}")

class Bank_v2:

    bank_address="Bglr"

    def __init__(self,n,a,b,ad,p):
        Bank_v1.__init__(self,n,a,b,ad)
        self.Cpin=p

    def customer_details(self):

        Bank_v1.customer_details(self)
        print(f"pin code of the customer is {self.Cpin}")
    
charan=Bank_v2("charan kumar B",25489,25000,"BAngalore","AMMU@143")
charan.customer_details()
