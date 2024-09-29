import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="connecting satelliite"
totalnumber=12
lines=[]
target=0
rock=[]
for i in range(totalnumber):
    x=random.randint(50,750)
    y=random.randint(50,550)
    satelliite=Actor("satelliite")
    satelliite.pos=(x,y)
    rock.append(satelliite)



def draw():
    screen.clear()
    screen.blit("space",(0,0))
    number=1
    for satelliite in rock:
        satelliite.draw()
        screen.draw.text(str(number),(satelliite.x-30,satelliite.y),color="white")
        number=number+1
    for line in lines:
        print(line)
        screen.draw.line(line[0],line[1],"white")

def on_mouse_down(pos):
   global target,lines
   if rock[target].collidepoint(pos):
       if target>0:
           lines.append((rock[target-1].pos,rock[target].pos))
       target=target+1
   else:
       target=0
       lines=[]
       
def update():
    pass







pgzrun.go()