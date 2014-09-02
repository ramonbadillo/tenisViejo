#!/usr/bin/python
import math

class game:
    description = ['love','15','30','40','game']
    scoreP1 = 0
    scoreP2 = 0
    nameP1 = ""
    nameP2 = ""
    ganador = ""
    diff = 0
    
    def __init__(self, nameP1, nameP2):
        self.nameP1 = nameP1
        self.nameP2 = nameP2
        print("[%s , %s]" % (self.description[self.scoreP1], self.description[self.scoreP2]))
    
    def getWinner(self):
        if self.scoreP1 > self.scoreP2:
            self.ganador=self.nameP1
        else:
            self.ganador=self.nameP2
      
    def score(self,quien):
        if self.ganador == "":
            if math.fabs(self.scoreP1 - self.scoreP2) < 4:
                if self.scoreP1 <=4 or self.score <=4:
                    if quien == self.nameP1:
                        self.scoreP1 += 1
                
                    elif quien == self.nameP2:
                        self.scoreP2 += 1
                
                    print("[%s , %s]" % (self.description[self.scoreP1], self.description[self.scoreP2]))
                elif math.fabs(self.scoreP1 - self.scoreP2) < 1:
                    if quien == self.nameP1:
                        self.scoreP1 += 1
                
                    elif quien == self.nameP2:
                        self.scoreP2 += 1
            else:
                #self.ganador="P1"
                self.getWinner()
                print("Felicidades gano: %s" % (self.ganador))
                #print self.filledplayers["one"].value()
                #print("Gano:%s" % (self.scoreP2))
                
        else:
            
            print("Set Terminado Gano:%s" % (self.ganador))

set1 = game(1,2)
set1.score(1)
set1.score(1)
set1.score(1)
set1.score(1)
set1.score(1)
set1.score(1)
set1.score(1)



'''
emp1 = game("Juanito","P2")
emp1.score("Juanito")
emp1.score("Juanito")
emp1.score("Juanito")
emp1.score("Juanito")
emp1.score("P2")
emp1.score("P2")
emp1.score("Juanito")
'''