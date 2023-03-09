#calculator main
#define functions in calcFunc.py
from tkinter import ttk
from tkinter import *
import calcFunc
root = Tk(screenName="Calculator")
# ths section checks if tkinter is working, "hello world" type
# def main():
#     frm = ttk.Frame(root, padding=10)
#     frm.grid()
#     ttk.Label(frm, text="I am working").grid(column=0,row=0)
#     ttk.Button(frm, text="kill me",command=root.destroy).grid(column=1,row=0)
#     root.mainloop()

#main calc function
def main():
    #create frame and grid
    dispVal = float
    dispVal = 0
    defDispVal = 0
    frm=ttk.Frame(root,padding=10)
    frm.grid()
    #create display and make it the highest object
    Disp=ttk.Entry(frm,textvariable=dispVal,background="Grey",width=48)
    Disp.grid(column=0,row=0,columnspan=4)
    #numpad buttons
    #like a normal numpad, the 0 button is twice as wide as the others. Adjusting the width of the button affects the width of the row without columnwidth
    #default button size is 12, expands based on amount of text needed to display(?)
    ttk.Button(frm,text="0",width=24,takefocus=0).grid(column=0,columnspan=2,row=20)
    ttk.Button(frm,text=".",takefocus=0).grid(column=2,row=20)
    ttk.Button(frm,text="1",takefocus=0).grid(column=0,row=19)
    ttk.Button(frm,text="2",takefocus=0).grid(column=1,row=19)
    ttk.Button(frm,text="3",takefocus=0).grid(column=2,row=19)
    ttk.Button(frm,text="4",takefocus=0).grid(column=0,row=18)
    ttk.Button(frm,text="5",takefocus=0).grid(column=1,row=18)
    ttk.Button(frm,text="6",takefocus=0).grid(column=2,row=18)
    ttk.Button(frm,text="7",takefocus=0).grid(column=0,row=17)
    ttk.Button(frm,text="8",takefocus=0).grid(column=1,row=17)
    ttk.Button(frm,text="9",takefocus=0).grid(column=2,row=17)
    #now for the function buttons
    ttk.Button(frm,text="=",takefocus=0).grid(column=3,row=20)
    ttk.Button(frm,text="+",takefocus=0).grid(column=3,row=19)
    ttk.Button(frm,text="-",takefocus=0).grid(column=3,row=18)
    ttk.Button(frm,text="*",takefocus=0).grid(column=3,row=17)
    ttk.Button(frm,text="/",takefocus=0).grid(column=3,row=16)
    ttk.Button(frm,text="Sqrt",takefocus=0).grid(column=2,row=16)
    ttk.Button(frm,text="CuSqrt",takefocus=0).grid(column=1,row=16)
    ttk.Button(frm,text="Exp",takefocus=0).grid(column=0,row=16)
    ttk.Button(frm,text="Clear",takefocus=0).grid(column=2,row=21)

    #exit button
    #do I even need it? window will be big enough for x button to appear at top(?)
    #yes, leave it
    ttk.Button(frm,text="Exit",command=root.destroy).grid(column=3,row=21)

    #call window in
    root.mainloop()

main()