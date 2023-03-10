#can I make an even shittier one (for practice)
from tkinter import ttk
from tkinter import *
funcSelVal = 0
def funcSel(value):
        global funcSelVal
        funcSelVal = value
root = Tk(screenName="Dog Water")

def main():
    frm = ttk.Frame(root,padding=10)
    frm.grid()
    ttk.Label(frm,text="What am I doing?").grid(column=0,row=0,columnspan=2)
    ttk.Button(frm,text='Addition',command=funcSel(1)).grid(column=0,row=1)
    ttk.Button(frm,text='Subtraction',command=funcSel(2)).grid(column=1,row=1)
    ttk.Button(frm,text="Multiply",command=funcSel(3)).grid(column=0,row=2)
    ttk.Button(frm,text="Division",command=funcSel(4)).grid(column=1,row=2)
    