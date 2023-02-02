from tkinter import *
from tkinter import ttk ,Label
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
import pandas as pd

did = StringVar()
name = StringVar()
gen = StringVar()
dob = StringVar()
lic = StringVar()
aadhar = StringVar()
address = StringVar()
m_no = StringVar()
doj = StringVar()
tt = StringVar()

def _back(x,y,q,k):
    did.set('')
    name.set('')
    gen.set('g')
    dob.set('')
    lic.set('')
    aadhar.set('')
    address.set('')
    m_no.set('')
    doj.set('')
    tt.set('g')
    x.destroy()
    globals()['F%s' % q]=Frame(k)
    y(globals()['F%s' % q])
    globals()['F%s' % q].pack()
    q+=1    

def _dr(t):
    t.config(bg="white")
    D_id= Label(t, text="Driver id : ",bg="white")
    D_id.grid(column=0, row=0, sticky=W)
    Name= Label(t, text="Name : ",bg="white")
    Name.grid(column=0, row=1, sticky=W)
    Gender= Label(t, text="Gender : ",bg="white")
    Gender.grid(column=0, row=2, sticky=W)
    Dob= Label(t, text="Date of Birth : ",bg="white")
    Dob.grid(column=2, row=1, sticky=W)
    Dlisence= Label(t, text="Driving lisence : ",bg="white")
    Dlisence.grid(column=0, row=3, sticky=W)
    Aadhar= Label(t, text="Aadhar Number : ",bg="white")
    Aadhar.grid(column=2, row=3, sticky=W)
    Address= Label(t, text="Address : ",bg='white')
    Address.grid(column=0, row=4, sticky=W)
    M_no= Label(t, text="Mobile number : ",bg="white")
    M_no.grid(column=2, row=0, sticky=W)
    Dtest= Label(t, text="Driving Test : ",bg="white")
    Dtest.grid(column=0, row=5, sticky=W)
    Doj= Label(t, text="Date of joining : ",bg="white")
    Doj.grid(column=0, row=6, sticky=W)

    d_id = Entry(t, width=20, textvariable=did,bg="white")
    d_id.grid(column=1, row=0, sticky=W)
    nam = Entry(t, width=20, textvariable=name,bg="white")
    nam.grid(column=1, row=1, sticky=W)
    gen.set('g')
    male = Radiobutton(t, text='Male', variable=gen, value='M',bg="white") 
    male.grid(column=1, row=2, sticky=W)
    female=Radiobutton(t, text='Female', variable=gen, value='F',bg="white") 
    female.grid(column=2, row=2, sticky=W)
    do = ttk.Entry(t, width=20, textvariable=dob)
    do.grid(column=3, row=1, sticky=W)
    lisence = ttk.Entry(t, width=20, textvariable=lic)
    lisence.grid(column=1, row=3, sticky=W)
    a_id = ttk.Entry(t, width=20, textvariable=aadhar)
    a_id.grid(column=3, row=3, sticky=W)
    add = ttk.Entry(t, width=71, textvariable=address)
    add.grid(column=1, row=4,columnspan=3, sticky=W)
    mobile = ttk.Entry(t, width=20, textvariable=m_no)
    mobile.grid(column=3, row=0, sticky=W)
    when = ttk.Entry(t, width=20, textvariable=doj)
    when.grid(column=1, row=6, sticky=W)
    tt.set('g')
    yes = Radiobutton(t, text='Yes', variable=tt, value='Y',bg="white") 
    yes.grid(column=1, row=5, sticky=W) 						
    no= Radiobutton(t, text='No', variable=tt, value='N',bg="white") 
    no.grid(column=2, row=5, sticky=W)

def _dinsert():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("insert into drivers values("+did.get()+", '"+name.get()+"', '"+gen.get()+"', '"+dob.get()+"', '"+lic.get()+"', '"+aadhar.get()+"', '"+address.get()+"', '"+m_no.get()+"', '"+doj.get()+"', '"+tt.get()+"')")
        print(cursor.rowcount)
        if(cursor.rowcount>0):
            mBox.showinfo('Congrats!','Registered!')
            did.set('')
            name.set('')
            gen.set('')
            dob.set('')
            lic.set('')
            aadhar.set('')
            address.set('')
            m_no.set('')
            doj.set('')
            tt.set('')
        else:
            mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()


