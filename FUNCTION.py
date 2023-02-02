from tkinter import *
from tkinter import ttk,Label
from PIL import Image, ImageDraw, ImageTk, ImageFont
from tkinter import ttk,Label
def _widow(frame0,ab,bc,cd,de,ef,fg,gh,hi,ij,jk,kl,lm):
    frame0.pack()

    image = Image.open(ab)
    image=image.resize((1000,650),1)
    photoimage = ImageTk.PhotoImage(image)
    B=Label(frame0, image=photoimage)
    B.place(x=0,y=0)
    B.pack()

    Cf = Label(frame0, text=bc,font=("Helvetica", 30),bg='white',fg='orangered')
    Cf.place(x=90,y=80)

    i=Image.open(cd)
    i=i.resize((45,45),1)
    m=Image.open(de)
    m=m.resize((200,125),1)
    a=Image.open(ef)
    a=a.resize((200,125),1)
    g=Image.open(fg)
    g=g.resize((200,125),1)
    e=Image.open(gh)
    e=e.resize((200,125),1)
    

    Back_image= ImageTk.PhotoImage(i)
    label = Label(image=Back_image)
    label.image=Back_image
    Driver_image= ImageTk.PhotoImage(m)
    label = Label(image=Driver_image)
    label.image = Driver_image
    Members_image= ImageTk.PhotoImage(a)
    label = Label(image=Members_image)
    label.image = Members_image
    Cars_image= ImageTk.PhotoImage(g)
    label=Label(image=Cars_image)
    label.image = Cars_image
    routine_image= ImageTk.PhotoImage(e)
    label = Label(image=routine_image)
    label.image = routine_image

    Back= Button(frame0,image=Back_image, command=hi,border=0,bg='white')
    Back.place(x=925,y=10)
    Driver = Button(frame0,image=Driver_image, command=ij,border=0,bg='white')
    Driver.place(x=50,y=320)
    Members = Button(frame0,image=Members_image, command=jk,border=0,bg='white')
    Members.place(x=290,y=320)
    Cars = Button(frame0,image=Cars_image, command=kl,border=0,bg='white')
    Cars.place(x=520,y=320)
    About = Button(frame0,image=routine_image, command=lm,border=0,bg='white')
    About.place(x=750,y=320)
    
    frame0.mainloop()

def _Routin(frame0,ab,bc,cd,ef,fg,hi,jk,kl):
    frame0.pack()

    image = Image.open(ab)
    image=image.resize((1000,650),1)
    photoimage = ImageTk.PhotoImage(image)
    B=Label(frame0, image=photoimage)
    B.place(x=0,y=0)
    B.pack()

    Cf = Label(frame0, text=bc,font=("Helvetica", 30),bg='white',fg='orangered')
    Cf.place(x=90,y=80)

    i=Image.open(cd)
    i=i.resize((45,45),1)
    a=Image.open(ef)
    a=a.resize((200,125),1)
    g=Image.open(fg)
    g=g.resize((200,125),1)
    

    Back_image= ImageTk.PhotoImage(i)
    label = Label(image=Back_image)
    label.image=Back_image
    Members_image= ImageTk.PhotoImage(a)
    label = Label(image=Members_image)
    label.image = Members_image
    Cars_image= ImageTk.PhotoImage(g)
    label=Label(image=Cars_image)
    label.image = Cars_image

    Back= Button(frame0,image=Back_image, command=hi,border=0,bg='white')
    Back.place(x=925,y=10)
    Members = Button(frame0,image=Members_image, command=jk,border=0,bg='white')
    Members.place(x=290,y=320)
    Cars = Button(frame0,image=Cars_image, command=kl,border=0,bg='white')
    Cars.place(x=520,y=320)  
    frame0.mainloop()
    
