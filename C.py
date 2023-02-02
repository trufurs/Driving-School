from tkinter import *
from tkinter import Label , ttk
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
import pandas as pd
a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()
f = StringVar()
g = StringVar()
h = StringVar()
def _back(x,y,q,k):
    a.set('')
    b.set('')
    c.set('')
    d.set('')
    e.set('')
    f.set('')
    g.set('')
    h.set('')
    x.destroy()
    globals()['F%s' % q]=Frame(k)
    y(globals()['F%s' % q])
    globals()['F%s' % q].pack()
    q+=1  
def _cars(t):
    t.config(bg='white')
    l1 = Label(t, text="Number plate :",bg='white')
    l1.grid(row=1,column=1,sticky=W)
    l2 = Label(t, text="Company :",bg='white')
    l2.grid(row=2,column=1,sticky=W)
    l3 = Label(t, text="Model :",bg='white')
    l3.grid(row=3,column=1,sticky=W)
    l4 = Label(t, text="Department :",bg='white')
    l4.grid(row=5,column=1,sticky=W)
    l5 = Label(t, text="Feul Type :",bg='white')
    l5.grid(row=4,column=1,sticky=W)
    l6 = Label(t, text="PUC :",bg='white')
    l6.grid(row=6,column=1,sticky=W)
    l7 = Label(t, text="Insurance :",bg='white')
    l7.grid(row=7,column=1,sticky=W)
    l8 = Label(t, text="Avalibility :",bg='white')
    l8.grid(row=8,column=1,sticky=W)
    C=Entry(t, width=20, textvariable=a)
    C.grid(row=1,column=2,sticky=W)
    D=Entry(t, width=20, textvariable=b)
    D.grid(row=2,column=2,sticky=W)
    E=Entry(t, width=20, textvariable=c)
    E.grid(row=3,column=2,sticky=W)
    d.set('g')
    F1= Radiobutton(t, text='Regular', variable=d, value='Normal',bg='white')
    F1.grid(row=5,column=2,sticky=W)
    F2= Radiobutton(t, text='Premium', variable=d, value='Premium',bg='white')
    e.set('g')
    F2.grid(row=5,column=3,sticky=W)
    G1= Radiobutton(t, text='Desiel', variable=e, value='Desiel',bg='white')
    G1.grid(row=4,column=2,sticky=W)
    G2= Radiobutton(t, text='Feul', variable=e, value='Feul',bg='white')
    G2.grid(row=4,column=3,sticky=W)
    G3= Radiobutton(t, text='Electric', variable=e, value='Electric',bg='white')
    G3.grid(row=4,column=4,sticky=W)
    f.set('g')
    H1= Radiobutton(t, text='Yes', variable=f, value='Y',bg='white')
    H1.grid(row=6,column=2,sticky=W)
    H2= Radiobutton(t, text='No', variable=f, value='N',bg='white')
    H2.grid(row=6,column=3,sticky=W)
    g.set('g')
    I1= Radiobutton(t, text='Yes', variable=g, value='Y',bg='white')
    I1.grid(row=7,column=2,sticky=W)
    I2= Radiobutton(t, text='No', variable=g, value='N',bg='white')
    h.set('g')
    I2.grid(row=7,column=3,sticky=W)
    J1= Radiobutton(t, text='Yes', variable=h, value='Y',bg='white')
    J1.grid(row=8,column=2,sticky=W)
    J2= Radiobutton(t, text='No', variable=h, value='N',bg='white')
    J2.grid(row=8,column=3,sticky=W)
    for child in t.winfo_children():
    	child.grid_configure(padx=20, pady=20)
def _cshow(regis,y,module,k):
    y+=1
    regis.config(bg='white')
    l1 = Label(regis, text="Number plate :",bg='white')
    l1.grid(row=0,column=0,sticky=W)
    l2 = Label(regis, text="Company :",bg='white')
    l2.grid(row=0,column=1,sticky=W)
    l3 = Label(regis, text="Model :",bg='white')
    l3.grid(row=0,column=2,sticky=W)
    l4 = Label(regis, text="Department :",bg='white')
    l4.grid(row=0,column=3,sticky=W)
    l5 = Label(regis, text="Feul Type :",bg='white')
    l5.grid(row=0,column=4,sticky=W)
    l6 = Label(regis, text="PUC :",bg='white')
    l6.grid(row=0,column=5,sticky=W)
    l7 = Label(regis, text="Insurance :",bg='white')
    l7.grid(row=0,column=6,sticky=W)
    l8 = Label(regis, text="Avalibility :",bg='white')
    l8.grid(row=0,column=7,sticky=W)
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("select * from cars")
        ls = cursor.fetchall()
        ls=pd.DataFrame(ls)
        for i in range(0, len(ls.index)):
            for j in range(0, len(ls.columns)):
                b = Entry(regis,width=15)
                b.insert(0, ls.iloc[i][j])
                b.grid(row=i+1, column=j)
                b.config(state = "readonly")
        Back = ttk.Button(regis, text="Back", command=lambda :_back(regis,module,y,k))
        Back.grid(column=0, row=len(ls.index)+1,columnspan=2)
    except Error as e :
        mBox.showinfo('Error', e)
    finally:
        print("MySQL connection is closed")
        conn.commit()
def _cinsert():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("insert into cars values('"+a.get()+"', '"+b.get()+"', '"+c.get()+"', '"+d.get()+"', '"+e.get()+"', '"+f.get()+"', '"+g.get()+"', '"+h.get()+"')")
        rout= cursor.execute("insert into routine values('"+a.get()+"','','','','','','','')")
        if(cursor.rowcount>0):
            mBox.showinfo('Congrats!')
            a.set('')
            b.set('')
            c.set('')
            d.set('')
            e.set('')
            f.set('')
            g.set('')
            h.set('')
        else:
            mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
def _cfill():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from cars where no_plate='"+a.get()+"'")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            a.set(ls.iloc[0][0])
            b.set(ls.iloc[0][1])
            c.set(ls.iloc[0][2])
            d.set(ls.iloc[0][3])
            e.set(ls.iloc[0][4])
            f.set(ls.iloc[0][5])
            g.set(ls.iloc[0][6])
            h.set(ls.iloc[0][7])        
        else:
            mBox.showinfo('!....IIIISH....!', 'Not Found')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
def _cdelete():
    try:
     conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("delete from cars where no_plate='"+a.get()+"'")
     rout= cursor.execute("delete from routine where no_plate='"+a.get()+"'")
     if(cursor.rowcount>0):
         mBox.showinfo('Done!', 'Deleted!')
         a.set('')
         b.set('')
         c.set('')
         d.set('')
         e.set('')
         f.set('')
         g.set('')
         h.set('')
     else:
         mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
     mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
def _cupdate():
    try:
     conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("update cars set company='"+b.get()+"',model='"+c.get()+"',department='"+d.get()+"',feul_type='"+e.get()+"',puc='"+f.get()+"',insurance='"+g.get()+"',availibility='"+h.get()+"' where no_plate='"+a.get()+"'")
     if(cursor.rowcount>0):
         mBox.showinfo('Done!', 'Updated!')
         a.set('')
         b.set('')
         c.set('')
         d.set('')
         e.set('')
         f.set('')
         g.set('')
         h.set('')
     else:
         mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
     mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
