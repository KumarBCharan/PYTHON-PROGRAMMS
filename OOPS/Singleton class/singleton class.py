def singleton(args):
    d={}
    def inner():
        if args not in d:
            d[args]=args()

        return d[args]
    return inner
@singleton
class Varadharaja:
    def __init__(self):
        self.tickets=500

    def booking(self,n):
        if self.tickets>=n:
            self.tickets-=n
            print("Tickets Bokked successfully")
            print(f"Available tickets are {self.tickets}")
        else:
            print("SRy sir we can not book that many tickets")
            print(f"Available tickets are {self.tickets}")
charan=Varadharaja()
charan.booking(250)
charan.booking(150)
vishnu=Varadharaja()
vishnu.booking(200)