def _Driver(z):
    frame0.pack()

    image = Image.open("aaaa.png")
    image=image.resize((1000,650),1)
    photoimage = ImageTk.PhotoImage(image)
    B=Label(frame0, image=photoimage)
    B.place(x=0,y=0)
    B.pack()

    i=Image.open("exit.png")
    i=i.resize((45,45),1)
    m=Image.open("rating (2).png")
    m=m.resize((200,125),1)
    a=Image.open("member1.png")
    a=a.resize((200,125),1)
    g=Image.open("car.png")
    g=g.resize((200,125),1)
    e=Image.open("calendar (2).png")
    e=e.resize((200,125),1)
    

    Back_image= ImageTk.PhotoImage(i)
    label = Label(image=Back_image)
    label.image=Back_image
    Driver_image= ImageTk.PhotoImage(m)
    label = Label(image=Driver_image)
    label.image = Driver_image
    Members_image= ImageTk.PhotoImage(a)
    label = Label(image=Members_image)
    label.image = Members_image
    Cars_image= ImageTk.PhotoImage(g)
    label=Label(image=Cars_image)
    label.image = Cars_image
    routine_image= ImageTk.PhotoImage(e)
    label = Label(image=routine_image)
    label.image = routine_image

    

    Back= Button(frame0,image=Back_image, command=lambda :print('a'),border=0,bg='white')
    Back.place(x=925,y=10)
    Driver = Button(frame0,image=Driver_image, command=lambda :print('b'),border=0,bg='white')
    Driver.place(x=50,y=320)
    Members = Button(frame0,image=Members_image, command=lambda :print('b'),bg='white')
    Members.place(x=290,y=320)
    Cars = Button(frame0,image=Cars_image,bg='white', command=print('b'),border=0)
    Cars.place(x=520,y=320)
    About = Button(frame0,image=routine_image, command=lambda :print('b') ,border=0,bg='white')
    About.place(x=750,y=320)
    
    frame0.mainloop()
    
##    z.pack()
##    image = Image.open("Capture1.png")
##    image=image.resize((1000,650),1)
##    photoimage = ImageTk.PhotoImage(image)
##    B=Label(z, image=photoimage)
##    B.place(x=0,y=0)
##    B.pack()
##
##    i=Image.open("Webp.net-resizeimage (2).png")
##    i=i.resize((45,45),1)
##    m=Image.open("seo.png")
##    m=m.resize((350,225),1)
##    a=Image.open("atm (1).png")
##    a=a.resize((350,225),1)
##    g=Image.open("update (1).png")
##    g=g.resize((350,225),1)
##    e=Image.open("trash.png")
##    e=e.resize((350,225),1)
##    
##
##    Back_image= ImageTk.PhotoImage(i)
##    label = Label(image=Back_image)
##    label.image=Back_image
##    Driver_image= ImageTk.PhotoImage(m)
##    label = Label(image=Driver_image)
##    label.image = Driver_image
##    Members_image= ImageTk.PhotoImage(a)
##    label = Label(image=Members_image)
##    label.image = Members_image
##    Cars_image= ImageTk.PhotoImage(g)
##    label=Label(image=Cars_image)
##    label.image = Cars_image
##    About_image= ImageTk.PhotoImage(e)
##    label = Label(image=About_image)
##    label.image = About_image
##
##
##    Back= Button(frame,image=Back_image, command=_a,border=0,bg='MediumPurple4')
##    Back.place(x=0,y=0)
##    new = Button(z,image=Driver_image, command=_a,border=0,bg='MediumPurple4')
##    new.place(x=100+27,y=125+30)
##    insert = Button(z,image=Members_image, command=_a,border=0,bg='MediumPurple4')
##    insert.place(x=560-27,y=125+30)
##    update = Button(z,image=Cars_image, command=_a,border=0,bg='MediumPurple4')
##    update.place(x=100+27,y=375+30)
##    remove = Button(z,image=About_image, command=_a,border=0,bg='MediumPurple4')
##    remove.place(x=560-27,y=375+30)
##    
##    z.mainloop()


    

