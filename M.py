from tkinter import *
from tkinter import Label,ttk
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
import pandas as pd
a = StringVar()
b= StringVar()
c= StringVar()
d= StringVar()
e= StringVar()
f= StringVar()
g= StringVar()
h= StringVar()
i= StringVar()
j= StringVar()
k= StringVar()
def _back(x,y,q,w):
    x.pack_forget()
    a.set('')
    b.set('')
    c.set('')
    d.set('')
    e.set('')
    f.set('')
    g.set('')
    h.set('')
    i.set('')
    j.set('')
    k.set('')
    x.destroy()
    globals()['F%s' % q]=Frame(w)
    y(globals()['F%s' % q])
    globals()['F%s' % q].pack()
    q+=1
def _members(x):
    x.config(bg='white')
    l1 = Label(x, text="Member ID :",bg='white')
    l1.grid(row=1,column=1, sticky=W)
    l2 = Label(x, text="Name :",bg='white')
    l2.grid(row=1,column=3, sticky=W)
    l3 = Label(x, text="Gender :",bg='white')
    l3.grid(row=2,column=1, sticky=W)
    l4 = Label(x, text="Date of Birth :",bg='white')
    l4.grid(row=3,column=1, sticky=W)
    l5 = Label(x, text="Mobile Number :",bg='white')
    l5.grid(row=3,column=3, sticky=W)
    l11 = Label(x, text="Department :",bg='white')
    l11.grid(row=4,column=1, sticky=W)
    l6 = Label(x, text="Aadhar Number :",bg='white')
    l6.grid(row=6,column=1, sticky=W)
    l7 = Label(x, text="Address :",bg='white')
    l7.grid(row=5,column=1, sticky=W)
    l8 = Label(x, text="Date of joining :",bg='white')
    l8.grid(row=6,column=3, sticky=W)
    l9 = Label(x, text="Fees Paid :",bg='white')
    l9.grid(row=7,column=1, sticky=W)
    l10 = Label(x, text="Fees Delay :",bg='white')
    l10.grid(row=7,column=3, sticky=W)
    A=Entry(x, width=20, textvariable=a)
    A.grid(row=1,column=2, sticky=W)
    B=Entry(x, width=20, textvariable=b)
    B.grid(row=1,column=4, sticky=W)
    c.set('g')
    male = Radiobutton(x, text='Male', variable=c, value='M',bg='white')
    male.grid(column=2, row=2, sticky=W)
    female=Radiobutton(x, text='Female', variable=c, value='F',bg='white')
    female.grid(column=3, row=2, sticky=W)
    D=Entry(x, width=20, textvariable=d)
    D.grid(row=3,column=2)
    E=Entry(x, width=20, textvariable=e)
    E.grid(row=3,column=4, sticky=W)
    f.set('g')
    J1= Radiobutton(x, text='Normal', variable=f, value='Normal',bg='white')
    J1.grid(row=4,column=2, sticky=W)
    J2= Radiobutton(x, text='Premium', variable=f, value='Premium',bg='white')
    J2.grid(row=4,column=3, sticky=W)
    G=Entry(x, width=20, textvariable=g)
    G.grid(row=6,column=2, sticky=W)
    H=Entry(x, width=71, textvariable=h)
    H.grid(row=5,column=2 ,columnspan=3, sticky=W)
    I=Entry(x, width=20, textvariable=i)
    I.grid(row=6,column=4, sticky=W)
    J=Entry(x, width=20, textvariable=j)
    J.grid(row=7,column=2, sticky=W)
    K=Entry(x, width=20, textvariable=k)
    K.grid(row=7,column=4, sticky=W)
    for child in x.winfo_children():
        child.grid_configure(padx=20, pady=20)
def _minsert():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("insert into members values('"+a.get()+"', '"+b.get()+"', '"+c.get()+"', '"+d.get()+"', '"+e.get()+"', '"+f.get()+"', '"+g.get()+"', '"+h.get()+"', '"+i.get()+"', '"+j.get()+"', '"+k.get()+"')")
        print(cursor.rowcount)
        if(cursor.rowcount>0):
            mBox.showinfo('Congrats!','Done!')
            a.set('')
            b.set('')
            c.set('')
            d.set('')
            e.set('')
            f.set('')
            g.set('')
            h.set('')
            i.set('')
            j.set('')
            k.set('')
        else:
            mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
def _mshow(regis,y,module,w):
    regis.config(bg='white')
    y+=1
    l1 = Label(regis, text="|Member ID|")
    l1.grid(row=0,column=1)
    l2 = Label(regis, text="|Name|")
    l2.grid(row=0,column=2)
    l3 = Label(regis, text="|Gender|")
    l3.grid(row=0,column=3)
    l4 = Label(regis, text="|Date of Birth|")
    l4.grid(row=0,column=4)
    l5 = Label(regis, text="|Mobile Number|")
    l5.grid(row=0,column=5)
    l11 = Label(regis, text="|Department|")
    l11.grid(row=0,column=6)
    l6 = Label(regis, text="|Aadhar Number|")
    l6.grid(row=0,column=7)
    l7 = Label(regis, text="|Address|")
    l7.grid(row=0,column=8)
    l8 = Label(regis, text="|Date of joining|")
    l8.grid(row=0,column=9)
    l9 = Label(regis, text="|Fees Paid|")
    l9.grid(row=0,column=10)
    l10 = Label(regis, text="|Fees Delay|")
    l10.grid(row=0,column=11)
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("select * from members")
        ls = cursor.fetchall()
        ls=pd.DataFrame(ls)
        for o in range(0, len(ls.index)):
            for j in range(0, len(ls.columns)):
                d = Entry(regis,width=10,bg='white')
                d.insert(0, ls.iloc[o][j])
                d.grid(row=o+1, column=j+1)
                d.config(state = "readonly")
        Back = ttk.Button(regis, text="Back", command=lambda : _back(regis,module,y,w))
        Back.grid(column=1, row=len(ls.index)+1,columnspan =2)
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
def _mfill():
    try:
     
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from members where m_id='"+a.get()+"'")
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
            i.set(ls.iloc[0][8])
            j.set(ls.iloc[0][9])
            k.set(ls.iloc[0][10])
        else:
            mBox.showinfo('!....IIIISH....!', 'Not Found')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
        
def _mupdate():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("update members set name='"+b.get()+"',gender='"+c.get()+"',dob='"+d.get()+"',m_no='"+e.get()+"',department='"+f.get()+"',aadhar_card='"+g.get()+"',address='"+h.get()+"',doj='"+i.get()+"',fees_paid='"+j.get()+"',Fees_delay='"+k.get()+"' where m_id='"+a.get()+"'")
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
            i.set('')
            j.set('')
            k.set('')
        else:
            mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()
        
def _mdelete():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("delete from members where m_id='"+a.get()+"'")
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
            i.set('')
            j.set('')
            k.set('')
        else:
            mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()

