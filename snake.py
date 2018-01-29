from tkinter import *
from random import *
#________________________________________________________________________________________
width=10
size=30
move_speed=500
update_speed=100
start=[]
a=None
#________________________________________________________________________________________
body=[[0,0],[1,0],[2,0]]
direct="Right"
food=[randint(0,width-1),randint(0,width-1)]
while(food in body):
    food=[randint(0,width-1),randint(0,width-1)]
upadted=False
lose=False
#________________________________________________________________________________________
def key(event):
    global direct,updated
    if((direct=="Up" and event.keysym!="Down") or
       (direct=="Down" and event.keysym!="Up") or
       (direct=="Left" and event.keysym!="Right") or
       (direct=="Right" and event.keysym!="Left")) and updated:
        direct,updated=event.keysym,False
def forward():
    global food,lose,updated
    old_head=body[len(body)-1]
    new_head=[0,0]
    if(direct=="Up"):
        new_head=[old_head[0],(old_head[1]-1)%width]
    elif(direct=="Down"):
        new_head=[old_head[0],(old_head[1]+1)%width]
    elif(direct=="Left"):
        new_head=[(old_head[0]-1)%width,old_head[1]]
    elif(direct=="Right"):
        new_head=[(old_head[0]+1)%width,old_head[1]]
    updated=True
    if(new_head in body):
        lose=True
    else:
        body.append(new_head)
        if(new_head!=food):
            body.pop(0)
        else:
            while(food in body):
                food=[randint(0,width-1),randint(0,width-1)]
    if(lose!=True):
        move.after(move_speed,forward)
def canvas_update():
    canvas.delete('snack')
    for a in body:
        canvas.create_polygon(a[0]*size, a[1]*size,
                              (a[0]+1)*size,a[1]*size,
                              (a[0]+1)*size,(a[1]+1)*size,
                              a[0]*size,(a[1]+1)*size,tag='snack')
    canvas.create_polygon(body[len(body)-1][0]*size, body[len(body)-1][1]*size,
                          (body[len(body)-1][0]+1)*size,body[len(body)-1][1]*size,
                          (body[len(body)-1][0]+1)*size,(body[len(body)-1][1]+1)*size,
                          body[len(body)-1][0]*size,(body[len(body)-1][1]+1)*size,fill='blue',tag='snack')
    canvas.delete('food')
    canvas.create_polygon(food[0]*size, food[1]*size,
                          (food[0]+1)*size,food[1]*size,
                          (food[0]+1)*size,(food[1]+1)*size,
                          food[0]*size,(food[1]+1)*size,fill='red',tag='food')
    move['text']="Length: "+str(len(body))
    if(lose!=True):
        canvas.after(update_speed,canvas_update)
    else:
        move['text']="Lose! Length: "+str(len(body))
    if(len(body)>=width*width):
        move['text']="Win!"
#________________________________________________________________________________________
window = Tk()
window.title('Snack')

move=Label(window,text="Length: "+str(len(body)),width=40)
move.focus_set()
move.bind("<Key>",key)
move.after(move_speed,forward)
move.pack()
    
canvas=Canvas(window,width=width*size, height=width*size, bg='white')
canvas.after(update_speed,canvas_update)
canvas.pack()

mainloop()














