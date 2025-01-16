import pyxel
import random

class Start:
    def __init__(self):
        self.page=0
        self.x=0
        self.y=50
        self.i=-1
        self.f=1
        self.n_x=1
        self.time=0
        self.previous_time=0
        self.first=True
        self.restart=False

    def update(self):
        self.time+=1
        if self.time%6==0:
            self.f=-self.f

        if self.page==0:
            if pyxel.btn(pyxel.KEY_SPACE):
                if self.restart:
                    self.page=3
                else:
                    self.page=1
        if self.page==1:
            if ((121<=pyxel.mouse_x<=125 and 170<=pyxel.mouse_y<=174) and (pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT))) or \
                pyxel.btnp(pyxel.KEY_RIGHT):
                self.page=2
                self.previous_time=self.time
        if self.page==2:
            if ((75<=pyxel.mouse_x<=79 and 170<=pyxel.mouse_y<=174) and (pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT))) or\
                pyxel.btnr(pyxel.KEY_LEFT):
                if (self.time-self.previous_time)>=30:
                    self.page=1
                    self.previous_time=self.time
            if ((121<=pyxel.mouse_x<=125 and 170<=pyxel.mouse_y<=174) and (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT))) or \
                pyxel.btnr(pyxel.KEY_RIGHT):
                if (self.time-self.previous_time)>=30:
                    self.page=3
                    self.previous_time=self.time
        # if self.page==3:
        #     if ((75<=pyxel.mouse_x<=79 and 170<=pyxel.mouse_y<=174) and (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT))) or\
        #         pyxel.btnp(pyxel.KEY_LEFT):
        #         if (self.time-self.previous_time)>=30:
        #             self.page=2
        #             self.previous_time=self.time
        #     if ((121<=pyxel.mouse_x<=125 and 170<=pyxel.mouse_y<=174) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT))) or \
        #         pyxel.btnp(pyxel.KEY_RIGHT):
        #         if (self.time-self.previous_time)>=30:
        #             self.page=4
        if self.page==3:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.page=5

    def draw(self):
        if self.page==0:
            pyxel.load("start.pyxres")
            pyxel.cls(0)
            pyxel.bltm(38,38,0,0,0,128,128,0)
            pyxel.text(120,190,"Thanks to HOYOVERSE",7)
            pyxel.line(10,10,10,190,7)
            pyxel.line(10,10,190,10,7)
            pyxel.line(190,10,190,185,7)
            pyxel.line(10,190,115,190,7)
            if self.f>=0:
                pyxel.text(70,140,"Press SPACE key",7)
        else:
            pyxel.mouse(True)
            if self.first:
                pyxel.cls(0)
            else:
                pyxel.rect(10,10,180,180,0)
            pyxel.line(10,10,10,190,7)
            pyxel.line(10,10,190,10,7)
            pyxel.line(190,10,190,190,7)
            pyxel.line(10,190,190,190,7)
            pyxel.text(75,20,"How to Play "+str(self.page),7)
            if self.page==1:
                pyxel.text(121,170,">",7)
                pyxel.text(115,176,"NEXT",7)
                pyxel.load("start.pyxres")
                pyxel.text(20,40,"1.Move",7)
                pyxel.text(120,45,"Move charactor",7)
                pyxel.text(120,55,"with W/A/S/D KEY",7)
                pyxel.bltm(20,20,0,0,128,160,160,0)
                pyxel.text(20,80,"2.Atack",7)
                pyxel.text(120,85,"Atack wiht",7)
                pyxel.text(120,95,"MOUSE Click",7)
                pyxel.text(20,120,"3.Skill",7)
                pyxel.text(90,135,"When the gauge is full",7)
                pyxel.text(110,145,"press SPACE",7)
                pyxel.text(100,155,"to use your skill",7)
            if self.page==2:
                pyxel.text(20,40,"4.Enemy",7)
                pyxel.text(120,45,"Can get point",7)
                pyxel.text(120,55,"to kill enemies",7)
                pyxel.text(20,80,"5.Items",7)
                pyxel.text(80,85,"bow:",7)
                pyxel.text(100,85,"change attack type",7)
                pyxel.text(80,102,"apple:",7)
                pyxel.text(108,102,"recover your HP",7)
                pyxel.text(80,118,"whale:",7)
                pyxel.text(108,118,"charge skill guage",7)
                pyxel.text(20,136,"6.Obstacle",7)
                pyxel.text(110,145,"touch the obstacle,",7)
                pyxel.text(110,155,"take damage",7)
                pyxel.bltm(20,20,0,192,128,160,160,0)
                pyxel.text(75,170,"<",7)
                pyxel.text(69,176,"BACK",7)
                pyxel.text(121,170,">",7)
                pyxel.text(115,176,"NEXT",7)
            # if self.page==3:
            #     pyxel.text(75,170,"<",7)
            #     pyxel.text(69,176,"BACK",7)
            #     pyxel.text(121,170,">",7)
            #     pyxel.text(115,176,"NEXT",7)
            if self.page==3:
                if self.f>=0:
                    if self.first:
                        pyxel.text(60,80,"Press SPACE to START!!",7)
                    else:
                        pyxel.text(38,80,"Press SPACE to go back to Game!!",7)

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



