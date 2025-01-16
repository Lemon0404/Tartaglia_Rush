import pyxel

class Player:
    def __init__(self):
        self.x=30
        self.y=150
        self.w=16
        self.h=16
        self.n_x=1
        # self.n_y=1
        self.direct=1
        self.damage_flag=False
        self.player_hp=5
        self.condition=0#プレイヤーの状態を分ける
        self.num=0
        self.get_num=-1
        self.condition_count=0
        self.attack_flag=False

    def move(self):
        if pyxel.btn(pyxel.KEY_D):
            if self.x<184:
                self.x+=1.5
            self.direct=1
        if pyxel.btn(pyxel.KEY_A):
            if self.x>0:
                self.x-=1.5
            self.direct=2
        if pyxel.btn(pyxel.KEY_S):
            self.direct=3
        if pyxel.btn(pyxel.KEY_W):
            self.direct=4

        #プレイヤーの二つの絵を切り替える関数の更新
        if self.x%4==0:
            self.n_x=-self.n_x
        # if self.y%4==0:
        #     self.n_y=-self.n_y

    def is_damage(self,enemy,obstacle1,obstacle2):
        is_damage=False
        if (self.x-obstacle1.w+2<=obstacle1.x<=self.x+self.w-2) and (self.y-obstacle1.h+2<=obstacle1.y<=self.y+self.h-2):
            is_damage=True
        if (self.x-obstacle2.w+2<=obstacle2.x<=self.x+self.w-2) and (self.y-obstacle2.h+2<=obstacle2.y<=self.y+self.h-2):
            is_damage=True
        if enemy.flag:
            if enemy.type==3:
                if enemy.attack.flag:
                    if self.x-(enemy.attack.w-2)<=enemy.attack.x<=self.x+(self.w-2) and self.y-(enemy.attack.h-1)<=enemy.attack.y<=self.y+(self.h-1):   
                        is_damage=True
            else:
                if self.x-(enemy.w-1)<=enemy.x<=self.x+(self.w-1) and self.y-(enemy.h-1)<=enemy.y<=self.y+(self.h-1):
                    is_damage=True
            
        return is_damage
    
    def damage(self,enemy,obstacle1,obstacle2):
        if self.is_damage(enemy,obstacle1,obstacle2):
            self.damage_flag=True
        if self.is_damage(enemy,obstacle1,obstacle2)==False and self.num>=4:
            self.damage_flag=False
        
        pyxel.sounds[1].set(notes="A2F2", tones="TT", volumes="33", effects="NN", speed=10)
        if self.damage_flag:
            self.num+=1
        else:
            self.num=0

        if enemy.flag:
            if self.is_damage(enemy,obstacle1,obstacle2):
                if enemy.d==0:
                    pyxel.play(0, 1)
                    self.player_hp-=1
                enemy.d+=1
                if enemy.d>=27:
                    enemy.d=0
                if enemy.type==3:
                    enemy.attack.flag=False
            else:
                enemy.d=0

    def draw(self):
        pyxel.load("player.pyxres")
        #ダメージを受けていなかった場合
        if self.damage_flag==False:
            
            if self.condition==0:
                if self.attack_flag:
                    if self.direct==1:
                        pyxel.blt(self.x,self.y,0,16,32,16,16,11)
                    if self.direct==2:
                        pyxel.blt(self.x,self.y,0,0,32,16,16,11)
                    if self.direct==3:
                        pyxel.blt(self.x,self.y,0,32,32,16,16,11)
                    if self.direct==4:
                        pyxel.blt(self.x,self.y,0,48,32,16,16,11)
                else:
                    if self.direct==1:
                        if self.n_x>0:
                            pyxel.blt(self.x,self.y,0,32,0,self.w,self.h,11)
                        else:
                            pyxel.blt(self.x,self.y,0,48,0,self.w,self.h,11)
                    if self.direct==2:
                        if self.n_x>0:
                            pyxel.blt(self.x,self.y,0,0,0,self.w,self.h,11)
                        else:
                            pyxel.blt(self.x,self.y,0,16,0,self.w,self.h,11)
                    if self.direct==3:
                        if self.n_x>0:
                            pyxel.blt(self.x,self.y,0,0,16,self.w,self.h,11)
                        else:
                            pyxel.blt(self.x,self.y,0,16,16,self.w,self.h,11)
                    if self.direct==4:
                        if self.n_x>0:
                            pyxel.blt(self.x,self.y,0,32,16,self.w,self.h,11)
                        else:
                            pyxel.blt(self.x,self.y,0,48,16,self.w,self.h,11)

            if self.condition==1:
                if self.attack_flag:
                    pyxel.blt(self.x,self.y,0,0,64,self.w,self.h,11)
                else:
                    if self.n_x>0:
                        pyxel.blt(self.x,self.y,0,32,64,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,48,64,self.w,self.h,11)

    #ダメージを受けていた場合
        else: 
            if self.num%2==0 and self.num>0:
                if self.condition==0:
                    if self.direct==1:
                        pyxel.blt(self.x,self.y,0,16,48,self.w,self.h,11)
                    if self.direct==2:
                        pyxel.blt(self.x,self.y,0,0,48,self.w,self.h,11)
                    if self.direct==3:
                        pyxel.blt(self.x,self.y,0,32,48,self.w,self.h,11)
                    if self.direct==4:
                        pyxel.blt(self.x,self.y,0,48,48,self.w,self.h,11)
                else:
                    pyxel.blt(self.x,self.y,0,48,64,self.w,self.h,11)