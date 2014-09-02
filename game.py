'''
Al inicio del juego cómo debe de estar el score?
>>> Game().score()
[0, 0]

Cuando un jugador anota
>>> Game().scores(1).score()
[15, 0]

Cuando un jugador anota 3 veces seguidas
>>> Game().scores(1).scores(1).scores(1).score()
[40, 0]

Cuando un jugador anota 4 veces seguidas
>>> Game().scores(1).scores(1).scores(1).scores(1).score()
[Wins, Loses]

Cuando el otro jugador le empata
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).score()
[Deuce, Deuce]

Cuando estan empatados y uno obtiene la ventaja
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).score()
[Adv, ]

Cuando después de tener la ventaja vuelven a empatar
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).score()
[Deuce', Deuce]

Cuando obtiene la ventaja y además anota otro punto
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(1).score()
[Wins, Loses]
'''

import math

class Game:
    
    
    description = ['0','15','30','40','Adv']
    pScores = [0,0]
    pScoresF = ["",""]
    flag = False
    win = False
    diff =  0
    empates = False
    
    def __init__(self):pass
        
        
    def scores(self, player):
        if not self.win:
            player -=1
            self.pScores[player] += 1
        else:
            print("Se acabo el set")
    
           
           
           
            
    def score(self):
        self.diff = math.fabs(self.pScores[0] - self.pScores[1])
        if self.pScores[0] >= 3 and self.pScores[1] >= 3:
            self.flag = True
        elif self.pScores[0] > 3 or self.pScores[1] > 3 and not self.flag:
            self.getWinner()
            self.flag = True
        if self.flag:
            if self.diff > 1:
                self.getWinner()
            elif self.diff == 0:
                self.pScoresF[0] = 'Deuce'
                self.pScoresF[1] = 'Deuce'
            else:
                self.getAdv()
        self.showResults()
        
        return self
        
       
        if self.diff > 1 and self.cuatros:
            self.getAdvantage()
        
        
    def showResults(self):
        if not self.flag:
            print("[%s, %s]" % (self.description[self.pScores[0]], self.description[self.pScores[1]]))
        else:
            print("[%s, %s]" % (self.pScoresF[0], self.pScoresF[1]))
    
    def getAdv(self):
        if self.pScores[0] > self.pScores[1]:
            self.pScoresF[0] = 'Adv'
            self.pScoresF[1] = ''
        if self.pScores[0] < self.pScores[1]:
            self.pScoresF[1] = ''
            self.pScoresF[0] = 'Adv'
            
    def getWinner(self):
        if self.pScores[0] > self.pScores[1]:
            self.pScoresF[0] = 'Wins'
            self.pScoresF[1] = 'Loses'
        if self.pScores[0] < self.pScores[1]:
            self.pScoresF[1] = 'Wins'
            self.pScoresF[0] = 'Loses'
        self.win = True
        



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    