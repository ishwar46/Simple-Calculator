#SIMPLE GUI CALCULATOR USING TKINTER
import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)
root.title("Calculator")

#Defining Variables and operators
val = ""
A = 0
operator = "+"

#DEFINING FUCTION OF BUTTONS
def btn1_click():
    global val
    val = val + "1"
    data.set(val)


def btn2_click():
    global val
    val = val + "2"
    data.set(val)


def btn3_click():
    global val
    val = val + "3"
    data.set(val)


def btn4_click():
    global val
    val = val + "4"
    data.set(val)


def btn5_click():
    global val
    val = val + "5"
    data.set(val)


def btn6_click():
    global val
    val = val + "6"
    data.set(val)


def btn7_click():
    global val
    val = val + "7"
    data.set(val)


def btn8_click():
    global val
    val = val + "8"
    data.set(val)


def btn9_click():
    global val
    val = val + "9"
    data.set(val)


def btn0_click():
    global val
    val = val + "0"
    data.set(val)


def btn_add_click():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_sub_click():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_mul_click():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_div_click():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def clr_click():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def btn_ans():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error!!", "Division by 0 is not supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)
            val = str(C)




data = StringVar()

lbl = Label(root, text="Label", anchor=SE, font=("Verdana", 20), textvariable=data, background="#1C1C1C",fg="#D4D4D2",)
lbl.pack(expand=True, fill="both")

row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill="both")

row2 = Frame(root)
row2.pack(expand=True, fill="both")

row3 = Frame(root)
row3.pack(expand=True, fill="both")

row4 = Frame(root)
row4.pack(expand=True, fill="both")

# ROW 1 Button details
btn1 = Button(row1, text="1", font=("Verdana", 22), relief=GROOVE, border=0, command=btn1_click, cursor="hand2")
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(row1, text="2", font=("Verdana", 22), relief=GROOVE, border=0, command=btn2_click,cursor="hand2")
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(row1, text="3", font=("Verdana", 22), relief=GROOVE, border=0, command=btn3_click, cursor="hand2")
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(row1, text="+", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_add_click, fg="#4285F4", cursor="hand2")
btn4.pack(side=LEFT, expand=True, fill="both")

# ROW 2 Button details
btn1 = Button(row2, text="4", font=("Verdana", 22), relief=GROOVE, border=0, command=btn4_click, cursor="hand2")
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(row2, text="5", font=("Verdana", 22), relief=GROOVE, border=0, command=btn5_click, cursor="hand2")
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(row2, text="6", font=("Verdana", 22), relief=GROOVE, border=0, command=btn6_click, cursor="hand2")
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button( row2, text="-", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_sub_click, fg="#4285F4", cursor="hand2")
btn4.pack(side=LEFT, expand=True, fill="both")

# ROW 3 Button details
btn1 = Button(row3, text="7", font=("Verdana", 22), relief=GROOVE, border=0, command=btn7_click, cursor="hand2")
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(row3, text="8", font=("Verdana", 22), relief=GROOVE, border=0, command=btn8_click, cursor="hand2")
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(row3, text="9", font=("Verdana", 22), relief=GROOVE, border=0, command=btn9_click, cursor="hand2")
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(row3, text="*", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_mul_click, fg="#4285F4", cursor="hand2")
btn4.pack(side=LEFT, expand=True, fill="both")

# ROW 4 Button details
btn1 = Button(row4, text="c", font=("Verdana", 22), relief=GROOVE, border=0, command=clr_click, cursor="hand2")
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(row4, text="0", font=("Verdana", 22), relief=GROOVE, border=0, command=btn0_click, cursor="hand2")
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(row4, text="=", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_ans, cursor="hand2")
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(row4, text="/", font=("Verdana", 22), relief=FLAT, border=0, command=btn_div_click, fg="#4285F4", cursor="hand2")
btn4.pack(side=LEFT, expand=True, fill="both")

root.mainloop()