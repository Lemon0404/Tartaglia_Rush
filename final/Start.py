import pyxel

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