class Items:
    def __init__(self):
        self.type=random.randint(0,2)
        self.x=random.randint(0,187)
        self.y=0
        if self.type==0:
            self.w=14
            self.h=14
        if self.type==1:
            self.w=14
            self.h=12
        if self.type==2:
            self.w=12
            self.h=13
        self.get_whale=0
        self.flag=True
        self.previous_time=0
        self.go_time=random.randint(self.previous_time,self.previous_time+800)

    def move(self,time):
        #エネミーが画面下から出た場合
        if self.flag==False:
            self.get_whale=0
            self.previous_time=time
            self.x=random.randint(0,187)
            self.type=random.randint(0,2)
            self.y=0
            self.go_time=random.randint(self.previous_time,self.previous_time+800)
        if self.y>168:
            self.flag=False
        if time>=self.go_time: 
            self.flag=True
        #範囲に生存している場合
        if self.y<=168 and self.flag==True:
            if time>=self.go_time:
                self.y+=1
        

    def draw(self,time):
        pyxel.load("items.pyxres")
        #獲得されていない場合
        if self.flag==True:
            if time>=self.go_time:
                pyxel.blt(self.x,self.y,0,16*self.type,0,self.w,self.h,11)
    
    def is_get(self,player):
        if not player.damage_flag and self.flag:
            return player.x-(self.w-2)<=self.x<=player.x+player.w-2 and player.y-(self.h-1)<=self.y<=player.y+player.h-1
            
    def get(self,player,time):
        if time>=self.go_time:
            if self.is_get(player):
                self.flag=False
                player.get_num=self.type
                if self.type==0:        
                    player.condition=1
                    player.condition_count+=200
                if self.type==1:
                    self.get_whale=1
                if self.type==2:
                    if player.player_hp<5:
                        player.player_hp+=1
            
            else:
                player.get_num=-1



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


