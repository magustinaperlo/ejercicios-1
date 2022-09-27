from multiprocessing.sharedctypes import Value
from select import select
from tkinter import *
from tkinter import messagebox
from turtle import right
import tkinter as tk

ventana = tk.Tk()
ventana.title("calculadora 2")
ventana.config(bg="black", padx=10, pady= 10)
opcion = IntVar()
var = StringVar()

def validar():
        valor1=float(num1.get())
        valor2 = float(num2.get())
        if (valor2<1):
            messagebox.showwarning("Error","No es posible dividir por cero")
           
        else:
            dividir = float(valor1) / float(valor2)
            return var.set(dividir)
 

def todo():
    
    op = opcion.get()
    if op== 1:
         suma = float(num1.get()) + float(num2.get())
         return var.set(suma)
    if op== 2:
         resta = float(num1.get()) - float(num2.get())
         return var.set(resta)
    if op== 3:
         multiplicar = float(num1.get()) * float(num2.get())
         return var.set(multiplicar)
    if op== 4:
         validar()
        

    
    
 


primer_numero = Label (ventana, text="valor 1", font= "arial 9", background="black", foreground="white")
primer_numero.grid(row=1, column=0,padx= 10, pady= 15)

segundo_numero = Label (ventana, text="valor 2", font= "arial 9", background="black", foreground="white")
segundo_numero.grid(row=2, column=0,padx= 10, pady= 15)

result = Label (ventana, text="Resultado", font= "arial 9", background="black", foreground="white")
result.grid(row=3, column=0,padx= 10, pady= 15)



operaciones = Label (ventana, text="operaciones", font= "arial 9", background="black", foreground="white")
operaciones.grid(row=0, column=2,padx= 10, pady= 15)



num1 = Entry (ventana, bg= "white", justify="center")
num1.grid (row= 1, column= 1, padx= 10)

num2 = Entry (ventana, bg= "white", justify="center")
num2.grid (row= 2, column= 1, padx= 10)






padsum= Radiobutton(ventana, text= "sumar", value= 1, variable= opcion, background="black", foreground="blue")
padsum.grid(row=1, column=2,padx= 10, pady= 15)


padres = Radiobutton(ventana, text= "restar", value= 2, variable= opcion, background="black", foreground="blue")
padres.grid(row=2, column=2, padx= 10, pady= 15)

padmult = Radiobutton(ventana, text= "multiplicar", value= 3, variable= opcion, background="black", foreground="blue")
padmult.grid(row=3, column=2,padx= 10, pady= 15)

paddiv = Radiobutton(ventana, text= "dividir", value= 4, variable= opcion, background="black", foreground="blue")
paddiv.grid(row=4, column=2,padx= 10, pady= 15)



boton1= Button(ventana, text="calcular", width= 16, height=1, command= todo)
boton1.grid(row=5, column= 1, pady= 10)

resultado = Label (ventana, textvariable=var, font= "arial 9", background="white", foreground="black", width= 17, height=1,)
resultado.grid(row=3, column=1,padx= 10, pady= 15)


ventana.mainloop()
