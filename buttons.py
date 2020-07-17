from tkinter import*
import calculator

def scibtn() :
    btnln = Button(calculator.root, bg="#605052", fg="white", text="ln", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lnfunc, activebackground='#696969', activeforeground='white')
    btnln.grid(row=6, column=0)
    btnlog = Button(calculator.root, bg="#605052", fg="white", text="log", font=("arial",30,"bold"), bd=5, height=1, width=5, command=logfunc, activebackground='#696969', activeforeground='white')
    btnlog.grid(row=6, column=1)
    btnopenbr = Button(calculator.root, bg="#605052", fg="white", text="(", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click("("), activebackground='#696969', activeforeground='white')
    btnopenbr.grid(row=6, column=2)
    btnclosebr = Button(calculator.root, bg="#605052", fg="white", text=")", font=("arial",30,"bold"), bd=5, height=1, width=5, command=lambda:click(')'), activebackground='#696969', activeforeground='white')
    btnclosebr.grid(row=6, column=3)
    btnsci.grid_remove()
    root.btnexp = Button(calculator.root, bg="#605052", fg="white", text="e", font=("arial",30,"bold"), bd=5, height=1, width=5, command=expo, activebackground='#696969', activeforeground='white')
    root.btnexp.grid(row=5, column=0,pady=10)

    root.btndeg = Button(calculator.root, bg="#605052", fg="white", text="deg", font=("arial",30,"bold"), bd=5, height=1, width=5, command=degfunc, activebackground='#696969', activeforeground='white')
    root.btndeg.grid(row=7, column=0, pady =10)
    root.btnsin = Button(calculator.root, bg="#605052", fg="white", text="sin", font=("arial",30,"bold"), bd=5, height=1, width=5, command=sinfunc, activebackground='#696969', activeforeground='white')
    root.btnsin.grid(row=7, column=1)
    root.btncos = Button(calculator.root, bg="#605052", fg="white", text="cos", font=("arial",30,"bold"), bd=5, height=1, width=5, command=cosfunc, activebackground='#696969', activeforeground='white')
    root.btncos.grid(row=7, column=2)
    root.btntan = Button(calculator.root, bg="#605052", fg="white", text="tan", font=("arial",30,"bold"), bd=5, height=1, width=5, command=tanfunc, activebackground='#696969', activeforeground='white')
    root.btntan.grid(row=7, column=3)
            
    root.btn2nd = Button(calculator.root, bg="#ec4d37", fg="white", text="2nd", font=("arial",30,"bold"), bd=5, height=1, width=5, command=intrifunc, activebackground='#696969', activeforeground='white')
    root.btn2nd.grid(row=1, column=4)
    btnpow = Button(calculator.root, bg="#605052", fg="white", text="^", font=("arial",30,"bold"), bd=5, height=1, width=5, command=power, activebackground='#696969', activeforeground='white')
    btnpow.grid(row=2, column=4)
    btnsqrt = Button(calculator.root, bg="#605052", fg="white", text="sqrt", font=("arial",30,"bold"), bd=5, height=1, width=5, command=sqrtfunc, activebackground='#696969', activeforeground='white')
    btnsqrt.grid(row=3, column=4)
    btnfact = Button(calculator.root, bg="#605052", fg="white", text="!", font=("arial",30,"bold"), bd=5, height=1, width=5, command=factfunc, activebackground='#696969', activeforeground='white')
    btnfact.grid(row=4, column=4)
    btnres = Button(calculator.root, bg="#605052", fg="white", text="1/x", font=("arial",30,"bold"), bd=5, height=1, width=5, command=resfunc, activebackground='#696969', activeforeground='white')
    btnres.grid(row=5, column=4)
    btnpi = Button(calculator.root, bg="#605052", fg="white", text="pi", font=("arial",30,"bold"), bd=5, height=1, width=5, command=pifunc, activebackground='#696969', activeforeground='white')
    btnpi.grid(row=6, column=4)
    root.btnsim = Button(calculator.root, bg="#ec4d37", fg="white", text="simple", font=("arial",30,"bold"), bd=5, height=1, width=5, command=simple, activebackground='#696969', activeforeground='white')
    root.btnsim.grid(row=7, column=4)