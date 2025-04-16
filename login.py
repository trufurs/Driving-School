from tkinter import ttk,Label
from ttkthemes import themed_tk as tk
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error
from tkinter import *
import pandas as pd
from PIL import Image, ImageDraw, ImageTk, ImageFont

k= tk.ThemedTk()
k.get_themes()
k.set_theme_advanced("radiance",preserve_transparency=False)
k.title('Driving school')
k.config(bg='white')
k.iconbitmap('Picture1.ico')
F0=Frame(k)
F0.pack()
t=0
def _login(mlog):
    mlog.pack()
    def EmsgBox():
        mBox.showinfo('Error', usr.get()+'\nInvalid Login Id or Password')
        usr.set('')
        pas.set('')
    def SmsgBox():
        mBox.showinfo('Welcome', usr.get())
        _back(mlog,_window,t)
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
    entry_pady = 7
    text_x1 = 55
    text_y1= 45
    text_x2 = 55 + 140
    text_y2 = 45
    text_x3 = 55
    text_y3= 45 + 45    
    image = Image.open("aaaa.PNG")
    image=image.resize((1000,650),1)
    k.geometry("%sx%s"%(1000,650))
    text1="Driving School"
    draw = ImageDraw.Draw(image)
    _, _,width_text, height_text = draw.textbbox((0, 0), text=text1)
    photoimage = ImageTk.PhotoImage(image)
    B=Label(mlog, image=photoimage)
    B.place(x=0,y=0)
    B.pack()
    photoimage1 =   PhotoImage(file="Webp.net-resizeimage (3).png")
    usr = StringVar()
    usrw=ttk.Entry(mlog, background="white", textvariable=usr)
    usrw.place(x=text_x1, y=text_y1+ height_text +7)
    pas = StringVar()
    pasw=ttk.Entry(mlog,background= "white", textvariable=pas , show='•')
    pasw.place(x=text_x2, y=text_y2 + height_text +7)
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
    action = Button(mlog, image=photoimage1, command=SmsgBox,border=0)
    action.place(x=text_x3,y=text_y3)
    mlog.mainloop()
def _back(x,y,q):
    x.destroy()
    q+=1
    globals()['F%s' % q]=Frame(k)
    y(globals()['F%s' % q])
def _Driver(x):
    from driver import _ddata,_dregistration,_dchange,_dremove
    from FUNCTION import _widow
    _widow(x,"Capture1.png",'Drivers',"back.png","2206310.png","member1.png","update (1).png","trash.png",lambda : _back(x,_window,t),lambda : _dregistration(t,x,_Driver,k),lambda : _ddata(t,x,_Driver,k),lambda : _dchange(t,x,_Driver,k),lambda : _dremove(t,x,_Driver,k))
def _Member(x):
    from members import _mdata,_mregistration,_mchange,_mremove
    from FUNCTION import _widow
    _widow(x,"Capture1.png",'Our Customer',"back.png","profile.png","customer.png","update (1).png","trash.png",lambda : _back(x,_window,t),lambda : _mregistration(t,x,_Member,k),lambda : _mdata(t,x,_Member,k),lambda : _mchange(t,x,_Member,k),lambda : _mremove(t,x,_Member,k))
def _Car(x):
    from cars import _cdata,_cnewcar,_cchange,_cremove
    from FUNCTION import _widow
    _widow(x,"Capture1.png",'Cars',"back.png","addc.png","cars1.png","organization (1).png","trash.png",lambda : _back(x,_window,t),lambda : _cnewcar(t,x,_Car,k),lambda : _cdata(t,x,_Car,k),lambda : _cchange(t,x,_Car,k),lambda : _cremove(t,x,_Car,k))
def _Routine(x):
    from routine import _r
    from FUNCTION import _Routin
    _Routin(x,"Capture1.png",'Daily Routine',"back.png","premium.png","normal.png",lambda : _back(x,_window,t),lambda : _r(t,x,_Routine,'Premium',k),lambda : _r(t,x,_Routine,'Normal',k))
    actin = ttk.Button(x, text='Premium', command=lambda : _r(t,x,_Routine,'Premium',k))
    actin.grid(column=1,row=1)
    acton = ttk.Button(x, text='Normal', command=lambda : _r(t,x,_Routine,'Normal',k))
    acton.grid(column=1,row=2)
    Back=ttk.Button(x,text='Back',command=lambda : _back(x,_window,t))
    Back.grid(row=0,column=0)
    for child in x.winfo_children():
        child.grid_configure(padx=20, pady=20)
def _window(x):
    from FUNCTION import _widow
    _widow(x,"apppy1.png",'Home',"exit.png","rating (2).png","member1.png","car1.png","calendar (2).png",lambda : _back(x,_login,t),lambda : _back(x,_Driver,t),lambda : _back(x,_Member,t),lambda : _back(x,_Car,t),lambda : _back(x,_Routine,t))
_back(F0,_login,t)



    
