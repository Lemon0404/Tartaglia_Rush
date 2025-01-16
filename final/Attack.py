import pyxel 

class Attack:
    def __init__(self):
        self.x=0
        self.y=0

    def move(self,player): 
            if player.direct==1:
                self.x=player.x+player.w
                self.y=player.y
            if player.direct==2:
                self.x=player.x-4
                self.y=player.y
            if player.direct==3:
                self.x=player.x
                self.y=player.y+player.h
            if player.direct==4:
                self.x=player.x
                self.y=player.y-4

    def attack_draw(self,player):
        pyxel.load("effect.pyxres")
        if player.direct==1:
            pyxel.load("effect.pyxres")
            pyxel.blt(self.x,self.y,0,0,0,4,16,11)
            # pyxel.load("player.pyxres")
            # pyxel.blt(player.x,player.y,0,16,32,16,16,11)
        if player.direct==2:
            pyxel.load("effect.pyxres")
            pyxel.blt(self.x,self.y,0,8,0,4,16,11)
            # pyxel.load("player.pyxres")
            # pyxel.blt(player.x,player.y,0,0,32,16,16,11)
        if player.direct==3:
            pyxel.load("effect.pyxres")
            pyxel.blt(self.x,self.y,0,16,0,16,4,11)
            # pyxel.load("player.pyxres")
            # pyxel.blt(player.x,player.y,0,32,32,16,16,11)
        if player.direct==4:
            pyxel.load("effect.pyxres")
            pyxel.blt(self.x,self.y,0,16,8,16,4,11)
            # pyxel.load("player.pyxres")
            # pyxel.blt(player.x,player.y,0,48,32,16,16,11)