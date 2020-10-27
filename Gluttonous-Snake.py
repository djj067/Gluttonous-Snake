from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics import Color
from kivy.uix.popup import Popup
from kivy.uix.button import Button
import random


class Mover(App):
    xmin, xmax = 250, 770
    ymin, ymax = 0, 600
    dian = 20
    changd = random.randrange(xmin + dian, xmax - dian, dian), random.randrange(ymin + dian, ymax - dian,
                                                                                       dian)
    ab = 1
    time = 30
    change = .105
    string = ""
    widget = Widget()

    def build(self):
        with self.widget.canvas:
            Color(1, 0, 0, 1)
            self.widget.maca = Rectangle(pos=(self.changd[0], self.changd[1]), size=(20, 20))
            Color(2, 2, 2, 1)
            self.widget.snake = Rectangle(pos=(random.randrange(self.xmin + self.dian, self.xmax - self.dian, self.dian),
                                               random.randrange(self.ymin + self.dian, self.ymax - self.dian, self.dian)),
                                          size=(20, 20)
                                          )
            Color(1, 1, 1, 1)
            self.widget.tail = Rectangle(pos=self.widget.snake.pos, size=(20, 20))
            self.widget.tail2 = Rectangle(pos=(1000, 1000), size=(20, 20))
            self.widget.tail3 = Rectangle(pos=(1000, 1000), size=(20, 20))
            self.widget.tail4 = Rectangle(pos=(1000, 1000), size=(20, 20))
            self.widget.tail5 = Rectangle(pos=(1000, 1000), size=(20, 20))
            self.widget.tail6 = Rectangle(pos=(1000, 1000), size=(20, 20))
            self.widget.tail7 = Rectangle(pos=(1000, 1000), size=(20, 20))
            self.widget.tail8 = Rectangle(pos=(1000, 1000), size=(20, 20))
            Color(0, 0, 1, 1)
            self.widget.bord = Rectangle(pos=(0, 0), size=(250, 1000))

        window = FloatLayout()
        self.shu = Label(text=f"Ab :{self.ab} ", y=220, x=-300)
        self.sjjiangli = Label(text=f"Sjjiangli : {str(self.time)}", y=240, x=-298)
        self.xsnake = self.widget.snake.pos[0]
        self.ysnake = self.widget.snake.pos[1]
        Window.bind(on_key_down=self.acao)
        Clock.schedule_interval(self.mov, self.change)
        Clock.schedule_interval(self.exmple, 1)

        window.add_widget(self.widget)
        window.add_widget(self.sjjiangli)
        window.add_widget(self.shu)

        return window

    def mov(self, zz):
        self.pengzhuang()
        self.growth()
       
        if self.string == "Top":
            self.ysnake += self.dian
            if self.ysnake > self.ymax:
                self.ysnake = self.ymin

        if self.string == "Btm":
            self.ysnake -= self.dian
            if self.ysnake < self.ymin:
                self.ysnake = self.ymax
       
        if self.string == "Zuo":
            self.xsnake += self.dian
            if self.xsnake > self.xmax:
                self.xsnake = self.xmin

        if self.string == "You":
            self.xsnake -= self.dian
            if self.xsnake < self.xmin:
                self.xsnake = self.xmax


        # print(self.widget.snake.pos)
        self.widget.snake.pos = self.xsnake, self.ysnake
        if self.xsnake == self.changd[0] and self.ysnake == self.changd[1]:
            self.coin()

    
     
        def growth(self):
            self.widget.tail.pos = self.widget.snake.pos
        if self.ab == 8:
            self.ganhou()
        if self.ab >= 7:
            self.widget.tail8.pos = self.widget.tail7.pos
        if self.ab >= 6:
            self.widget.tail7.pos = self.widget.tail6.pos
        if self.ab >= 5:
            self.widget.tail6.pos = self.widget.tail5.pos
        if self.ab >= 4:
            self.widget.tail5.pos = self.widget.tail4.pos
        if self.ab >= 3:
            self.widget.tail4.pos = self.widget.tail3.pos
        if self.ab >= 2:
            self.widget.tail3.pos = self.widget.tail2.pos
        if self.ab >= 1:
            self.widget.tail2.pos = self.widget.tail.pos


    def coin(self):
        self.ab += 1
        self.shu.text = f"Ab : {self.ab}"
        self.time += 3
        self.changd = random.randrange(self.xmin + self.dian, self.xmax - self.dian, self.dian),                       random.randrange(self.ymin + self.dian, self.ymax - self.dian, self.dian)
        self.widget.maca.pos = self.changd[0], self.changd[1]
        self.sjjiangli.text = f"Sjjiangli : {str(self.time)}"
        self.change -= .001
    
    def exmple(self, zz):
        if self.time == 0:
            self.gameover()
        if self.string != "":
            self.time -= 1
        self.sjjiangli.text = f"Sjjiangli : {str(self.time)}"

    def acao(self, *args):
        args = str(args)
        args = args.split()
        if len(args) > 5:
            if (args[5] == "79," or args[5] == "7,") and self.string != "You":
                self.string = "Zuo"
            if (args[5] == "80," or args[5] == "4,") and self.string != "Zuo":
                self.string = "You"
            if (args[5] == "82," or args[5] == "26,") and self.string != "Btm":
                self.string = "Top"
            if (args[5] == "81," or args[5] == "22,") and self.string != "Top":
                self.string = "Btm"

   
    def pengzhuang(self):
        bump = [self.widget.tail.pos, self.widget.tail2.pos, self.widget.tail3.pos, self.widget.tail4.pos,
                        self.widget.tail5.pos, self.widget.tail5.pos, self.widget.tail6.pos, self.widget.tail7.pos]
        if self.widget.snake.pos in bump and self.ab > 2:
            self.gameover()
        self.bump = []


    def gameover(self):
        bt = Button(text="ok")
        bt.on_release = exit
        sair = Popup(title="lose", content=bt, auto_dismiss=False, size_hint=(None, None),
                     size=(250, 250))
        sair.open()

    def ganhou(self):
        win = Popup(title="uwin", content=(Label(text="zhuhe")), auto_dismiss=True, size_hint=(None, None),
                     size=(250, 250))
        win.open()


Window.size = 770 + 20, 600+20 
Mover.title = "naugty Snake?"
if __name__ == '__main__':
    Mover().run()

