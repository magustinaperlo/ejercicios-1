from cProfile import label
from cgitb import text
from tkinter import * 
import random
from tkinter import dialog
from unittest import result


ventana = Tk()
ventana.title("Generador de numeros")
ventana.config(bg="black", padx=80, pady= 10)



def rndom():
    a= n1.get()
    b = n2.get()
    if a<b:
        n3= random.randint(a,b)
        ngenerado.set(n3)
    else:
        n3 = 0
        ngenerado.set(n3)
        pop()
    

def pop():
    popp= Toplevel()
    popp.config(bg="black", padx=80, pady= 10)
    Label(popp, text="el primer campo tiene que ser menor al segundo", background="black", foreground="white").grid(row=0, column=0,pady= 10)
    Button(popp, text= "oka", command= popp.destroy).grid(row=1, column=0,pady= 10)


n1= IntVar()
n2= IntVar()
ngenerado= StringVar()

num1 = Label (ventana, text="numero 1", font= "arial 9", background="black", foreground="white")
num1.grid(row=0, column=0,pady= 10)

num2 = Label (ventana, text="numero 2", font= "arial 9", background="black", foreground="white")
num2.grid(row=1, column=0,pady= 10)

num_gen = Label (ventana, text="numero generado", font= "arial 9", background="black", foreground="white")
num_gen.grid(row=2, column=0,pady= 10)

#se añade el state readonly para que el usuario no tenga la posibilidad de ingresar valores manualmente y solo lo haga desde los spinbox
spin1 = Spinbox(ventana, from_= -100, to= 1000, textvariable= n1, state= "readonly")
spin1.grid(row = 0, column = 1,pady= 10)

spin2 = Spinbox(ventana, from_= -100, to= 1000, textvariable= n2,state= "readonly")
spin2.grid(row = 1, column = 1,pady= 10)

randomm = Label (ventana, textvariable= ngenerado, font= "arial 9", background="white", foreground="black", width= 18, height=1,state= "readonly")
randomm.grid(row=2, column=1,pady= 10)


boton1= Button(ventana, text="generar", width= 8, height=1,command= rndom)
boton1.grid(row=3, column= 1, pady= 10)




ventana.mainloop()
