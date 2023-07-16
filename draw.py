#print("Hello world!")
from PIL import Image
import turtle 
import random

#tur = turtle.Turtle()
turtle.tracer(False)

"""
def find_cood():
    def click(x,y):
        print(x,y)
    turtle.onscreenclick(click,1)
    turtle.listen()
    turtle.speed(10)
"""
ps_ad=[]
def convert(w,_type_):
    temp = (random.randrange(1000,9999))
    if temp not in ps_ad:
            ps_ad.append(temp)
    else:
        convert()

    w.getscreen().getcanvas().postscript(file = _type_+str(temp)+'.eps')
    fig = Image.open(_type_+str(temp)+'.eps')
    img = fig.convert('RGBA')
    return img

def tshirt(w,color):
    w.setpos(0.0,0.0)
    w.fillcolor(color)
    w.begin_fill()
    w.forward(115)
    w.left(90)
    w.forward(150)
    w.goto(142.0, 117.0)
    w.goto(170.0, 138.0)
    w.goto(120.0, 197.0)
    w.left(90)
    w.forward(38.33)
    w.left(90)
    for i in range(105):
        w.right(1.72)
        w.forward(0.8)
    w.left(90)
    w.forward(38.33)
    w.goto(-67.0, 146.0)
    w.goto(-46.0, 117.0)
    w.goto(-11.0, 148.0)
    w.goto(-11.0,1.0)
    w.goto(0.0, 0.0)
    w.end_fill()

def pant(w,color):
    w.penup()
    w.setpos(0.0,0.0)
    w.pendown()
    w.fillcolor(color)
    w.begin_fill()
    w.goto(-11.0,0.0)
    w.goto(-11.0, -183.0)
    w.goto(35.0, -183.0)
    w.goto(47.0, -35.0)
    w.goto(53.0, -35.0)
    w.goto(69.0, -183.0)
    w.goto(115.0, -183.0)
    w.goto(115.0, -0.0)
    w.goto(0.0,0.0)
    w.end_fill()

def shirt(w,color):
    w.setpos(0.0,0.0)
    w.fillcolor(color)
    w.begin_fill()
    w.forward(115)
    w.left(90)
    w.forward(150)
    w.goto(142.0, 117.0)
    w.goto(170.0, 138.0)
    w.goto(120.0, 197.0)
    w.left(90)
    w.forward(38.33)
    w.left(90)
    for i in range(45):
        w.right(1)
        w.forward(0.8)
    w.right(90)
    w.forward(23)
    w.right(90)
    for i in range(45):
        w.left(1)
        w.forward(0.8)
    w.right(130)
    w.forward(25)
    w.setpos(65.0, 212.0)
    w.right(140)
    w.forward(38.33)
    w.left(47)
    w.forward(23)
    w.left(55)
    for i in range(45):
        w.left(1)
        w.forward(0.9)
    w.left(90)
    w.forward(25)
    w.left(95)
    for i in range(45):
        w.right(1)
        w.forward(0.8)
    w.setpos(11.0,194.0)
    w.left(73)
    w.forward(33.33)
    w.goto(-67.0, 146.0)
    w.goto(-46.0, 117.0)
    w.goto(-11.0, 148.0)
    w.goto(-11.0,1.0)
    w.goto(0.0, 0.0)
    w.setpos(51.0,0)   
    w.goto(51.0,181.0)
    w.goto(48.0, 184.0)     
    w.end_fill()

def shoes(w):
    w.penup()
    w.goto(-11.0,-184.4)
    w.pendown()

class combo:
    def __init__(self,Ucolor,Pcolor,var=None):
        self.Ucolor = Ucolor
        self.Pcolor = Pcolor
        self.var = var
    def casuals(self):
        cas_tur = turtle.Turtle()
        tshirt(cas_tur,self.Ucolor)
        pant(cas_tur,self.Pcolor)
        shoes(cas_tur)
        cas_tur._tracer(True)
        cas_tur.hideturtle()
        out = convert(cas_tur,"casuals")
        turtle.done()
        return out
    def formals(self):
        for_tur = turtle.Turtle()
        shirt(for_tur,self.Ucolor)
        pant(for_tur,self.Pcolor)
        shoes(for_tur)
        for_tur._tracer(True)
        for_tur.hideturtle()
        out = convert(for_tur,"formals")
        turtle.done()  
        return out

#set1=combo('red','black',3)
#set2=combo('blue','red')
#a = set1.formals

#diff window each drawing
