import math

class game:
    description = ['Love','15','30','40','Adv']
    scoreP1 = 0
    scoreP2 = 0
    nameP1 = ""
    nameP2 = ""
    ganador = ""
    diff = 0
    cuatros = False
    scores = ["",""]
    
    
    
    def __init__(self, nameP1, nameP2):
        self.nameP1 = nameP1
        self.nameP2 = nameP2
        #print("%s , %s" % (self.description[self.scoreP1], self.description[self.scoreP2]))
    
    def scores(self,quien):
        if self.ganador == "":
            if quien == self.nameP1:
                self.scoreP1 += 1
            elif quien == self.nameP2:
                self.scoreP2 += 1
            
            #self.getWinner()
            #self.showResults()
        else:
            print("Set Terminado Gano:%s" % (self.ganador))
        return self
        
    def score(self):
        self.getWinner()
        self.showResults()
    
    
    def getWinner(self):
        
        if self.scoreP1 >=3 and self.scoreP2 >=3:
			self.cuatros = True
			self.diff = math.fabs(self.scoreP1 - self.scoreP2)		
            
			if self.diff==0:
				print "Douce"
				
			if self.diff==1:
				print "Adv"
				
			if self.diff > 1:
				self.getAdvantage()
				
		else :
			if self.scoreP1 >3 or self.scoreP2 >3:
				self.getAdvantage()
          
        
            
        
        
    def showResults(self):
        print self.cuatros
		if self.ganador != "":
            print "Win"
        elif not self.cuatros:
            print("%s,%s" % (self.description[self.scoreP1], self.description[self.scoreP2]))
        
    
    def getAdvantage(self):
        if self.scoreP1 > self.scoreP2:
            self.ganador = self.nameP1
        elif self.scoreP1 < self.scoreP2:
            self.ganador = self.nameP2
           
            
game(1,2).scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).scores(2).score()
''''
set1.score(2)
set1.score(2)
set1.score(1)
set1.score(1)
set1.score(1)
set1.score(2)
set1.score(2)

'''
