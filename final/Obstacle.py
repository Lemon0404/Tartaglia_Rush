import pyxel
import random

class Obstacle:
    def __init__(self,x):
        self.w=32
        self.h=16
        self.x=x
        self.y=168
        self.num=0
        self.interval=random.randint(0,100)

    def move(self):
        if self.y<168:
            self.y+=1
        if self.y>=168:
            self.num+=1
            if self.num>self.interval:
                self.y=30-self.h
                self.num=0
                self.interval=random.randint(0,100)

    def draw(self):
        pyxel.load("obstacle.pyxres")
        if self.x==0:
            pyxel.blt(self.x,self.y,0,0,0,self.w,self.h,1)
        else:
            pyxel.blt(self.x,self.y,0,0,16,self.w,self.h,1)