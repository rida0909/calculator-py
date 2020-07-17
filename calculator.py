from tkinter import*
from tkinter import messagebox
import math

root = Tk()
root.title("Smart Calculator")
root.config(bg="black")
root.geometry("600x600+500+50")
root.iconbitmap('icon.ico')

def sciCal() :
    root.geometry("750x800+400+0")
    display.config(width = "25")
    scibtn()

def intrifunc() :
    root.btnsin.grid_remove()
    root.btncos.grid_remove()
    root.btntan.grid_remove()
    root.btn2nd.grid_remove()
    root.btnsinin = Button(root, bg="#605052", fg="white", text="sin-in", font=("arial",30,"bold"), bd=5, height=1, width=5, command=insinfunc, activebackground='#696969', activeforeground='white')
    root.btnsinin.grid(row=7, column=1)
    root.btncosin = Button(root, bg="#605052", fg="white", text="cos-in", font=("arial",30,"bold"), bd=5, height=1, width=5, command=incosfunc, activebackground='#696969', activeforeground='white')
    root.btncosin.grid(row=7, column=2)
    root.btntanin = Button(root, bg="#605052", fg="white", text="tan-in", font=("arial",30,"bold"), bd=5, height=1, width=5, command=intanfunc, activebackground='#696969', activeforeground='white')
    root.btntanin.grid(row=7, column=3)
    root.btn1st = Button(root, bg="#ec4d37", fg="white", text="1st", font=("arial",30,"bold"), bd=5, height=1, width=5, command=trifunc, activebackground='#696969', activeforeground='white')
    root.btn1st.grid(row=1, column=4)

def power() :
    pass

def factfunc() :
    pass

def resfunc() :
    pass

def pifunc() :
    pass

def simple() :
    display.config(width = "20")
    root.btnsim.grid_remove()
    root.btnexp.grid_remove()
    root.btnsci.grid(row=5, column=0,pady=10)
    root.geometry("600x600+500+50")

    for i in buttons :
        i.grid_remove()

def decimal():
    pass

def insinfunc() :
    pass

def incosfunc() :
    pass

def intanfunc() :
    pass

def expo() :
    global operation
    try :
        result = math.exp(eval(equation.get()))
        operation = str(result)
        equation.set(operation)
    except :
        messagebox.showinfo("invalid input", "pleaase enter correcct equation.")

def degfunc() :
    global operation
    root.btndeg.grid_remove()
    root.btnrad = Button(root, bg="#605052", fg="white", text="rad", font=("arial",30,"bold"), bd=5, height=1, width=5, command=radfunc, activebackground='#696969', activeforeground='white')
    root.btnrad.grid(row=7, column=0)
    try : 
        result = math.degrees(eval(equation.get()))
        operation = str(result)
        equation.set(operation)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def radfunc() :
    global operation
    root.btnrad.grid_remove()
    root.btndeg = Button(root, bg="#605052", fg="white", text="deg", font=("arial",30,"bold"), bd=5, height=1, width=5, command=degfunc, activebackground='#696969', activeforeground='white')
    root.btndeg.grid(row=7, column=0)
    try : 
        result = math.radians(eval(equation.get()))
        operation = str(result)
        equation.set(operation)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def backspace():
    global operation
    operation = operation[0: len(operation)-1]
    equation.set(operation)

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

def lnfunc() :
    global operation
    try :
        result = math.log(eval(equation.get()))
        operation = str(result)
        equation.set(result)
    except :
        messagebox.showinfo("invalid input", "first enter an input than command an operation")

def logfunc() :
    global operation
    messagebox.showinfo("read","the last digit in the equation is connsidered as base")
    base = int(operation[-1])
    num = equation.get()
    num = num[0:len(num)-1]
    eq = (eval(num))
    try :
        result = math.log(eq,base)
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

display = Entry(root, bg="#dcdcdc", font=("arial", 40, "bold"), bd="10", justify='right',width = 20, textvariable=equation)
display.grid(ipady=10, columnspan=5)

