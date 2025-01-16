import pyxel

class Background:
    def __init__(self):
        pyxel.load("background.pyxres")
        self.x=64*8
        self.y=95*8
        self.w=200
        self.h=137

    def move(self):
        self.y-=0.5
        if self.y<=0:
            self.y=95*8

    def draw(self,stage):
        if stage<=10:
            pyxel.load("background.pyxres")
            pyxel.bltm(0,31,0,self.x,self.y,self.w,self.h,0)