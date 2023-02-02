from tkinter import *
from tkinter import ttk, Label

def _cnewcar(x,y,module,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from C import _cars,_cinsert,_back
    _cars(globals()['F%s' % x])
    submit=ttk.Button(globals()['F%s' % x],text='Submit',command=_cinsert)
    submit.grid(row=8,column=4)
    Back=ttk.Button(globals()['F%s' % x],text='Back',command=lambda :  _back(globals()['F%s' % x],module,x,k))
    Back.grid(row=7,column=4)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)

    
def _cdata(x,y,z,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from C import _cshow
    _cshow(globals()['F%s' % x],x,z,k)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=10, pady=10)

def _cremove(x,y,module,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from C import _cars,_cfill,_cdelete,_back
    _cars(globals()['F%s' % x])
    submit=ttk.Button(globals()['F%s' % x],text='Delete',command=_cdelete)
    submit.grid(row=8,column=4)
    Back=ttk.Button(globals()['F%s' % x],text='Back',command=lambda :  _back(globals()['F%s' % x],module,x,k))
    Back.grid(row=7,column=4)
    fill=ttk.Button(globals()['F%s' % x],text='Search',command=_cfill)
    fill.grid(row=6,column=4)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)
    

def _cchange(x,y,module,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from C import _cars,_cfill,_cupdate,_back
    _cars(globals()['F%s' % x])
    submit=ttk.Button(globals()['F%s' % x],text='Update',command=_cupdate)
    submit.grid(row=8,column=4)
    Back=ttk.Button(globals()['F%s' % x],text='Back',command=lambda :  _back(globals()['F%s' % x],module,x,k))
    Back.grid(row=7,column=4)
    fill=ttk.Button(globals()['F%s' % x],text='Search',command=_cfill)
    fill.grid(row=6,column=4)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)
