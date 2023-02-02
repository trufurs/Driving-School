from tkinter import *
from tkinter import Label,ttk

def _mregistration(x,y,module,w):
    y.destroy()
    globals()['F%s' % x]=Frame(w)
    globals()['F%s' % x].pack()
    from M import _members, _minsert,_back
    _members(globals()['F%s' % x])
    submit=ttk.Button(globals()['F%s' % x],text='Submit',command=_minsert)
    submit.grid(row=8,column=4)
    Back=ttk.Button(globals()['F%s' % x],text='Back',command=lambda : _back(globals()['F%s' % x],module,x,w))
    Back.grid(row=8,column=1)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)

def _mdata(x,y,module,w):
    y.destroy()
    globals()['F%s' % x]=Frame(w)
    globals()['F%s' % x].pack()
    from M import _mshow
    _mshow(globals()['F%s' % x],x,module,w)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=4, pady=4)

def _mremove(x,y,module,w):
    y.destroy()
    globals()['F%s' % x]=Frame(w)
    globals()['F%s' % x].pack()
    from M import _members,_mfill,_mdelete,_back
    _members(globals()['F%s' % x])
    submit=ttk.Button(globals()['F%s' % x],text='Delete',command=_mdelete)
    submit.grid(row=8,column=4)
    Back=ttk.Button(globals()['F%s' % x],text='Back',command=lambda : _back(globals()['F%s' % x],module,x,w))
    Back.grid(row=8,column=1)
    fill=ttk.Button(globals()['F%s' % x],text='Search',command=_mfill)
    fill.grid(row=8,column=3)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)

def _mchange(x,y,module,w):
    y.destroy()
    globals()['F%s' % x]=Frame(w)
    globals()['F%s' % x].pack()
    from M import _members,_mfill,_mupdate,_back
    _members(globals()['F%s' % x])
    submit=ttk.Button(globals()['F%s' % x],text='Update',command=_mupdate)
    submit.grid(row=8,column=4)
    Back=ttk.Button(globals()['F%s' % x],text='Back',command=lambda : _back(globals()['F%s' % x],module,x,w))
    Back.grid(row=8,column=1)
    fill=ttk.Button(globals()['F%s' % x],text='Search',command=_mfill)
    fill.grid(row=8,column=3)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=20, pady=20)


