from tkinter import *
from tkinter import ttk ,Label

def _ddata(x,y,module,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from D import _dshow
    _dshow(globals()['F%s' % x],x,module,k)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=10, pady=10)

def _dregistration(x,y,module,k):
    y.destroy()
    from D import _dr,_dinsert,_back
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    _dr(globals()['F%s' % x])

    Back = ttk.Button(globals()['F%s' % x], text="Back", command=lambda : _back(globals()['F%s' % x],module,x,k))
    Back.grid(column=3, row=5)

    submit = ttk.Button(globals()['F%s' % x], text="Submit", command=_dinsert) 
    submit.grid(column=3, row=6)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)
def _dchange(x,y,module,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    
    from D import _dr,_fill,_dupdate,_back
    _dr(globals()['F%s' % x])
    Back = ttk.Button(globals()['F%s' % x], text="Back",command=lambda : _back(globals()['F%s' % x],module,x,k))
    Back.grid(column=3, row=5)

    submit = ttk.Button(globals()['F%s' % x], text="Update!", command=_dupdate) 
    submit.grid(column=3, row=6)

    search = ttk.Button(globals()['F%s' % x], text="Search!", command=_fill) 
    search.grid(column=2, row=6)

    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)
    
def _dremove(x,y,module,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from D import _ddelete
    _ddelete(globals()['F%s' % x],x,module,k)

