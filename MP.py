import io
import base64
import tkinter as tk
from tkinter import *
import pandas as pd
from tkinter import ttk,Label
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageDraw, ImageTk, ImageFont

log = tk.Tk() 	
log.title("Driving School")
g1=Frame(log)
g1.pack()
g=Frame(log)



def _login(mlog):
    mlog.pack()
    def EmsgBox():
        mBox.showinfo('Error', usr.get()+'\nInvalid Login Id or Password')
        usr.set('')
        pas.set('')

    def SmsgBox():
        mBox.showinfo('Welcome', usr.get())
        usr.set('')
        pas.set('')


    def fin(event):
        if(event.widget==usrw and usr.get()== 'Enter Login ID'):
            usrw.configure(foreground='black')
            usr.set('')
        elif(event.widget==pasw and pas.get()== 'Enter Password'):
            pasw.configure(foreground='black', show='•')
            pas.set('')

    def fout(event):
        if(event.widget==usrw):
            if(len(usr.get())==0):
                usrw.configure(foreground='red')
                usr.set('Enter Login ID')
        elif(event.widget==pasw):
            if(len(pas.get())==0):
                pasw.configure(foreground='red', show='')
                pas.set('Enter Password')

    text_x1 = 55
    text_y1= 45

    text_x2 = 55 + 140
    text_y2 = 45

    text_x3 = 55
    text_y3= 45 + 45




    text1 = "User ID"

    text2 = "Password"

    entry_pady = 7

    image = Image.open("aaaa.png")
    image=image.resize((1000,650),1)

    w, h = image.size

    log.geometry("%sx%s"%(w, h))

    draw = ImageDraw.Draw(image)

    width_text, height_text = draw.textsize(text1)


    photoimage = ImageTk.PhotoImage(image)
    B=Label(mlog, image=photoimage)
    B.place(x=0,y=0)
    B.pack()
    photoimage1 =   PhotoImage(file="Webp.net-resizeimage (3).png")

    usr = tk.StringVar()
    usrw=ttk.Entry(mlog, background="white", textvariable=usr)
    usrw.place(x=text_x1-3, y=text_y1+ height_text +7)

    pas = tk.StringVar()
    pasw=ttk.Entry(mlog,background= "white", textvariable=pas , show='*')
    pasw.place(x=text_x2-6, y=text_y2 + height_text +7)

    usrw.bind('<FocusIn>', fin)
    usrw.bind('<FocusOut>', fout)
    usrw.bind('<Enter>', fin)
    usrw.bind('<Leave>', fout)

    pasw.bind('<FocusIn>', fin)
    pasw.bind('<FocusOut>', fout)
    pasw.bind('<Enter>', fin)
    pasw.bind('<Leave>', fout)

    def _msgBox():
        try:
         
             conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
             cursor = conn.cursor()
             cursor.execute("select login_id,password from mlogin where login_id='"+usr.get()+"' and password='"+pas.get()+"'")
             ls = pd.DataFrame(cursor.fetchall())
             if (len(ls.index)>0):
                 SmsgBox()
                 
             else:
                 EmsgBox()
         
        except Error as e :
            print()
        finally:
            conn.commit()
            
    action = Button(mlog, image=photoimage1, command=_msgBox,border=0)
    action.place(x=text_x3,y=text_y3)
    mlog.mainloop()

def _go(x,y,z):
    x.pack_forget()
    z(y)
    
    
    

def _d(g,g1):
    g.pack_forget()
    g1.pack()


_go(g1,g,_login)
    

