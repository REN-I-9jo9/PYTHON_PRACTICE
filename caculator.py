#C:Python31python.exe
# -*- coding:utf-8 -*-
from tkinter import *

window = Tk()
window.title("Caculator")

Canvas(window, height=1, width=1).grid(row=0, column=1)

screenline1=""
screenline2=""

screen=Label(window, text=screenline1+"\n"+screenline2,
             width = 33,
             height = 2,
             bg = "#FFFFFF",
             justify = 'right',
             anchor = "ne")
screen.grid(sticky=E,row=1, column=1,columnspan=5)

number1=0
number2=0
def num(n):
    global number2,screenline1,screenline2
    number2=number2*10+n
    screenline2=action+" "+str(number2)
    screen.configure(text=screenline1+"\n"+screenline2)
action=""
def button(n):
    global number1,number2,action,screenline1,screenline2
    eq=""
    if(action!=""):
        eq="="
        if(action=="+"):
            number2=number1+number2
        elif(action=="-"):
            number2=number1-number2
        elif(action=="x"):
            number2=number1*number2
        elif(action=="/"):
            number2=number1/number2
            
    if(n==1):
        action="+"
    elif(n==2):
        action="-"
    elif(n==3):
        action="x"
    elif(n==4):
        action="/"
    else:
        action=""
    number1=number2
    number2=0
    screenline1=eq+" "+str(number1)
    screenline2=action+" "+str(number2)
    screen.configure(text=screenline1+"\n"+screenline2)
    if(action==""):
        number2=number1

num0=Button(window,text='0',width=5,height=2,command=lambda:num(0))
num1=Button(window,text='1',width=5,height=2,command=lambda:num(1))
num2=Button(window,text='2',width=5,height=2,command=lambda:num(2))
num3=Button(window,text='3',width=5,height=2,command=lambda:num(3))
num4=Button(window,text='4',width=5,height=2,command=lambda:num(4))
num5=Button(window,text='5',width=5,height=2,command=lambda:num(5))
num6=Button(window,text='6',width=5,height=2,command=lambda:num(6))
num7=Button(window,text='7',width=5,height=2,command=lambda:num(7))
num8=Button(window,text='8',width=5,height=2,command=lambda:num(8))
num9=Button(window,text='9',width=5,height=2,command=lambda:num(9))

but1=Button(window,text='+',width=5,height=2,command=lambda:button(1))
but2=Button(window,text='-',width=5,height=2,command=lambda:button(2))
but3=Button(window,text='x',width=5,height=2,command=lambda:button(3))
but4=Button(window,text='/',width=5,height=2,command=lambda:button(4))
but5=Button(window,text='=',width=5,height=2,command=lambda:button(5))

num0.grid(row=4,column=4)
num1.grid(row=2,column=1)
num2.grid(row=2,column=2)
num3.grid(row=2,column=3)
num4.grid(row=3,column=1)
num5.grid(row=3,column=2)
num6.grid(row=3,column=3)
num7.grid(row=4,column=1)
num8.grid(row=4,column=2)
num9.grid(row=4,column=3)
but1.grid(row=2,column=4)
but2.grid(row=2,column=5)
but3.grid(row=3,column=4)
but4.grid(row=3,column=5)
but5.grid(row=4,column=5)
        
mainloop()

