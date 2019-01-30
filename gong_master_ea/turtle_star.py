from turtle import *

color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()

pu();goto(-180,-50);color("violet")
write('快乐',align="left",font=("Arial",40,"normal"))