#C:Python31python.exe
# -*- coding:utf-8 -*-
import tkinter as tk
from random import *
size=30
offset=10
x,y=None,None
helding,heldx,heldy=False,0,0
cseq=["red","blue","green","yellow","purple","pink"]
ball=[[choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq)],
      [choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq)],
      [choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq)],
      [choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq)],
      [choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq),choice(cseq)]]

def get(event):
    global x,y,helding,heldx,heldy
    x,y=event.x,event.y
    heldx,heldy=event.x,event.y
    x,y=int((x-offset)/(size*2)),int((y-offset-size*10)/(size*2))
    if x<0 or x>5 or y<0 or y>4:
        x,y=None,None
    else:
        helding=True
    label['text']=str(x)+","+str(y)+"_"+str(heldx)+","+str(heldy)

def held(event):
    global helding,heldx,heldy,x,y
    heldx,heldy=event.x,event.y
    
    if heldx<offset:
        heldx=offset+1
    elif heldx>offset+size*12:
        heldx=offset+size*12-1
    if heldy<offset+size*10:
        heldy=offset+size*10+1
    elif heldy>offset+size*20:
        heldy=offset+size*20-1

    if(heldx<x*size*2+size+offset-size):
        ball[y][x],ball[y][x-1],x=ball[y][x-1],ball[y][x],x-1
    elif(heldx>x*size*2+size+offset+size):
        ball[y][x],ball[y][x+1],x=ball[y][x+1],ball[y][x],x+1
    elif(heldy<y*size*2+size*11+offset-size):
        ball[y][x],ball[y-1][x],y=ball[y-1][x],ball[y][x],y-1
    elif(heldy>y*size*2+size*11+offset+size):
        ball[y][x],ball[y+1][x],y=ball[y+1][x],ball[y][x],y+1
    
    label['text']=str(x)+","+str(y)+"_"+str(heldx)+","+str(heldy)

def release(event):
    global helding,heldx,heldy,x,y
    helding,heldx,heldy,x,y=False,0,0,None,None

def update():
    canvas.delete("ball")
    for rol in range(0,5):
        for col in range(0,6):
            if(rol!=y or col!=x):
                canvas.create_oval(col*2*size+offset,rol*2*size+offset+size*10,
                                   (col+1)*2*size+offset,(rol+1)*2*size+offset+size*10,
                                   fill=ball[rol][col],tag="ball")
            else:
                canvas.create_oval(col*2*size+offset,rol*2*size+offset+size*10,
                                   (col+1)*2*size+offset,(rol+1)*2*size+offset+size*10,
                                   fill="#aaa",tag="ball",outline="")
    if(helding):
        canvas.create_oval(heldx-size,heldy-size,
                           heldx+size,heldy+size,
                           fill=ball[y][x],tag="ball")
                
    canvas.after(50,update)

win=tk.Tk()
win.title("tkinter GUI")
win.geometry(str(size*12+offset*2)+"x"+str(size*20+offset*2+30))
win.resizable(False,False)

label=tk.Label(win)
label.pack()



canvas = tk.Canvas(win, width=size*12+offset*2, height=size*20+offset*2,bg='black')
canvas.bind("<Button-1>", get)
canvas.bind("<B1-Motion>", held)
canvas.bind("<ButtonRelease-1>", release)
canvas.after(50,update)
canvas.create_polygon(offset,offset,
                      offset+size*12,offset,
                      offset+size*12,offset+size*20,
                      offset,offset+size*20,fill='white',tag="body")
canvas.pack()


win.mainloop()
