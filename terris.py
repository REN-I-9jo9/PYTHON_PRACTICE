from tkinter import *
from random import *
#________________________________________________________________________________________
width=10
height=20
size=30
drop_speed=1000
update_speed=100
start_x=width/2
#________________________________________________________________________________________
bitmap=[]
empty_line=[]
for i in range(0,height):
    empty_line=[]
    for j in range(0,width):
        empty_line.append(False)
    bitmap.append(empty_line)
#_______________________
init_x=[[-1, 0,-1, 0],#0
        [-2,-1, 0, 1],#1
        [ 0,-1, 0, 1],#2
        [-1, 0, 0, 1],#3
        [-1, 0, 0, 1],#4
        [-1, 0, 1, 1],#5
        [-1, 0, 1,-1]]#6
#-----------------------
init_y=[[ 0, 0, 1, 1],#0
        [ 0, 0, 0, 0],#1
        [ 0, 0, 1, 0],#2
        [ 0, 0, 1, 1],#3
        [ 1, 1, 0, 0],#4
        [ 0, 0, 0, 1],#5
        [ 0, 0, 0, 1]]#6
#_______________________
lose=False
score=0
block_type=randint(0,6)
rotate_type=0
x=init_x[block_type]
x=[x[0]+start_x,x[1]+start_x,x[2]+start_x,x[3]+start_x]
y=init_y[block_type]
#________________________________________________________________________________________
def hit():
    if((-1 in x) or
       (width in x) or
       (-1 in y) or
       (height in y) or
       (True in [bitmap[int(y[0])][int(x[0])],
                 bitmap[int(y[1])][int(x[1])],
                 bitmap[int(y[2])][int(x[2])],
                 bitmap[int(y[3])][int(x[3])]])):
        return True
    else:
        return False
#________________________________________________________________________________________
def key(event):
    global x,y,rotate_type
    tmp_x,tmp_y,tmp_r=x,y,rotate_type
    if(event.keysym=="Up"):
        if(block_type==1):
            if(rotate_type==0):
                x,y,rotate_type=[x[0],x[1]-1,x[2]-2,x[3]-3],[y[0],y[1]+1,y[2]+2,y[3]+3],1
            elif(rotate_type==1):
                x,y,rotate_type=[x[0],x[1]+1,x[2]+2,x[3]+3],[y[0],y[1]-1,y[2]-2,y[3]-3],0
        elif(block_type==2):
            if(rotate_type==0):
                x,y,rotate_type=[x[0],x[1]+1,x[1],x[2]],[y[0],y[1]-1,y[1],y[2]],1
            elif(rotate_type==1):
                x,y,rotate_type=[x[0],x[1]+1,x[1],x[2]],[y[0],y[1]+1,y[1],y[2]],2
            elif(rotate_type==2):
                x,y,rotate_type=[x[0],x[1]-1,x[1],x[2]],[y[0],y[1]+1,y[1],y[2]],3
            elif(rotate_type==3):
                x,y,rotate_type=[x[0],x[1]-1,x[1],x[2]],[y[0],y[1]-1,y[1],y[2]],0
        elif(block_type==3):
            if(rotate_type==0):
                x,y,rotate_type=[x[0]+1,x[1],x[2]-1,x[3]-2],[y[0]-1,y[1],y[2]-1,y[3]],1
            elif(rotate_type==1):
                x,y,rotate_type=[x[0]-1,x[1],x[2]+1,x[3]+2],[y[0]+1,y[1],y[2]+1,y[3]],0
        elif(block_type==4):
            if(rotate_type==0):
                x,y,rotate_type=[x[0]+1,x[1],x[2]+1,x[3]],[y[0]-1,y[1],y[2]+1,y[3]+2],1
            elif(rotate_type==1):
                x,y,rotate_type=[x[0]-1,x[1],x[2]-1,x[3]],[y[0]+1,y[1],y[2]-1,y[3]-2],0
        elif(block_type==5):
            if(rotate_type==0):
                x,y,rotate_type=[x[0]+1,x[1],x[2]-1,x[3]-2],[y[0]-1,y[1],y[2]+1,y[3]],1
            elif(rotate_type==1):
                x,y,rotate_type=[x[0]+1,x[1],x[2]-1,x[3]],[y[0]+1,y[1],y[2]-1,y[3]-2],2
            elif(rotate_type==2):
                x,y,rotate_type=[x[0]-1,x[1],x[2]+1,x[3]+2],[y[0]+1,y[1],y[2]-1,y[3]],3
            elif(rotate_type==3):
                x,y,rotate_type=[x[0]-1,x[1],x[2]+1,x[3]],[y[0]-1,y[1],y[2]+1,y[3]+2],0
        elif(block_type==6):
            if(rotate_type==0):
                x,y,rotate_type=[x[0]+1,x[1],x[2]-1,x[3]],[y[0]-1,y[1],y[2]+1,y[3]-2],1
            elif(rotate_type==1):
                x,y,rotate_type=[x[0]+1,x[1],x[2]-1,x[3]+2],[y[0]+1,y[1],y[2]-1,y[3]],2
            elif(rotate_type==2):
                x,y,rotate_type=[x[0]-1,x[1],x[2]+1,x[3]],[y[0]+1,y[1],y[2]-1,y[3]+2],3
            elif(rotate_type==3):
                x,y,rotate_type=[x[0]-1,x[1],x[2]+1,x[3]-2],[y[0]-1,y[1],y[2]+1,y[3]],0
    elif(event.keysym=="Down"):
        y=[y[0]+1,y[1]+1,y[2]+1,y[3]+1]
    elif(event.keysym=="Left"):
        x=[x[0]-1,x[1]-1,x[2]-1,x[3]-1]
    elif(event.keysym=="Right"):
        x=[x[0]+1,x[1]+1,x[2]+1,x[3]+1]
    if hit():
        x,y,rotate_type=tmp_x,tmp_y,tmp_r
