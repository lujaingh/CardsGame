#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Write Your Program Here ###
import random
import tkinter.messagebox  
from tkinter import *

listmachine,listplayer,listground=[],[],[]

dictionaryCards={'1':1,'2':2,'3':3,
                 '4':4,'5':5,'6':6,
                 '7':7,'8':8,'9':9,
                 '10':10,'J':11,             
                 'Q':12 ,'K':13}

fsitch=True
def switch():

    swapmachine()
            


            
            
    
flagu=True
def done():
    global flagu
    print("donef")
    flagu=False
    clearg()
    swapmachine()

    
    
def swapfunc():
    print(type(card1.get()))
    c1=card1.get()
    c2=card2.get()
    t1=0
    t2=0
    global flagu
    if  len(c1)>0:
        print("1111111111")
        if c1 =='K':
            t1=13
        elif c1 =='Q':
            t1=12
        elif c1 =='J':
            t1=11
        else:
            t1=int(c1)

        if c2 =='K':
            t2=13
        elif c2 =='Q':
            t2=12
        elif c2 =='J':
            t2=11
        else:
            t2=int(c2)
                    
        


        temp = t1
        listground[listground.index(t2)]=temp
        listplayer[listplayer.index(t1)]=t2
        setbuttonsuser(listplayer)
        setbuttonsground(listground)

        print(f"temp: {temp}")
        print(f"t1: {t1}")
        print(f"t2: {t2}") 
        flagu=True
        
 



    
    
    
def setbuttons():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b12,b13,b14,b15,b16,card1,card2,p1,p2
     
    p1 = StringVar()
    p2 = StringVar()
    
    card1 = Entry(tk, textvariable=p1, bd=5,width=30,fg="steelblue")##cards to swap
    card1.grid(row=1, column=1, columnspan=8 )
    card2 = Entry(tk, textvariable=p2, bd=5,width=30,fg="steelblue")
    card2.grid(row=2, column=1, columnspan=8)
    
    
    b1 = Button(tk , text=" " , font=("Merlin",20),height=2,width=5,bg="pink",fg="palevioletred")
    b2 = Button(tk , text=" " , font=("Merlin",20),height=2,width=5,bg="pink",fg="palevioletred")
    b3 = Button(tk , text=" " , font=("Merlin",20),height=2,width=5,bg="pink",fg="palevioletred")
    b4 = Button(tk , text=" " , font=("Merlin",20),height=2,width=5,bg="pink",fg="palevioletred")
    
    b5 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="skyblue",fg="royalblue")
    b6 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="skyblue",fg="royalblue")
    b7 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="skyblue",fg="royalblue")
    b8 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="skyblue",fg="royalblue")
    
    b9 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="aquamarine",fg="teal")
    b10 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="aquamarine",fg="teal")
    b12 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="aquamarine",fg="teal")
    b13 = Button(tk , text=" " , font=("Merlin",20),height=3,width=4,bg="aquamarine",fg="teal")
    
    b14 = Button(tk , text="swap" , font=("Merlin",8),height=2,width=5,bg="palevioletred",fg="white",command=lambda:swapfunc())
    b15 = Button(tk , text="pass" , font=("Merlin",8),height=2,width=5,bg="palevioletred",fg="white",command=lambda:done())
    b16 = Button(tk , text="start" , font=("Merlin",8),height=2,width=5,bg="palevioletred",fg="white",command=lambda:switch())

    b1.grid(row=7, column=1)##machine
    b2.grid(row=8, column=1)
    b3.grid(row=9, column=1)
    b4.grid(row=10, column=1)
    
    b5.grid(row=11, column=3)##user
    b6.grid(row=11, column=4)
    b7.grid(row=11, column=5)
    b8.grid(row=11, column=6)
    
    b9.grid(row=6, column=3)##ground
    b10.grid(row=6, column=4)
    b12.grid(row=6, column=5)
    b13.grid(row=6, column=6)
    
    b14.grid(row=1, column=1)#swap and done
    b15.grid(row=2, column=1)    
    b16.grid(row=3, column=1)  
    disableswap()
######################
randomGroundDeck=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10
                 ,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]    
def generaterandomGround(lr):   
    for i in range(0,4):
        random_number = random.choice(randomGroundDeck)
        print('randgen: ',random_number)
        lr.append(random_number)
        randomGroundDeck.remove(random_number)
        print(randomGroundDeck," deckrand")
        
    return lr
    

def generaterandom(lr):
    global listmachine,listplayer,listground
    for i in range(0,4):
        random_number = int(random.randint(1, 13))##to generate random index
        print('rand: ',random_number)
        lr.append(random_number)
        randomGroundDeck.remove(random_number)
    return lr
    
