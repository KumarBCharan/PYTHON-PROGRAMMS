class Desktop:
    def __init__(self,b,m,g,p):
        self.brand=b
        self.model=m
        self.generation=g
        self.processor=p

    def desktop_details(self):
        
        print(f"brand of the desktop is {self.brand}")
        print(f"model of the desktop is {self.model}")
        print(f"generation of the desktop is {self.generation}")
        print(f"processor of the desktop is {self.processor}")

class Loptop(Desktop):
    def __init__(self,b,m,g,p,s,bc):
        super().__init__(b,m,g,p)
        self.screen_size=s
        self.batterycapacity=bc

    def laptop_details(self):
        
        print("\n") 
        super().desktop_details()
        print(f"screen size of the loptop is {self.screen_size}")
        print(f"battery capacity of the laptop is {self.batterycapacity}")
       
class Gaming_Loptop(Loptop):
    def __init__(self,b,m,g,p,s,bc,gr):
        super().__init__(b,m,g,p,s,bc)
        self.graphics=gr

    def gaming_looptop_details(self):
        print("\n")
        super().laptop_details()
        print(f"THe graphics of the gaming laptop is {self.graphics}")
dell=Gaming_Loptop('Dell', 'msi', 5, 55000, 16.5, 5000, 'RTX')

lenovo=Gaming_Loptop('Lenovo', 'slime3', 8, 35000, 15.5, 4800, 'RTX 36800')
hp=Gaming_Loptop('HP','core',9,50000,14.8,6500,'RTX 3650')
dell.desktop_details()
lenovo.laptop_details()
hp.gaming_looptop_details()
        