btnclear = Button(root, bg="#605052", fg="white", text="CA", font=("arial",30,"bold"), bd=5, height=1, width=5, command=clear, activebackground='#696969', activeforeground='white')
btnclear.grid(row=1, column=0, pady =10)
btnback = Button(root, bg="#605052", fg="white", text="C", font=("arial",30,"bold"), bd=5, height=1, width=5, command=backspace, activebackground='#696969', activeforeground='white')
btnback.grid(row=1, column=1)
btndiv = Button(root, bg="#605052", fg="white", text="/", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click('/'), activebackground='#696969', activeforeground='white')
btndiv.grid(row=1, column=3)
btnper = Button(root, bg="#605052", fg="white", text="%", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click('+'), activebackground='#696969', activeforeground='white')
btnper.grid(row=1, column=2)

btn7 = Button(root, bg="#110c11", fg="white", text="7", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(7), activebackground='#696969', activeforeground='white')
btn7.grid(row=2, column=0)
btn8 = Button(root, bg="#110c11", fg="white", text="8", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(8), activebackground='#696969', activeforeground='white')
btn8.grid(row=2, column=1)
btn9 = Button(root, bg="#110c11", fg="white", text="9", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(9), activebackground='#696969', activeforeground='white')
btn9.grid(row=2, column=2)
btnadd = Button(root, bg="#605052", fg="white", text="+", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click('+'), activebackground='#696969', activeforeground='white')
btnadd.grid(row=4, column=3)

btn4 = Button(root, bg="#110c11", fg="white", text="4", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(4), activebackground='#696969', activeforeground='white')
btn4.grid(row=3, column=0,pady=10)
btn5 = Button(root, bg="#110c11", fg="white", text="5", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(5), activebackground='#696969', activeforeground='white')
btn5.grid(row=3, column=1)
btn6 = Button(root, bg="#110c11", fg="white", text="6", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(6), activebackground='#696969', activeforeground='white')
btn6.grid(row=3, column=2)
btnsub = Button(root, bg="#605052", fg="white", text="-", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click('-'), activebackground='#696969', activeforeground='white')
btnsub.grid(row=3, column=3)

btn1 = Button(root, bg="#110c11", fg="white", text="1", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(1), activebackground='#696969', activeforeground='white')
btn1.grid(row=4, column=0)
btn2 = Button(root, bg="#110c11", fg="white", text="2", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(2), activebackground='#696969', activeforeground='white')
btn2.grid(row=4, column=1)
btn3 = Button(root, bg="#110c11", fg="white", text="3", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(3), activebackground='#696969', activeforeground='white')
btn3.grid(row=4, column=2)
btnmul = Button(root, bg="#605052", fg="white", text="X", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click('*'), activebackground='#696969', activeforeground='white')
btnmul.grid(row=2, column=3)

root.btnsci = Button(root, bg="#ec4d37", fg="white", text="Sci", font=("arial",30,"bold"), bd=5, height=1, width=5, command=sciCal, activebackground='#696969', activeforeground='white')
root.btnsci.grid(row=5, column=0,pady=10)
btn0 = Button(root, bg="#110c11", fg="white", text="0", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(0), activebackground='#696969', activeforeground='white')
btn0.grid(row=5, column=1)
btnequals = Button(root, bg="#ec4d37", fg="white", text="=", font=("arial",30,"bold"), bd=5, height=1, width=5, command=equal, activebackground='#696969', activeforeground='white')
btnequals.grid(row=5, column=3)
btndec = Button(root, bg="#110c11", fg="white", text=".", font=("arial",30,"bold"), bd=5, height=1, width=5, command=decimal, activebackground='#696969', activeforeground='white')
btndec.grid(row=5, column=2)

buttons = []

