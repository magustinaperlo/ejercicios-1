from distutils.command.clean import clean
from tkinter import *
from tkinter import messagebox
from turtle import right
import tkinter as tk



ventana = Tk()
ventana.title("calculadora")
ventana.config(bg="black", padx=1, pady= 2)
var = StringVar()
into = IntVar()
into2= IntVar()


def validar():
    try:
        valor1=pantalla1.get()
        valor2 = pantalla2.get()
    except:
        messagebox.showwarning("Error","Debe ingresar dos valores numericos")

def suma():
    suma = float(pantalla1.get()) + float(pantalla2.get())
    return var.set(suma)
    
def multiplicacion():
    multiplicacion = float(pantalla1.get()) * float(pantalla2.get())
    return var.set(multiplicacion)

# def divicion():
#     divicion = float(pantalla1.get()) / float(pantalla2.get())
#     return var.set(divicion)

def division():
    validar()
    if int(pantalla2.get())!=0:
        dividir=pantalla1.get()/pantalla2.get()
        return result.set(dividir)
    else:
        return messagebox.showerror ("Error", "No es posible dividir por 0")
    limpiar()

def resta():
    resta = float(pantalla1.get()) - float(pantalla2.get())
    return var.set(resta)


def clear():
   var.set(0)
   into.set(0)
   into2.set(0)



def porcentaje():
    porcentaje = float(pantalla1.get()) % float(pantalla2.get())
    return var.set(porcentaje)


primer_numero = Label (ventana, text="1er numero", font= "arial 9", background="black", foreground="white")
primer_numero.grid(row=0, column=0,padx= 10, pady= 15)

segundo_numero = Label (ventana, text="2do numero", font= "arial 9", background="black", foreground="white")
segundo_numero.grid(row=1, column=0,padx= 10, pady= 15)

result = Label (ventana, text="Resultado", font= "arial 9", background="black", foreground="white")
result.grid(row=2, column=0,padx= 10, pady= 15)


pantalla1 = Entry (ventana, textvariable=into, bg= "white", justify="center")
pantalla1.grid (row= 0, column= 1, padx= 10, pady= 15)


pantalla2 = Entry (ventana, textvariable= into2, bg= "white", justify="center")
pantalla2.grid (row= 1, column= 1, padx= 10, pady= 15)



"=================================================botones=================================================================="

boton_mas= Button(ventana, text="+", width= 17, height=1, command= suma)
boton_mas.grid(row=4, column= 0, padx= 10, pady= 15)

boton_x= Button(ventana, text="*", width= 17, height=1, command= multiplicacion)
boton_x.grid(row=5, column= 0, padx= 10, pady= 15)

boton_porcentaje= Button(ventana, text="%", width= 17, height=1, command= porcentaje)
boton_porcentaje.grid(row=6, column= 0, padx= 10, pady= 15)

boton_menos= Button(ventana, text="-", width= 17, height=1, command= resta)
boton_menos.grid(row=4, column= 1, padx= 10, pady= 15)

boton_div= Button(ventana, text="/", width= 17, height=1, command= division)
boton_div.grid(row=5, column= 1, padx= 10, pady= 15)

boton_clear= Button(ventana, text="CLEAR", width= 17, height=1, command= clear)
boton_clear.grid(row=6, column= 1, padx= 10, pady= 15)


resultado = Label (ventana, textvariable= var, font= "arial 9", background="white", foreground="black", width= 17, height= 0)
resultado.grid(row=2, column=1, padx= 10, pady= 15)






ventana.mainloop()
