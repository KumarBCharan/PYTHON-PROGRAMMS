

class Team:
    
    def __init__(self,gn,tn,c):
        self.Gname=gn
        self.Tname=tn     
        self.Tcoach=c

        
        
        
    def display_details(self):
        print(f"Name of the game is {self.Gname}")
        print(f"name of the team is {self.Tname}")
        print(f"coach of the team is {self.Tcoach}")
        print(f"the details of the player is")
       
        
a=Team("CRICKET","RCB","Andy Flower")



class Players:
    
    def __init__(self,n,jn,a,ad,p):
        self.Pname=n
        self.PjersyNumber=jn
        self.Page=a
        self.Paddress=ad
        self.tplayers=p
        
    def player_details(self):
        self.tplayers.display_details()
        print(f"name of the player is : {self.Pname}")
        print(f"Player JersyNumber of the player is : {self.PjersyNumber}")
        print(f"Page of the player is : {self.Page}")
        print(f"Paddress of the player is : {self.Paddress}")
        print("\n")
        
player1=Players("Rohit Sharma",45,36,"Mumbai",a)
player2=Players("Virat Kohli",18,35,"Bangalore",a)
player3=Players("Dhoni",7,41,"Chennai",a)
player1.player_details()
player2.player_details()
player3.player_details()