def scibtn() :
    btnln = Button(root, bg="#605052", fg="white", text="ln", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lnfunc, activebackground='#696969', activeforeground='white')
    btnln.grid(row=6, column=0)
    buttons.append(btnln)
    btnlog = Button(root, bg="#605052", fg="white", text="log", font=("arial",30,"bold"), bd=5, height=1, width=5, command=logfunc, activebackground='#696969', activeforeground='white')
    btnlog.grid(row=6, column=1)
    buttons.append(btnlog)
    btnopenbr = Button(root, bg="#605052", fg="white", text="(", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click("("), activebackground='#696969', activeforeground='white')
    btnopenbr.grid(row=6, column=2)
    buttons.append(btnopenbr)
    btnclosebr = Button(root, bg="#605052", fg="white", text=")", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(')'), activebackground='#696969', activeforeground='white')
    btnclosebr.grid(row=6, column=3)
    buttons.append(btnclosebr)
    root.btnsci.grid_remove()
    root.btnexp = Button(root, bg="#605052", fg="white", text="e", font=("arial",30,"bold"), bd=5, height=1, width=5, command=expo, activebackground='#696969', activeforeground='white')
    root.btnexp.grid(row=5, column=0,pady=10)

    root.btndeg = Button(root, bg="#605052", fg="white", text="deg", font=("arial",30,"bold"), bd=5, height=1, width=5, command=degfunc, activebackground='#696969', activeforeground='white')
    root.btndeg.grid(row=7, column=0, pady =10)
    buttons.append(root.btndeg)
    root.btnsin = Button(root, bg="#605052", fg="white", text="sin", font=("arial",30,"bold"), bd=5, height=1, width=5, command=sinfunc, activebackground='#696969', activeforeground='white')
    root.btnsin.grid(row=7, column=1)
    buttons.append(root.btnsin)
    root.btncos = Button(root, bg="#605052", fg="white", text="cos", font=("arial",30,"bold"), bd=5, height=1, width=5, command=cosfunc, activebackground='#696969', activeforeground='white')
    root.btncos.grid(row=7, column=2)
    buttons.append(root.btncos)
    root.btntan = Button(root, bg="#605052", fg="white", text="tan", font=("arial",30,"bold"), bd=5, height=1, width=5, command=tanfunc, activebackground='#696969', activeforeground='white')
    root.btntan.grid(row=7, column=3)
    buttons.append(root.btntan)
            
    btn2nd = Button(root, bg="#ec4d37", fg="white", text="2nd", font=("arial",30,"bold"), bd=5, height=1, width=5, command=intrifunc, activebackground='#696969', activeforeground='white')
    btn2nd.grid(row=1, column=4)
    buttons.append(btn2nd)
    btnpow = Button(root, bg="#605052", fg="white", text="^", font=("arial",30,"bold"), bd=5, height=1, width=5, command=power, activebackground='#696969', activeforeground='white')
    btnpow.grid(row=2, column=4)
    buttons.append(btnpow)
    btnsqrt = Button(root, bg="#605052", fg="white", text="sqrt", font=("arial",30,"bold"), bd=5, height=1, width=5, command=sqrtfunc, activebackground='#696969', activeforeground='white')
    btnsqrt.grid(row=3, column=4)
    buttons.append(btnsqrt)
    btnfact = Button(root, bg="#605052", fg="white", text="!", font=("arial",30,"bold"), bd=5, height=1, width=5, command=factfunc, activebackground='#696969', activeforeground='white')
    btnfact.grid(row=4, column=4)
    buttons.append(btnfact)
    btnres = Button(root, bg="#605052", fg="white", text="1/x", font=("arial",30,"bold"), bd=5, height=1, width=5, command=resfunc, activebackground='#696969', activeforeground='white')
    btnres.grid(row=5, column=4)
    buttons.append(btnres)
    btnpi = Button(root, bg="#605052", fg="white", text="pi", font=("arial",30,"bold"), bd=5, height=1, width=5, command=pifunc, activebackground='#696969', activeforeground='white')
    btnpi.grid(row=6, column=4)
    buttons.append(btnpi)
    root.btnsim = Button(root, bg="#ec4d37", fg="white", text="simple", font=("arial",30,"bold"), bd=5, height=1, width=5, command=simple, activebackground='#696969', activeforeground='white')
    root.btnsim.grid(row=7, column=4)



root.mainloop()