def _dshow(t,y,module,k):
    t.config(bg="white")
    D_id= Label(t, text="Driver id :",bg="white")
    D_id.grid(column=0, row=0, sticky=W)
    Name= Label(t, text="Name :",bg="white")
    Name.grid(column=1, row=0, sticky=W)
    Gender= Label(t, text="Gender :",bg="white")
    Gender.grid(column=2, row=0, sticky=W)
    Dob= Label(t, text="Date of Birth :",bg="white")
    Dob.grid(column=3, row=0, sticky=W)
    Dlisence= Label(t, text="Driving lisence :",bg="white")
    Dlisence.grid(column=4, row=0, sticky=W)
    Aadhar= Label(t, text="Aadhar Number :",bg="white")
    Aadhar.grid(column=5, row=0, sticky=W)
    Address= Label(t, text="Address :",bg="white")
    Address.grid(column=6, row=0, sticky=W)
    M_no= Label(t, text="Mobile number :",bg="white")
    M_no.grid(column=7, row=0, sticky=W)
    Dtest= Label(t, text="Driving Test :",bg="white")
    Dtest.grid(column=8, row=0, sticky=W)
    Doj= Label(t, text="Date of joining :",bg="white")
    Doj.grid(column=9, row=0, sticky=W)
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("select * from drivers")
        ls = cursor.fetchall()
        ls=pd.DataFrame(ls)
        for i in range(0, len(ls.index)):
            for j in range(0, len(ls.columns)):
                b = Entry(t,width=10)
                b.insert(0, ls.iloc[i][j])
                b.grid(row=i+1, column=j)
                b.config(state = "readonly")
        Back = ttk.Button(t, text="Back", command=lambda : _back(t,module,y,k))
        Back.grid(column=0, row=len(ls.index)+1)
          
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()

def _dupdate():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("update drivers set name= '"+name.get()+"',gender='"+gen.get()+"',dob='"+dob.get()+"', D_lisence='"+lic.get()+"', aadhar_card='"+aadhar.get()+"', address='"+address.get()+"', m_no='"+m_no.get()+"', doj='"+doj.get()+"', d_test='"+tt.get()+"' where d_id='"+did.get()+"'")
        print(cursor.rowcount)
        '''ls = cursor.fetchall()
        ls=list(ls[0])'''
        if(cursor.rowcount>0):
            mBox.showinfo('Congrats!','Updated!')
            did.set('')
            name.set('')
            gen.set('')
            dob.set('')
            lic.set('')
            aadhar.set('')
            address.set('')
            m_no.set('')
            doj.set('')
            tt.set('')
        else:
            mBox.showinfo('!Error!', 'Not Done!')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()

def _fill():
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from drivers where d_id='"+did.get()+"'")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            did.set(ls.iloc[0][0])
            name.set(ls.iloc[0][1])
            gen.set(ls.iloc[0][2])
            dob.set(ls.iloc[0][3])
            lic.set(ls.iloc[0][4])
            aadhar.set(ls.iloc[0][5])
            address.set(ls.iloc[0][6])
            m_no.set(ls.iloc[0][7])
            doj.set(ls.iloc[0][8])
            tt.set(ls.iloc[0][9])
        
        else:
            mBox.showinfo('!Error!', 'Not Found')
    except Error as z :
        mBox.showinfo('Error', z)
    finally:
        print("MySQL connection is closed")
        conn.commit()



def _ddelete(regis,y,module,k):
    regis.config(bg="white")
    y+=1
    li=[]
    #tuplle=()
    def _l():
        for k in range(1,i+1):
            li[k-1]=globals()['B%s' % k].get()
    try:
        conn = mysql.connector.connect(host='localhost',database='fproject',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        row = cursor.execute("select * from drivers")
        ls = cursor.fetchall()
        ls=pd.DataFrame(ls)
        for i in range(1, len(ls.index)+1):
            li.append('0')
            globals()['B%s' % i]= StringVar()
            globals()['B%s' % i].set(False)
            globals()['Br%s' % i]= Checkbutton(regis,variable=globals()['B%s' % i],onvalue=ls.iloc[i-1][0],command=_l,bg='white')
            globals()['Br%s' % i].grid(row=i-1,column=0)
            for j in range(0, len(ls.columns)):
                b = Entry(regis,width=10)
                b.insert(0, ls.iloc[i-1][j])
                b.grid(row=i-1, column=j+1)
                b.config(state = "readonly")
            def _delete():
                for s in li:
                    dl = cursor.execute("delete from drivers where D_id = '"+s+"'")
                    if (cursor.rowcount>0):
                        conn.commit()
                    else:
                        mBox.showinfo('!Error!', 'Not Done!')
        delete = ttk.Button(regis, text="Delete permently", command=_delete)
        delete.grid(column=j, row=i+1,columnspan=2)
        Back = ttk.Button(regis, text="Back",command=lambda: _back(regis,module,y,k))
        Back.grid(column=1, row=i+1)
        regis.pack()	    
    except Error as e :
        mBox.showinfo('Error', e)
    finally:
        print("MySQL connection is closed")
        conn.commit()
        
    for child in regis.winfo_children():
        child.grid_configure(padx=10, pady=10)
