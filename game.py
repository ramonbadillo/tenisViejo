import math

class game:
    description = ['love','15','30','40','game']
    scoreP1 = 0
    scoreP2 = 0
    nameP1 = ""
    nameP2 = ""
    ganador = ""
    diff = 0
    cuatros = False
    
    def __init__(self, nameP1, nameP2):
        self.nameP1 = nameP1
        self.nameP2 = nameP2
        print "game start"
        print("[%s , %s]" % (self.description[self.scoreP1], self.description[self.scoreP2]))
    
    
    def score(self,quien):
        if self.ganador == "":
            if quien == self.nameP1:
                self.scoreP1 += 1
            elif quien == self.nameP2:
                self.scoreP2 += 1
            self.getWinner()
            self.showResults()
        else:
            print("Set Terminado Gano:%s" % (self.ganador))
    
    
    def getWinner(self):
        diff = math.fabs(self.scoreP1 - self.scoreP2)
        print diff
        if self.scoreP1 <=3 or self.score <=3:
            self.cuatros = True
            
        if diff > 3:
            if self.scoreP1 > self.scoreP2:
                self.ganador=self.nameP1
            else:
                self.ganador=self.nameP2
            print("Felicidades gano: %s" % (self.ganador))
        
        if self.diff > 2 and self.cuatros:
            if self.scoreP1 > self.scoreP2:
                self.ganador=self.nameP1
            else:
                self.ganador=self.nameP2
            print("Felicidades gano: %s" % (self.ganador))   
            
    
    
    def showResults(self):
        if not self.cuatros:
            print("[%s , %s]" % (self.description[self.scoreP1], self.description[self.scoreP2]))
        else:
            print("[%s , %s]" % (self.scoreP1, self.scoreP2))
            
            
set1 = game(1,2)
set1.score(1)
set1.score(2)
set1.score(1)
set1.score(2)
set1.score(1)
set1.score(1)
set1.score(1)