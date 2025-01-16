import pyxel
import random

class Enemy:
    def __init__(self,stage):
        self.reset_enemy(stage)

    def move(self,player,stage):
        self.time+=1
        if self.flag==True:
            if self.type<=2:
                #エネミーが画面下から出た場合
                if self.y>168:
                    self.reset_enemy(stage)
                #範囲に生存している場合
                elif self.y<=168:
                    self.y+=1

                    #左右にプレイヤーを追尾
                    if self.x<player.x:
                        self.x+=0.2
                    elif self.x>player.x:
                        self.x-=0.2
            if self.type==3:
                if self.y<=30:
                    self.y+=1
                
                #左右にプレイヤーを追尾
                # if self.x<player.x:
                #     self.x+=0.5
                # elif self.x>player.x:
                #     self.x-=0.5

                self.attack.move(self.x,self.y,self.h)


        #倒された場合
        else:
            self.n+=1
        
        #エネミーの二つの絵を切り替える関数の更新
        if self.time%4==0:
            self.e_y=-self.e_y

    def is_kill(self,player,attack,arrows,skill_long):
    # プレイヤーとエネミーの当たり判定を確認
        is_kill=False
        self.kill_with="None"
        if player.condition==0: 
            if player.direct == 1:  # 右向き
                if self.x-3<=attack.x<=self.x+self.w-4 and self.y-player.h+3<=attack.y<=self.y+self.h-3:
                    is_kill=True
                    self.kill_with="attack"
            elif player.direct == 2:  # 左向き
                if self.x<=attack.x<=self.x+self.w-1 and self.y-player.h+3<=attack.y<=self.y+self.h-3:
                    is_kill=True
                    self.kill_with="attack"
            elif player.direct == 3:  # 下向き
                if self.x-player.w+3<=attack.x<=self.x+self.w-3 and self.y-3<=attack.y<=self.y+self.h-4:
                    is_kill=True
                    self.kill_with="attack"
            elif player.direct == 4:  # 上向き
                if self.x-player.w+3<=attack.x<=self.x+self.w-3 and self.y<=attack.y<=self.y+self.h-1:
                    is_kill=True
                    self.kill_with="attack"
        for i in range(len(arrows)):
            if arrows[i].flag:
                if self.x-(arrows[i].w-1)<=arrows[i].x<=self.x+self.w and self.y<=arrows[i].y<=self.y+self.h:
                    arrows[i].flag=False
                    is_kill=True
                    self.kill_with="arrows"
        if skill_long.flag:
            if self.x-skill_long.w+2<=skill_long.x<=self.x+self.w-2 and self.y-skill_long.h+2<=skill_long.y<=self.y+self.h-5:
                is_kill=True
                self.kill_with="skill"
        return is_kill

    def kill(self,player,attack,arrows,skill_long,stage):
        if self.flag and self.is_kill(player,attack,arrows,skill_long):
            if self.kill_with=="attack":
                if player.attack_flag:
                    self.kill_flag=True
                    self.flag=False
            else:
                self.kill_flag=True
                self.flag=False

        if self.n>0:
            self.kill_flag=False            
        if self.n>=4:
            self.reset_enemy(stage)

    def draw(self):
        pyxel.load("enemy.pyxres")
        #倒されていない場合
        if self.flag==True:
            if self.type==3 and 0<self.attack.time<=3:#攻撃の瞬間   
                pyxel.blt(self.x,self.y,0,16+32*(self.type-1),16,self.w,self.h,11)
            else:
                if self.e_y>0:
                    pyxel.blt(self.x,self.y,0,32*(self.type-1),0,self.w,self.h,11)
                else:
                    pyxel.blt(self.x,self.y,0,16+32*(self.type-1),0,self.w,self.h,11)
        #倒された場合
        else:
            pyxel.blt(self.x,self.y,0,32*(self.type-1),16,self.w,self.h,11)

        if self.type==3:
            self.attack.draw()

    def reset_enemy(self,stage):
        self.enemies_w=[13,13,16]
        self.enemies_h=[13,11,13]
        if stage<=5:
            self.type=random.randint(1,2)
        else:
            self.type=random.randint(1,3)
        self.w=self.enemies_w[self.type-1]
        self.h=self.enemies_h[self.type-1]
        self.x=random.randint(10,187)
        self.y=30-self.h
        self.e_y=1
        self.flag=True
        self.kill_flag=False
        self.time=0
        self.n=0
        if self.type==3:
            self.attack=Enemy_Attack(self.x,self.y,self.h)
        self.d=0
        self.kill_with="None"
        # self.give_damage=False

class Enemy_Attack:
    def __init__(self,x,y,h):
        self.reset_value(x,y,h)

    def move(self,x,y,h):
        self.time+=1
        if self.flag==False:
            self.reset_value(x,y,h)
            self.flag=True
        if self.flag:
            self.y+=1
            if self.y>=168:
                self.flag=False
            if self.time%2==0:
                self.num=-self.num
    
    def draw(self):
        pyxel.load("Enemy.pyxres")
        if self.flag:
            if self.num<0:
                pyxel.blt(self.x,self.y,0,64,32,self.w,self.h,11)
            else:
                pyxel.blt(self.x,self.y,0,72,32,self.w,self.h,11)

    def reset_value(self,x,y,h):
        self.time=0
        self.attack_time=0
        self.x=x+4
        self.y=y+h
        self.w=7
        self.h=7
        self.flag=False
        self.num=1
        
