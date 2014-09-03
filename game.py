"""
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
['Win', 'Lose']

Cuando el otro jugador le empata
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).score()
['Deuce', 'Deuce']

Cuando estan empatados y uno obtiene la ventaja
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).score()
['Adv', 'Deuce']

Cuando después de tener la ventaja vuelven a empatar
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).score()
['Deuce', 'Deuce']

Cuando obtiene la ventaja y además anota otro punto
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(1).score()
['Win', 'Lose']
"""

import math

class Game:
    
    description = [0,15,30,40,'Deuce','Adv','Win','Lose']
    puntos = [0,0]
    
    def __init__(self):
        self.puntos[0] = 0
        self.puntos[1] = 0   
        
    def scores(self, player):
        if player <=2 and player > 0:
            player -=1
            self.puntos[player] += 1
        else:
            print("Jugador no valido")
        self.check()
        return self
                  
            
    def check(self):
        if self.puntos[0]>6:
            self.puntos[0]-=1

        if self.puntos[1]>6:
            self.puntos[1]-=1

        if  self.puntos[0]>3 and self.puntos[1]<3:
            self.puntos[0] = 6

        if  self.puntos[0]<3 and self.puntos[1]>3:
            self.puntos[1] = 6

        if self.description[self.puntos[0]] == 40 and self.description[self.puntos[1]] == 40:
            self.puntos[0]+=1
            self.puntos[1]+=1

        if self.description[self.puntos[0]] == 'Adv' and self.description[self.puntos[1]] == 'Adv':
            self.puntos[0]-=1
            self.puntos[1]-=1

        if self.description[self.puntos[0]] == 'Win':
            self.puntos[1] =7

        if self.description[self.puntos[1]] == 'Win':
            self.puntos[0] =7

        return self       
        
    def score(self):
        return [self.description[self.puntos[0]], self.description[self.puntos[1]]]

if __name__ == "__main__":
    import doctest
    doctest.testmod()