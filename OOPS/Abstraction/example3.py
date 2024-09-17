from abc import ABC,abstractmethod

class Polygone(ABC):
    @abstractmethod
    def sides(self):
        pass
class Triable(Polygone):
    def sides(self):
        print("i have three sideS")
class Square(Polygone):
    def sides(self):
        print("i have four  sideS")


class Pentagone(Polygone):
    def sides(self):
        print("i have five sides")
class Hexagone(Polygone):
    def sides(self):
        print("i have Sixe sideS")
        
t=Triable()
t.sides()
s=Square()
s.sides()
p=Pentagone()
p.sides()
h=Hexagone()
h.sides()