##############
flag11=False    
def swapmachine(card=""):
    flag11=False
    
    item=0
    maxcount=0
    count=0
    listcounts=[]
    for i in listground:
        if flag11:
            break
        for j in listmachine:
            if flag11:
                break
            if i==j:
                print("i==j")
                print(i," ",j)
                item=i
                count=listmachine.count(i)
                maxcount=count
                
                for k in listmachine:
                    if maxcount<listmachine.count(k):
                        maxcount=listmachine.count(k)
                if count==1 and maxcount<=1:                       
                    for i in listground:
                        print("swapm1")
                        if flag11:
                            break
                        for j in listmachine:
                            if i!=j and i==item:  
                                temp = i
                                listground[listground.index(i)]=j
                                listmachine[listmachine.index(j)]=temp

                                print(f"temp m: {temp}")
                                print(f"cardg m: {i}")
                                print(f"card m: {j}")
                                #setbuttonsmachine(listmachine)
                                setbuttonsground(listground)
                                flag11=True
                                break 
                                
                if count ==2 and maxcount<=2:
                    for i in listground:
                        print("swapm1")
                        if flag11:
                            break
                        for j in listmachine:
                            if i!=j and i==item:  
                                temp = i
                                listground[listground.index(i)]=j
                                listmachine[listmachine.index(j)]=temp

                                print(f"temp m: {temp}")
                                print(f"cardg m: {i}")
                                print(f"card m: {j}")
                                #setbuttonsmachine(listmachine)
                                setbuttonsground(listground)
                                flag11=True
                                break 
                
                if maxcount ==3 and count==3:
                
                    for i in listground:
                        print("swapm1")
                        if flag11:
                            break
                        for j in listmachine:
                            if i!=j and i==item:  
                                temp = i
                                listground[listground.index(i)]=j
                                listmachine[listmachine.index(j)]=temp

                                print(f"temp m: {temp}")
                                print(f"cardg m: {i}")
                                print(f"card m: {j}")
                                setbuttonsmachine(listmachine)
                                setbuttonsground(listground)
                                flag11=True
                                break                 
    enableswap()
    disablemach()
    winorlose()
    
    
##################
def setbuttonsuser(np):
    t=0
    lp=[]
    for i in np:
        t=i
        if i==11:
            t='J'
        elif i==12:
            t='Q'
        elif i==13:
            t='K'
            
        lp.append(t)
            
    b5["text"] = lp[0]
    b6["text"] = lp[1]    
    b7["text"] = lp[2]    
    b8["text"] = lp[3]
    
def setbuttonsground(np):
    t=0
    lp=[]
    for i in np:
        t=i
        if i==11:
            t='J'
        elif i==12:
            t='Q'
        if i==13:
            t='K'
            
        lp.append(t)
    b9["text"] = lp[0]
    b10["text"] = lp[1]    
    b12["text"] = lp[2]    
    b13["text"] = lp[3]
    
def setbuttonsmachine(np):
    t=0
    lp=[]
    for i in np:
        t=i
        if i==11:
            t='J'
        elif i==12:
            t='Q'
        elif i==13:
            t='K'
            
        lp.append(t)
        
    b1["text"] = lp[0] #Hidden from user
    b2["text"] = lp[1]    
    b3["text"] = lp[2]    
    b4["text"] = lp[3]
    
    
def disableswap():
    b14["state"] = DISABLED
def disablemach():
    b16["state"] = DISABLED
def enableswap():
    b14["state"] = NORMAL    
def enablesmach():
    b16["state"] = NORMAL 
    
    
def clearg():
    listground.clear()
    generaterandomGround(listground)
    setbuttonsground(listground)
    winorlose()
    
def winorlose():    
    f1=all(i==listmachine[0] for i in listmachine) 
    f2=all(i==listplayer[0] for i in listplayer)
    print(f1)
    print(f2)
    if len(randomGroundDeck)>=0 and f1==True:
        setbuttonsmachine(listmachine)
        messagebox.showinfo(message="You lose") 
    elif len(randomGroundDeck)>=0 and f2==True:
        messagebox.showinfo(message="You Win") 
        
        
    if len(randomGroundDeck)==0 and f1==False:
        messagebox.showinfo(message="Finish")        
    elif len(randomGroundDeck)==0 and f2==False:
        messagebox.showinfo(message="Finish")    
    
    
tk = Tk()
tk.title("Lujain's Cards Game")
#tk.geometry("600x400")
tk.resizable(True, True)
tk.config(bg="lavenderblush")

name1L = Label( tk, text="Ground", font="Merlin 15 bold", bg='lavenderblush', fg='teal', height=1, width=10)
name1L.grid(row=6, column=2)
name2L = Label( tk, text="Machine", font="Merlin 15 bold", bg='lavenderblush', fg='palevioletred', height=1, width=10)
name2L.grid(row=6, column=1)
areyouL = Label( tk, text="You", font="Merlin 15 bold", bg='lavenderblush', fg='royalblue', height=2, width=10)
areyouL.grid(row=11, column=2)

 
setbuttons()

tk.update()




"""Hello, The counting machine,This cards game,you will have 4 cards and also machine will, there is 4 cards on the ground they changed every round
the machine will start playing click start, when your turn you can swap  from cards, first entry write your card in second one write card from ground then click swap.then finish swapping,
,click done to finish swapping,the winner will have four same cards,if you do not want to swap just write pass in first  entry, have fun:)
enjoy it the max"""
messagebox.showinfo(message="""Hello, The counting machine,This cards game,you will have 4 cards and also machine will, there is 4 cards on the ground they changed every round
the machine will start playing click start, when your turn you can swap  from cards, first entry write your card in second one write card from ground then click swap.then finish swapping,
,click done to finish swapping,the winner will have four same cards,if you do not want to swap just write pass in first  entry, have fun:)
enjoy it the max""")
print(__doc__)    

    
    
    

win=False
listplayer=[]
global listuserOrMachine
listuserOrMachine = ["machine","user"]
listkqj=['J','Q','K']

generaterandom(listplayer)
print(listplayer, "listplayer")
setbuttonsuser(listplayer)


generaterandom(listmachine)
print(listmachine, "listmachine")
#setbuttonsmachine(listmachine)

generaterandomGround(listground)
print(listground, "listg")
setbuttonsground(listground)



t1=0
t2=0
check=False
itemi=0
itemj=0

    
tk.mainloop()

