from tkinter import*
from PIL import Image, ImageTk
import math
from os import path

fenetre = Tk()
fenetre.title('Clock')
fenetre.configure(background='black')

def get_file(name):
    return path.join(path.dirname(path.realpath(__file__)), name)

img= ImageTk.PhotoImage(Image.open(get_file("bg.png")))
imgStart= ImageTk.PhotoImage(Image.open(get_file("button start.png")))
imgReset= ImageTk.PhotoImage(Image.open(get_file("button reset.png")))
imgStime= ImageTk.PhotoImage(Image.open(get_file("button stime.png")))
imgSalarm= ImageTk.PhotoImage(Image.open(get_file("button salarm.png")))
imgConfirm= ImageTk.PhotoImage(Image.open(get_file("button confirm.png")))
imgCStime= ImageTk.PhotoImage(Image.open(get_file("button confirm stime.png")))
imgCSalarm= ImageTk.PhotoImage(Image.open(get_file("button confirm salarm.png")))
imgWakeUp= ImageTk.PhotoImage(Image.open(get_file("button wake up.png")))

btn1=0
btnreveil=0
btntime=0
def refresh():
    clock.zone.delete("all")
    canvas.create_rectangle(0,105 , 726,431, fill='black', outline='black')
    add=0
    for i in range(3):
        for i in range(2):
            canvas.create_rectangle(8+add,113 , 8+add+100,293, fill=('#303030'), outline=('#303030'))
            add+=110
        add+=30
    canvas.create_image(0,0,anchor=NW,image=img)
    clock.image()
    clock.heure()

def btnstartstop():
    global btn1
    if btn1==0:
        btn1=1
        start()

    else:
        btn1=0
        stop()

def start():
    global id
    time.avance()
    if time.verif_reveil()==True:
        clock.confirm_alarm()
    id = fenetre.after(1000,start)
    refresh()


def stop():
    fenetre.after_cancel(id)

def reset():
    time.resetage()
    refresh()

class Time():

    def __init__(self,h=0,m=0,s=0,reveil=[0,0,3]):
        self.h=h
        self.m=m
        self.s=s
        self.reveil=reveil

    def __str__(self):
        return f'{self.h}h {self.m}m {self.s}s'

    def avance(self):
        self.s+=1
        if self.s>=60:
            self.s=0
            self.m+=1
            if self.m>=60:
                self.m=0
                self.h+=1
            if self.h>23:
                self.h=0

    def resetage(self):
        self.h=0
        self.m=0
        self.s=0

    def verif_reveil(self):
        if self.h==self.reveil[0] and self.m==self.reveil[1] and self.s==self.reveil[2]:
            return True
        else:
            return False

    def set_alarm(self):
        global btnreveil
        global text_alarm
        if btnreveil==0:
            text_alarm = Entry(fenetre, bg = 'pink', font=('Helvetica', 16, 'bold'))
            text_alarm.grid(column=0, row=1)
            btnreveil=1
            btn_alarm.config(image=imgCSalarm)
        else:
            L=text_alarm.get().split(":")
            for i in range(len(L)):
                self.reveil[i]=int(L[i])
            if self.reveil[0] > 23:
                self.reveil[0]=23
            if self.reveil[1] > 59:
                self.reveil[1]=59
            if self.reveil[2] > 59:
                self.reveil[2]=59
            print(self.reveil)
            text_alarm.grid_forget()
            btnreveil=0
            btn_alarm.config(image=imgSalarm)

    def set_time(self):
        global btntime
        global text_time
        if btntime==0:
            text_time = Entry(fenetre, bg = 'light sky blue', font=('Helvetica', 16, 'bold'))
            text_time.grid(column=1, row=1)
            btntime=1
            btn_time.config(image=imgCStime)
        else:
            L=text_time.get().split(":")
            self.h=int(L[0])
            self.m=int(L[1])
            self.s=int(L[2])
            if self.h > 23:
                self.h=23
            if self.m > 59:
                self.m=59
            if self.s > 59:
                self.s=59
            text_time.grid_forget()
            btntime=0
            btn_time.config(image=imgStime)
            refresh()


