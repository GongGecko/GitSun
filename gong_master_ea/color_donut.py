from turtle import *
import random

def coldonut():
    colormode(255)# 设置色彩模式是RGB
    speed(10)
    width(2)
    for i in range(200):
        r=int(random.uniform(0,255))
        g=int(random.uniform(0,255))
        b=int(random.uniform(0,255))
        fd(100)
        if(i%2==0):
            pencolor(r,g,b)
            rt(155)
        else:
            pencolor(r,g,b)
            lt(100)


if __name__=='__main__':
    coldonut()
    done()