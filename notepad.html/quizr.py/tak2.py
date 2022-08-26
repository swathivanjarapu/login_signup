from tkinter import*

mw=Tk()
mw.title("calculator")
# mw.geometry("354*460")
# mwlabel=Label(mw,text="calculator",bg="dark gray",front=("Times",30,"bold"))
# mwlabel.pack(side=TOP)
# mw.config(background='dark gray')

textin=StringVar()
operater=""


def clickbut(number):
    global operater
    operater=operater+str(number)
    textin.set(operater)
    
def equlbut():
    global operater
    add=str(eval(operater))
    textin.set(add)
    operater=""
    
def equlbut():
    global operater
    sub=str(eval(operater))
    textin.set(sub)
    operater=""
    
def equlbut():
    global operater
    mul=str(eval(operater))
    textin.set(mul)
    operater=""
    
def equlbut():
    global operater
    div=str(eval(operater))
    textin.set(div)
    operater=""
    
def clrbut():
    textin.set("")


mwtext=Entry(mw,font=("courier new",12,"bold"),textvar=textin,width=25,bd=5,bg="powder blue")
mwtext.grid(row=0,columnspan=4)

but1=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(1),text="1",font=("(courier new",16,"bold"))
but1.place(x=10,y=100)
but2=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(2),text="2",font=("(courier new",16,"bold"))
but2.place(x=10,y=170)
but3=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(3),text="3",font=("courier new",16,"bold"))
but3.place(x=10,y=240)
but4=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(4),text="4",font=("(courier new",16,"bold"))
but4.place(x=75,y=100)
but5=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(5),text="5",font=("(courier new",16,"bold"))
but5.place(x=75,y=170)
but6=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(6),text="6",font=("(courier new",16,"bold"))
but6.place(x=75,y=240)
but7=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(7),text="7",font=("(courier new",16,"bold"))
but7.place(x=140,y=100)
but8=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(8),text="8",font=("(courier new",16,"bold"))
but8.place(x=140,y=170)
but9=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(9),text="9",font=("(courier new",16,"bold"))
but9.place(x=140,y=240)
but0=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(0),text="0",font=("(courier new",16,"bold"))
but0.place(x=10,y=310)
butdot=Button(mw,padx=47,pady=14,bd=4,bg="white",command=lambda:clickbut("."),text=".",font=("(courier new",16,"bold"))
butdot.place(x=75,y=310)
butpl=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut("+"),text="+",font=("(courier new",16,"bold"))
butpl.place(x=205,y=100)
butsub=Button(mw,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut("-"),text="-",font=("(courier new",16,"bold"))
butsub.place(x=205,y=170)
butml=Button(mw,padx=14,pady=14,bd=4,bg="white",text="*",command=lambda:clickbut("*"),font=("(courier now",16,"bold"))
butml.place(x=205,y=240)
butdiv=Button(mw,padx=14,pady=14,bd=4,bg="white",text="/",command=lambda:clickbut("/"),font=("(courier new",16,"bold"))
butdiv.place(x=205,y=310)
butclear=Button(mw,padx=14,pady=119,bd=4,bg="white",text="CE",command=clrbut,font=("(courier now",16,"bold"))
butclear.place(x=270,y=110)
butequal=Button(mw,padx=151,pady=14,bd=4,bg="white",command=equlbut,text="=",font=("(courier now",16,"bold"))
butequal.place(x=10,y=380)


mw.mainloop()
