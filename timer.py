
#C:Python31python.exe
# -*- coding:utf-8 -*-
from tkinter import *

window = Tk()
window.title('Timer')

tic=0
tic_act=False
speed=1000

tic_=Label(window)
def tic_update():
    global tic,speed,tic_act
    if(tic_act==True):
        tic=tic+1
    tic_.after(speed, tic_update)
tic_.after(speed, tic_update)

def tic_active():
    global tic_act
    if(tic_act==True):
        tic_act=False
        tic_active_button['text']="Continue"
    else:
        tic_act=True
        tic_active_button['text']="Pause"
tic_active_button=Button(window,
                         text=("Start"),
                         width=10,
                         command = tic_active)

timer=Label(window,
            text="000:00:00:00:",
            justify = 'right',
            anchor = "ne")
timer_speed=100
def timer_update():
    global tic
    timer_tic=tic
    day=int(timer_tic/864000)
    hour=int(timer_tic/3600)-day*24
    minute=int(timer_tic/60)-day*1440-hour*60
    second=timer_tic-day*86400-hour*3600-minute*60
    timer['text']=str(day).rjust(3,'0')+":"+str(hour).rjust(2,'0')+":"+str(minute).rjust(2,'0')+":"+str(second).rjust(2,'0')
    timer.after(timer_speed, timer_update)
timer.after(timer_speed, timer_update)

def refresh():
    global tic
    tic=0
refresh_button=Button(window,
                      text=("Refresh"),
                      width=10,
                      command = refresh)


timer.grid(sticky=E,row=0, column=1)
tic_active_button.grid(sticky=E,row=0, column=2)
Label(window,text="Timer:").grid(sticky=E,row=0, column=0)
refresh_button.grid(sticky=E,row=1, column=2)



mainloop()