class Clock():

    def __init__(self,time,zone,color='white',outline='white'):
        self.zone=zone
        self.time=time
        self.color=color
        self.outline=outline


    def zero(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,20+114 , x+20,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+20,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,20+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def un(self,x):
        self.zone.create_rectangle(x+80,0+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def deux(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,80+114 , x+20,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,20+114 , x+100,100+114, fill=self.color, outline=self.outline)

    def trois(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,20+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def quatre(self,x):
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,0+114 , x+20,100+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,0+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def cinq(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,20+114 , x+20,100+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def six(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,0+114 , x+20,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+20,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def sept(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,20+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def huit(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,20+114 , x+20,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+20,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,20+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def neuf(self,x):
        self.zone.create_rectangle(x,0+114 , x+100,20+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,80+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,160+114 , x+100,180+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x,20+114 , x+20,100+114, fill=self.color, outline=self.outline)

        self.zone.create_rectangle(x+80,20+114 , x+100,100+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x+80,80+114 , x+100,180+114, fill=self.color, outline=self.outline)

    def slash(self,x):
        self.zone.create_rectangle(x,60+114 , x+20,80+114, fill=self.color, outline=self.outline)
        self.zone.create_rectangle(x,100+114 , x+20,120+114, fill=self.color, outline=self.outline)

    def chiffre(self,c,x):
        if c==0:
            self.zero(x)
        if c==1:
            self.un(x)
        if c==2:
            self.deux(x)
        if c==3:
            self.trois(x)
        if c==4:
            self.quatre(x)
        if c==5:
            self.cinq(x)
        if c==6:
            self.six(x)
        if c==7:
            self.sept(x)
        if c==8:
            self.huit(x)
        if c==9:
            self.neuf(x)

    def heure(self):
        if time.h<10:
            clock.chiffre(0,8)
            clock.chiffre(time.h,118)
        else:
            clock.chiffre(time.h//10,8)
            clock.chiffre(time.h%10,118)
        clock.slash(228)
        if time.m<10:
            clock.chiffre(0,258)
            clock.chiffre(time.m,368)
        else:
            clock.chiffre(time.m//10,258)
            clock.chiffre(time.m%10,368)
        clock.slash(478)
        if time.s<10:
            clock.chiffre(0,508)
            clock.chiffre(time.s,618)
        else:
            clock.chiffre(time.s//10,508)
            clock.chiffre(time.s%10,618)

    def image(self):
        self.zone.grid(columnspan=2,row=0)


    def btnstart(self):
        btn_start = Button(self.zone, image=imgStart, command=btnstartstop, font=('Calibri', 48, 'bold'), borderwidth=0)
        btn_start.place(x=166,y=302)

    def btnreset(self):
        btn_reset = Button(self.zone, image=imgReset, command=reset, font=('Calibri', 48, 'bold'), borderwidth=0)
        btn_reset.place(x=394,y=303)

    def btnalarm(self):
        global btn_alarm
        btn_alarm = Button(self.zone, image=imgSalarm, command=time.set_alarm, font=('Calibri', 48, 'bold'), borderwidth=0)
        btn_alarm.place(x=166,y=362)

    def btntime(self):
        global btn_time
        btn_time = Button(self.zone, image=imgStime, command=time.set_time, font=('Calibri', 48, 'bold'), borderwidth=0)
        btn_time.place(x=394,y=362)

    def confirm_alarm(self):
        btn_stopréveil = Button(self.zone, image=imgWakeUp, command=lambda: btn_stopréveil.place_forget(), borderwidth=0)
        btn_stopréveil.place(x=196,y=145)


time = Time()
canvas = Canvas(fenetre, width='726',height='431',bg='white', highlightthickness=0)
clock=Clock(time,canvas)
refresh()
clock.btnstart()
clock.btnreset()
clock.btnalarm()
clock.btntime()



mainloop()