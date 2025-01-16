import pyxel

class Arrows:
    def __init__(self,player,is_skill):
        self.is_skill=is_skill
        self.move_y=0
        if self.is_skill:
            self.w=32
            self.h=48
            self.draw_h=0
            self.x=player.x-8
            self.y=player.y-1
            self.splash_x=player.x-8
            self.splash_y=player.y-16
        else:
            self.x=player.x+7
            self.y=player.y-7
            self.w=3
            self.h=7
        self.flag=True
        self.num=1
        

    def move(self,time):
        if self.is_skill:
            self.move_y+=1
            if self.draw_h<self.h:
                self.draw_h+=2
        self.y-=2
        if self.y<30-self.h:
            self.flag=False
        if time%8==0:
            self.num=-self.num
    
    def arrows_draw(self):
        if self.flag:
            pyxel.load("effect.pyxres")
            pyxel.blt(self.x,self.y,0,34,0,3,7,11)

    def skill_draw(self):
        if self.flag:
            pyxel.load("effect.pyxres")
            if self.move_y<=15:
                if self.num<0:
                    pyxel.blt(self.x,self.y,0,104,0,self.w,self.draw_h,11)
                else:
                    pyxel.blt(self.x,self.y,0,136,0,self.w,self.draw_h,11)
            else:
                if self.num<0:
                    pyxel.blt(self.x,self.y,0,40,0,self.w,self.draw_h,11)
                else:
                    pyxel.blt(self.x,self.y,0,72,0,self.w,self.draw_h,11)
            if self.move_y<=8:
                pyxel.blt(self.splash_x,self.splash_y,0,168,0,self.w,16,11)
            if 8<self.move_y<=16:
                pyxel.blt(self.splash_x,self.splash_y,0,168,16,self.w,16,11)
            if 16<self.move_y<25:
                pyxel.blt(self.splash_x,self.splash_y,0,168,32,self.w,16,11)
                        


