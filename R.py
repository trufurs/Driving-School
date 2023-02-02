from tkinter import *
from tkinter import Label,ttk
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
import pandas as pd


a= StringVar()
c= StringVar()
d= StringVar()

def _back(x,q,z,k):
    a.set('')
    c.set('')
    d.set('')
    x.destroy()
    globals()['F%s' % q]=Frame(k)
    z(globals()['F%s' % q])
    globals()['F%s' % q].pack()
    q+=1    


def layout(regis):
    regis.config(bg='white')
    l1 = Label(regis, text="No_plate :",bg='white')
    l1.grid(row=0,column=0,sticky=W)
    l2 = Label(regis, text="6_7AM :",bg='white')
    l2.grid(row=0,column=2,sticky=W)
    l3 = Label(regis, text="7_8AM :",bg='white')
    l3.grid(row=0,column=4,sticky=W)
    l4 = Label(regis, text="3_4PM :",bg='white')
    l4.grid(row=0,column=6,sticky=W)
    l5 = Label(regis, text="4_5PM :",bg='white')
    l5.grid(row=0,column=8,sticky=W)
    l6 = Label(regis, text="5_6PM :",bg='white')
    l6.grid(row=0,column=10,sticky=W)
    l7 = Label(regis, text="6_7PM :",bg='white')
    l7.grid(row=0,column=12,sticky=W)
    l8 = Label(regis, text="7_8PM :",bg='white')
    l8.grid(row=0,column=14,sticky=W)

def daily_routine(regis,y,z,w,k):
    try:
        y+=1
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        s = cursor.execute("select r.* from routine r,cars c where r.No_plate=c.No_plate and c.department='"+w+"' and c.availibility='Y'")
        l4 = cursor.fetchall()
        l4=pd.DataFrame(l4)
        for i in range(0, len(l4.index)):
            for j in range(0, len(l4.columns)):
                b = Entry(regis,width=15,bg='white')
                b.insert(0, l4.iloc[i][j])
                b.grid(row=i+1, column=j*2,columnspan=2,sticky=W)
                b.config(state = "readonly")
        Back = ttk.Button(regis, text="Back",command=lambda :_back(regis,y,z,k))
        Back.grid(column=(len(l4.columns)-1)*2, row=len(l4.index)+1)
        l1 = Label(regis, text='change members/drivers=',bg='white')
        l1.grid(row=i+2,column=0,columnspan=3,sticky=W)
        l11 = Entry(regis, width=20, textvariable=c)
        l11.grid(column=4, row=len(l4.index)+1,columnspan=3, sticky=W)
        
        l2 = Label(regis, text='in time slot =',bg='white')
        l2.grid(row=len(l4.index)+1,column=8,sticky=W)
        l22 = Entry(regis, width=10, textvariable=a)
        l22.grid(column=12, row=len(l4.index)+1, sticky=W)
        
        l44 = Label(regis, text='with car number plate=',bg='white')
        l44.grid(row=i+3,column=0,columnspan=3,sticky=W)
        l444 = Entry(regis, width=10, textvariable=d)
        l444.grid(column=4,row= len(l4.index)+2, sticky=W)

        def _update(x):
            try:
                conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
                cursor = conn.cursor()
                update= cursor.execute("update routine set "+a.get()+"='"+c.get()+"' where no_plate='"+d.get()+"'")
                if(cursor.rowcount>0):
                    s = cursor.execute("select r.* from routine r,cars c where r.No_plate=c.No_plate and c.department='"+w+"' and c.availibility='Y'")
                    l4 = cursor.fetchall()
                    l4=pd.DataFrame(l4)
                    for i in range(0, len(l4.index)):
                        for j in range(0, len(l4.columns)):
                            b = Entry(regis,width=15,bg='white')
                            b.insert(0, l4.iloc[i][j])
                            b.grid(row=i+1, column=j*2,columnspan=2,sticky=W)
                            b.config(state = "readonly")
                    x.pack()
                    for child in x.winfo_children():
                        child.grid_configure(padx=10, pady=10)
                    mBox.showinfo('Congrats!','ROUTINE IS UPDATED!')
                    a.set('')
                    c.set('')
                    d.set('')
                
                else:
                    mBox.showinfo('Error', z)
            except Error as e :
                mBox.showinfo('Error', e) 
            finally:
                conn.commit()

        update = ttk.Button(regis, text="Update",command=lambda:_update(regis))
        update.grid(column=(len(l4.columns)-1)*2, row=len(l4.index)+2,columnspan=2)

        
    except Error as e :
        mBox.showinfo('Error', e)       
    finally:
        conn.commit()

    