#________________________________________________________________________________________
def block_drop():
    global x,y,block_type,rotate_type,lose,score
    y=[y[0]+1,y[1]+1,y[2]+1,y[3]+1]
    if hit():
        score=score+4
        drop['text']="Score: "+str(score)
        y=[y[0]-1,y[1]-1,y[2]-1,y[3]-1]
        if(0 in y):
            lose=True
            drop['text']="Lose!   "+"Score: "+str(score)
        (bitmap[int(y[0])][int(x[0])],
         bitmap[int(y[1])][int(x[1])],
         bitmap[int(y[2])][int(x[2])],
         bitmap[int(y[3])][int(x[3])])=True,True,True,True
        rotate_type=0
        block_type=randint(0,6)
        x=init_x[block_type]
        x,y=[x[0]+start_x,x[1]+start_x,x[2]+start_x,x[3]+start_x],init_y[block_type]
    if(lose==False):
        drop.after(drop_speed, block_drop)
#________________________________________________________________________________________
def line_delete():
    global score
    for i in range(0,height):
        if(bitmap[i].count(True)==width):
            score=score+width
            drop['text']="Score: "+str(score)
            for j in range(i,0,-1):
                bitmap[j]=bitmap[j-1]
            empty_line=[]
            for j in range(0,width):
                empty_line.append(False)
            bitmap[0]=empty_line
    if(lose==False):
        drop.after(update_speed, line_delete)
#________________________________________________________________________________________
def block_update():
    canvas.delete('block')
    for i in [0,1,2,3]:
        canvas.create_polygon(x[i]*size+x[i]-1, y[i]*size+y[i]-1,
                              (x[i]+1)*size+x[i]-1,y[i]*size+y[i]-1,
                              (x[i]+1)*size+x[i]-1,(y[i]+1)*size+y[i]-1,
                              x[i]*size+x[i]-1,(y[i]+1)*size+y[i]-1,tag='block')
    canvas.update()
    if(lose==False):
        canvas.after(100, block_update)
#________________________________________________________________________________________
def canava_update():
    canvas.delete('bitmap')
    for i in range(0,height):
        for j in range(0,width):
            if(bitmap[i][j]==True):
                canvas.create_polygon(j*size+j-1, i*size+i-1,
                                      (j+1)*size+j-1,i*size+i-1,
                                      (j+1)*size+j-1,(i+1)*size+i-1,
                                      j*size+j-1,(i+1)*size+i-1,fill='blue',tag='bitmap')
    if(lose==False):
        canvas.after(update_speed, canava_update)
#________________________________________________________________________________________
window = Tk()
window.title('Terris')

drop=Label(window,text="Score: "+str(score),anchor="e",width=40)
drop.focus_set()
drop.bind("<Key>",key)
drop.pack()
drop.after(drop_speed, block_drop)
drop.after(update_speed, line_delete)
    
canvas=Canvas(window,width=width*size+width-1, height=height*size+height-1, bg='white')
canvas.pack()
canvas.after(update_speed, block_update)
canvas.after(update_speed, canava_update)

mainloop()
