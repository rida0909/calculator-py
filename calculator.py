from tkinter import*
from tkinter import messagebox
import math

root = Tk()
root.title("Smart Calculator")
root.config(bg="white")
root.geometry("600x700+500+50")
root.maxsize(width=750, height=710)
root.minsize(width=600, height=710)
root.iconbitmap('icon.ico')

def click(number) :
    global operation
    operation += str(number)
    equation.set(operation)

def clear() :
    global operation
    operation = ''
    equation.set(operation)

def equal() :
    global operation
    try :
        result = eval(operation)
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "please enter a valid input without starting with zero", parent=root)

def sinfunc() :
    global operation
    try :
        result = math.sin(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def sinfunc() :
    global operation
    try :
        result = math.sin(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def cosfunc() :
    global operation
    try :
        result = math.cos(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def tanfunc() :
    global operation
    try :
        result = math.tan(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def logfunc() :
    global operation
    try :
        result = math.log(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def sqrtfunc() :
    global operation
    try :
        result = math.sqrt(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

operation = ''
equation = StringVar()

display = Entry(root, bg="#ecb8a5", font=("arial", 40, "bold"), bd="10", justify='right', textvariable=equation)
display.grid(ipady=25, columnspan=4)

btn7 = Button(root, bg="#e49ab0", text="7", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(7), activebackground='#904c77', activeforeground='white')
btn7.grid(row=1, column=0, pady=10)
btn8 = Button(root, bg="#e49ab0", text="8", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(8), activebackground='#904c77', activeforeground='white')
btn8.grid(row=1, column=1)
btn9 = Button(root, bg="#e49ab0", text="9", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(9), activebackground='#904c77', activeforeground='white')
btn9.grid(row=1, column=2)
btnadd = Button(root, bg="#e49ab0", text="+", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click('+'), activebackground='#904c77', activeforeground='white')
btnadd.grid(row=1, column=3)

btn4 = Button(root, bg="#e49ab0", text="4", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(4), activebackground='#904c77', activeforeground='white')
btn4.grid(row=2, column=0)
btn5 = Button(root, bg="#e49ab0", text="5", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(5), activebackground='#904c77', activeforeground='white')
btn5.grid(row=2, column=1)
btn6 = Button(root, bg="#e49ab0", text="6", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(6), activebackground='#904c77', activeforeground='white')
btn6.grid(row=2, column=2)
btnsub = Button(root, bg="#e49ab0", text="-", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click('-'), activebackground='#904c77', activeforeground='white')
btnsub.grid(row=2, column=3)

btn1 = Button(root, bg="#e49ab0", text="1", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(1), activebackground='#904c77', activeforeground='white')
btn1.grid(row=3, column=0, pady=10)
btn2 = Button(root, bg="#e49ab0", text="2", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(2), activebackground='#904c77', activeforeground='white')
btn2.grid(row=3, column=1)
btn3 = Button(root, bg="#e49ab0", text="3", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(3), activebackground='#904c77', activeforeground='white')
btn3.grid(row=3, column=2)
btnmul = Button(root, bg="#e49ab0", text="*", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click('*'), activebackground='#904c77', activeforeground='white')
btnmul.grid(row=3, column=3)

btnclear = Button(root, bg="#e49ab0", text="C", font=("arial",30,"bold"), bd=5, height=2, width=5, command=clear, activebackground='#904c77', activeforeground='white')
btnclear.grid(row=4, column=0)
btn0 = Button(root, bg="#e49ab0", text="0", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click(0), activebackground='#904c77', activeforeground='white')
btn0.grid(row=4, column=1)
btnequals = Button(root, bg="#e49ab0", text="=", font=("arial",30,"bold"), bd=5, height=2, width=5, command=equal, activebackground='#904c77', activeforeground='white')
btnequals.grid(row=4, column=2)
btndiv = Button(root, bg="#e49ab0", text="/", font=("arial",30,"bold"), bd=5, height=2, width=5, command=lambda:click('/'), activebackground='#904c77', activeforeground='white')
btndiv.grid(row=4, column=3)

btnsin = Button(root, bg="#e49ab0", text="sin", font=("arial",30,"bold"), bd=5, height=2, width=5, command=sinfunc, activebackground='#904c77', activeforeground='white')
btnsin.grid(row=0, column=4)
btncos = Button(root, bg="#e49ab0", text="cos", font=("arial",30,"bold"), bd=5, height=2, width=5, command=cosfunc, activebackground='#904c77', activeforeground='white')
btncos.grid(row=1, column=4)
btntan = Button(root, bg="#e49ab0", text="tan", font=("arial",30,"bold"), bd=5, height=2, width=5, command=tanfunc, activebackground='#904c77', activeforeground='white')
btntan.grid(row=2, column=4)
btnsqrt = Button(root, bg="#e49ab0", text="sqrt", font=("arial",30,"bold"), bd=5, height=2, width=5, command=sqrtfunc, activebackground='#904c77', activeforeground='white')
btnsqrt.grid(row=3, column=4)
btnlog = Button(root, bg="#e49ab0", text="log", font=("arial",30,"bold"), bd=5, height=2, width=5, command=logfunc, activebackground='#904c77', activeforeground='white')
btnlog.grid(row=4, column=4)

root.mainloop()