class App:
    def __init__(self):
        pyxel.init(200,200,fps=20)
        pyxel.sounds[0].set(notes="C3F3", tones="TT", volumes="33", effects="NN", speed=10)
        pyxel.sounds[1].set(notes="A2F2", tones="TT", volumes="33", effects="NN", speed=10)
        pyxel.sounds[2].set(notes="C2", tones="T", volumes="33", effects="N", speed=10)
        pyxel.sounds[3].set(notes="G3F#3F3E3", tones="TTTT", volumes="33", effects="NNNN", speed=100)
        self.resetvalues()
        pyxel.run(self.update,self.draw)

    def update(self):
        if self.start.page<5:
            self.start.update()
        else:
            if not self.GameOver:

                #Tabが押されたらポーズ/ゲームに戻る
                if pyxel.btnp(pyxel.KEY_TAB):
                    if self.pause_flag==False:
                        self.pause_flag=True
                    else:
                        self.pause_flag=False

                #ポーズ中の更新
                if self.pause_flag:
                    if (70<=pyxel.mouse_x<=140 and 60<=pyxel.mouse_y<=100):
                        self.pause_y=80
                    if (70<=pyxel.mouse_x<=140 and 100<pyxel.mouse_y<=140):
                        self.pause_y=120

                    if (142<=pyxel.mouse_x<=149 and 55<=pyxel.mouse_y<=62) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        self.pause_y=0
                        self.pause_flag=False

                    if self.pause_y==80 and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.KEY_KP_ENTER)):
                        self.start.page=0
                        self.resetvalues()
                        if self.start.page>5:
                            self.pause_flag=False
                    if self.pause_y==120 and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.KEY_KP_ENTER)):
                        self.start.first=False
                        self.start.page=1

                #ポーズしていない場合
                else:

                    self.time+=1
                    self.previos_point=self.point
                    self.player.move()

                    #背景の更新
                    self.background.move()

                    #障害物の移動
                    self.obstacle1.move()
                    self.obstacle2.move()

                    #アイテムの更新
                    for i in range(self.item_num):
                        self.items[i].move(self.time)
                        self.items[i].get(self.player,self.time)
                        if self.items[i].get_whale==1:
                            self.skill_gauge+=2

                    #プレイヤーの状態の更新
                    if self.player.condition==1:
                        self.player.condition_count-=1
                    if self.player.condition_count<0:
                        self.player.condition=0
                        self.player.condition_count=0

                    #スキルの更新
                    # if self.player.condition==1:
                    if self.skill_gauge>=12:
                        if self.skill_long.flag==False:
                            if pyxel.btnp(pyxel.KEY_SPACE):
                                self.skill_long.flag=True
                                self.skill_long.x=self.player.x-8
                                self.skill_long.y=self.player.y-1
                                self.skill_long.splash_x=self.player.x-8
                                self.skill_long.splash_y=self.player.y-16
                                self.skill_gauge=0
                    if self.skill_long.flag:
                        self.skill_long.move(self.time)


                    for i in range(len(self.enemies)):       
                        self.enemies[i].move(self.player,self.stage)#エネミーの更新処理 
                        self.player.damage(self.enemies[i],self.obstacle1,self.obstacle2)#プレイヤーのダメージ判定
                        self.enemies[i].kill(self.player,self.attack,self.arrows,self.skill_long,self.stage)#エネミーのキル判定

                        #敵を倒した時の更新
                        pyxel.sounds[0].set(notes="C3F3", tones="TT", volumes="33", effects="NN", speed=10)
                        pyxel.sounds[2].set(notes="C2", tones="T", volumes="33", effects="N", speed=10)#入れないとならない...?
                        if self.enemies[i].kill_flag:
                            pyxel.play(0,0)    
                            self.point+=10
                            self.combo+=1
                            if self.skill_gauge<12:
                                self.skill_gauge+=1
                            if self.fever_gauge<42:
                                if self.combo<10:
                                    self.fever_gauge+=1
                                else:
                                    self.fever_gauge+=2
                        else:
                            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                                if self.player.condition==0:
                                    pyxel.play(0,2)
                        if self.player.damage_flag:
                            if self.enemies[i].n==0:
                                self.combo=0
                        

                    #攻撃
                    pyxel.sounds[2].set(notes="C2", tones="T", volumes="33", effects="N", speed=10)#入れないとならない...?
                    self.attack.move(self.player)
                    
                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        if self.player.condition==0:
                            self.player.attack_flag=True
                        if self.player.condition==1:
                            if self.arrows==[]:
                                pyxel.play(0,2)
                                self.arrows.append(Arrows(self.player,is_skill=False))
                                self.player.attack_flag=True
                            elif self.arrows[-1].y<=self.player.y-40:
                                pyxel.play(0,2)
                                self.arrows.append(Arrows(self.player,is_skill=False))
                                self.player.attack_flag=True

                    if self.player.attack_flag:
                        self.attack_count+=1
                    if self.attack_count>=4:
                        self.player.attack_flag=False
                        self.attack_count=0
                            
                    for i in range(len(self.arrows)):
                        if self.arrows[i].flag:
                            self.arrows[i].move(self.time)
                        if self.arrows[i].flag==False:
                            del self.arrows[i]
                            break
                    
                    #ステージの更新
                    if self.point!=0 and self.point==self.stage*50 and self.previous_point!=self.point:
                        self.stage+=1
                        #ステージに応じたエネミーの追加
                        if len(self.enemies)<10:
                            self.enemies.append(Enemy(self.stage))
            else:
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    self.longpress_count+=1
                if self.longpress_count>=60:
                    self.resetvalues()
                    self.start.restart=True

                        
            pyxel.sounds[3].set(notes="G3F#3F3E3", tones="TTTT", volumes="33", effects="NNNN", speed=100)
            if self.player.player_hp<=0:
                if self.GameOver==False:
                    self.GameOver=True
                    pyxel.play(0,3)
            

    def draw(self):
        if self.start.page<5:
            self.start.draw()
        else:
            if self.GameOver==False:
                pyxel.cls(5)

                self.background.draw(self.stage)
                #スキルの描画
                if self.skill_long.flag:         
                    self.skill_long.skill_draw()

                #障害物の描画
                self.obstacle1.draw()
                self.obstacle2.draw()

                #プレイヤーの描画
                self.player.draw()
                for i in range(self.item_num):
                    self.items[i].draw(self.time)
                
                        
                #攻撃モーション
                if self.pause_flag==False:
                    if self.player.condition==0:
                        if self.player.attack_flag==True:
                            self.attack.attack_draw(self.player)
                    # if self.player.condition==1:
                    for i in range(len(self.arrows)):
                        if self.arrows[i].flag==True:
                            self.arrows[i].arrows_draw()

                
                
                #敵の描画
                for i in range(len(self.enemies)):
                    self.enemies[i].draw()

                #画面の表示
                pyxel.rect(0,0,200,30,0)
                pyxel.rect(0,168,200,32,0)
                pyxel.line(0,30,200,30,7)
                pyxel.line(0,168,200,168,7)

                pyxel.line(3,197,17,197,7)
                pyxel.line(3,197,3,190,7)
                pyxel.line(3,190,17,190,7)
                pyxel.line(17,190,17,197,7)
                pyxel.text(5,191,"Tab pause",7)


                #ポイントの表示
                pyxel.text(5,3,"Point: "+str(self.point),7)
                pyxel.text(5,10,str(self.time),7)

                #コンボの表示
                if self.combo>0:
                    pyxel.text(5,17,str(self.combo)+"Combo!!",7)
                    
                #ステージの表示
                pyxel.text(87,5,"stage"+str(self.stage),7)
                
                #hpゲージの描画
                pyxel.load("effect.pyxres")
                for i in range(5):
                    pyxel.blt(149+i*10,3,0,0,16,9,9,11)
                for i in range(self.player.player_hp):
                    pyxel.blt(149+i*10,3,0,16,16,9,9,11)

                #スキルゲージの描画
                pyxel.load("effect.pyxres")
                pyxel.blt(170,170,0,0,96,24,24,11)
                if self.skill_gauge<12:
                    for i in range(int(self.skill_gauge/2)):
                        pyxel.blt(170,193-4*(i+1),0,24,119-4*(i+1),24,4,11)
                else:
                    pyxel.blt(169,169,0,48,96,26,26,11)

                #フィーバーゲージの描画
                # pyxel.load("effect.pyxres")
                # pyxel.blt(137,12,0,2,48,13,13,11)
                # pyxel.blt(152,16,0,17,51,46,7,11)
                # for i in range(int(self.fever_gauge)):
                #     pyxel.blt(154+i,16,0,19+i,67,1,7,11)
                # if self.fever_gauge>=42:
                #     pyxel.blt(137,13,0,2,80,13,14,11)
                #     pyxel.blt(152,16,0,17,83,46,7,11)


                if self.skill_gauge>=12:
                    if self.time%2==0:
                        pyxel.text(50,180,"press SPACE to use skill!!",7)
                if self.fever_gauge>=42:
                    if self.time%2!=0:
                        pyxel.text(58,80,"press ENTER to fever!!",7)
            else:
                #ゲームオーバーの場合の表示
                pyxel.cls(0)
                pyxel.load("gameover.pyxres")
                pyxel.bltm(0,0,0,0,0,200,200,0)
                pyxel.text(96,96,"Score:"+str(self.point),7)
                pyxel.text(96,106,"Time:"+str(self.time),7)
                pyxel.text(55,130,"Press and hold to restart!",7)



            

            #ポーズ中の描画
            if self.pause_flag:
                pyxel.mouse(True)
                pyxel.load("effect.pyxres")
                pyxel.rect(50,50,100,100,0)
                pyxel.line(50,50,50,150,7)
                pyxel.line(50,150,150,150,7)
                pyxel.line(150,150,150,50,7)
                pyxel.line(150,50,50,50,7)
                pyxel.text(70,80,"Back to the title",7)
                pyxel.text(70,120,"View manual",7)
                if self.pause_y>0:
                    pyxel.blt(self.pause_x,self.pause_y,0,0,32,3,5,11)
                pyxel.blt(142,55,0,8,32,7,7,11)
            else:
                pyxel.mouse(False)

    #再スタートの処理を行う関数
    def resetvalues(self):
        pyxel.sounds[0].set(notes="C3F3", tones="TT", volumes="33", effects="NN", speed=10)
        pyxel.sounds[1].set(notes="A2F2", tones="TT", volumes="33", effects="NN", speed=10)
        pyxel.sounds[2].set(notes="C2", tones="T", volumes="33", effects="N", speed=10)
        pyxel.sounds[3].set(notes="G3F#3F3E3", tones="TTTT", volumes="33", effects="NNNN", speed=100)
        self.time=0
        self.previous_time=0
        self.point=0
        self.previous_point=0
        self.GameOver=False
        self.pause_flag=False
        self.pause_x=60
        self.pause_y=80
        self.player=Player()
        self.stage=1
        self.enemies=[]
        self.enemies.append(Enemy(self.stage))
        self.combo=0
        self.start=Start()
        self.fever_gauge=0#MAX42
        self.skill_gauge=0#MAX12
        self.skill_long=Arrows(self.player,is_skill=True)
        self.skill_long.flag=False
        self.items=[]
        self.attack=Attack()
        self.arrows=[]
        self.item_num=5
        self.attack_count=0
        self.longpress_count=0
        for _ in range(self.item_num):
            self.items.append(Items())
        self.background=Background()
        self.obstacle1=Obstacle(0)
        self.obstacle2=Obstacle(168)


App()