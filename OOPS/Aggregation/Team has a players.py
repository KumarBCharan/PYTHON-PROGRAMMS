class Player:
    def __init__(self,n,a,j,m,w,r):
        self.Pname=n
        self.Page=a
        self.Pjersynum=j
        self.Pmatches=m
        self.Pwickets=w
        self.Pruns=r
    def disply_details(self):
        print(f"Name of the player is {self.Pname}")
        print(f"age of the player is {self.Page}")
        print(f"Jersy NUmber of the player is {self.Pjersynum}")
        print(f"Matches of the player is {self.Pmatches}")
        print(f"Wickets of the player is {self.Pwickets}")
        print(f"Runs  of the player is {self.Pruns}")
class Team:
    def __init__(self,n):
        self.nop=n
        self.pl=[]
        for i in range(self.nop):
            n=input("enter player name")
            a=int(input("eneter player age"))
            j=int(input("enter player nersy number"))
            m=int(input("enter no of matches of the player"))
            w=int(input("Enter the no of wickets taken bplayer"))
            r=int(input("Enter the no of runs scored by player"))
            po=Player(n,a,j,m,w,r)
            self.pl.append(po)
    def highest_Matches(self):
         
        mrs=self.pl[0]
        for po in self.pl:
             if po.Pmatches>mrs.Pmatches:
                 
                mrs=po
        return mrs.Pname
    def highest_Runs(self):
        mrs=self.pl[0]
        for po in self.pl:
            if po.Pruns>mrs.Pruns:
                mrs=po
        return mrs.Pname
    def highest_wickets(self):
        mwt=self.pl[0]
        for po in self.pl:
            if po.Pwickets>mwt.Pwickets:
                mwt=po
        return mwt.Pname
    
india=Team(5)
print(india.highest_Runs())
print((india.highest_wickets()))
print(india.highest_Matches())
print(india.pl.highest_Matches())
