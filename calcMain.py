#calculator main
#define functions in calcFunc.py
from tkinter import *
import math
#yea I imported the math library
expression= ""
def type(val):
    global expression
    expression = expression + str(val)
    equation.set(expression)

def eqPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set('Error')
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def sqrt():
    try:
        global expression
        expression = float(expression)
        result = str(math.sqrt(expression))
        equation.set(result)
        expression=""
    except:
        equation.set('Error')
        expression=""

def cuSqrt():
    try:
        global expression
        expression = float(expression)
        result= str(math.cbrt(expression))
        equation.set(result)
        expression=""
    except:
        equation.set('Error')
        expression=""

def square():
    try:
        global expression
        expression = float(expression)
        result = str(math.pow(expression,2))
        equation.set(result)
        expression=""
    except:
        equation.set("Error")
        expression=""

# ths section checks if tkinter is working, "hello world" type
# def main():
#     root = ttk.Frame(root, padding=10)
#     root.grid()
#     ttk.Label(root, text="I am working").grid(column=0,row=0)
#     ttk.Button(root, text="kill me",command=root.destroy).grid(column=1,row=0)
#     root.mainloop()

#main calc function
if __name__ == "__main__":
    root = Tk()
    root.title('Calculator')
    equation = StringVar()
    #create frame and grid
    #create display and make it the highest object
    Disp=Entry(root,textvariable=equation,background="Grey",width=56)
    Disp.grid(column=0,row=0,columnspan=4)
    #numpad buttons
    #like a normal numpad, the 0 button is twice as wide as the others. Adjusting the width of the button affects the width of the row without columnwidth
    #default button size is 12, expands based on amount of text needed to display(?)
    button0=Button(root,text="0",width=26,takefocus=0,command=lambda:type(0)).grid(column=0,columnspan=2,row=20)
    buttonDec=Button(root,text=".",takefocus=0,width=12,command=lambda:type('.')).grid(column=2,row=20)
    button1=Button(root,text="1",takefocus=0,width=12,command=lambda:type(1)).grid(column=0,row=19)
    button2=Button(root,text="2",takefocus=0,width=12,command=lambda:type(2)).grid(column=1,row=19)
    button3=Button(root,text="3",takefocus=0,width=12,command=lambda:type(3)).grid(column=2,row=19)
    button4=Button(root,text="4",takefocus=0,width=12,command=lambda:type(4)).grid(column=0,row=18)
    button5=Button(root,text="5",takefocus=0,width=12,command=lambda:type(5)).grid(column=1,row=18)
    button6=Button(root,text="6",takefocus=0,width=12,command=lambda:type(6)).grid(column=2,row=18)
    button7=Button(root,text="7",takefocus=0,width=12,command=lambda:type(7)).grid(column=0,row=17)
    button8=Button(root,text="8",takefocus=0,width=12,command=lambda:type(8)).grid(column=1,row=17)
    button9=Button(root,text="9",takefocus=0,width=12,command=lambda:type(9)).grid(column=2,row=17)
    #now for the function buttons
    #why does = and clear functions not need ()? breaks if added, like they dont exist. Must be a python thing
    buttonEq=Button(root,text="=",takefocus=0,width=12,command=eqPress).grid(column=3,row=20)
    buttonPlus=Button(root,text="+",takefocus=0,width=12,command=lambda:type('+')).grid(column=3,row=19)
    buttonMinus=Button(root,text="-",takefocus=0,width=12,command=lambda:type('-')).grid(column=3,row=18)
    buttonMult=Button(root,text="*",takefocus=0,width=12,command=lambda:type('*')).grid(column=3,row=17)
    buttonDiv=Button(root,text="/",takefocus=0,width=12,command=lambda:type('/')).grid(column=3,row=16)
    buttonSqrt=Button(root,text="Sqrt",takefocus=0,width=12,command=sqrt).grid(column=2,row=16)
    buttonCuSqrt=Button(root,text="CuSqrt",takefocus=0,width=12,command=cuSqrt).grid(column=1,row=16)
    buttonExp=Button(root,text="Square",takefocus=0,width=12).grid(column=0,row=16)
    buttonClear=Button(root,text="Clear",takefocus=0,width=12,command=clear).grid(column=2,row=21)

    #exit button
    #do I even need it? window will be big enough for x button to appear at top(?)
    #yes, leave it
    buttonExit=Button(root,text="Exit",command=root.destroy,width=12).grid(column=3,row=21)

    #call window in
    root.mainloop()