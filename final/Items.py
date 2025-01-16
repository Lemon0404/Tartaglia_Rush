import pyxel
import random

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
