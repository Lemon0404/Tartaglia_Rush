import pyxel

from Start import Start
from Player import Player
from Attack import Attack
from Arrows import Arrows
from Enemy import Enemy
from Items import Items
from Background import Background
from Obstacle import Obstacle

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