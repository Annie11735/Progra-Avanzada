import tkinter as tk
from backend import *
from tkinter import messagebox
    
ven = tk.Tk()
ven.title("Base de datos")
ven.geometry("600x400")

etiq1=tk.Label(ven,text="Nombre")
etiq1.pack()
entrada1=tk.Entry(ven, width=40)
entrada1.pack(pady=15)

etiq2=tk.Label(ven,text="Edad")
etiq2.pack()
entrada2=tk.Entry(ven, width=40)
entrada2.pack(pady=15)

etiq3=tk.Label(ven,text="Comida favorita")
etiq3.pack()
entrada3=tk.Entry(ven, width=40)
entrada3.pack(pady=15)

def registrar():
    name=entrada1.get()
    age=entrada2.get()
    food=entrada3.get()
    newuser=Usuario(name,age,food)
    entrada1.delete(0,tk.END)
    entrada2.delete(0,tk.END)
    entrada3.delete(0,tk.END)
    messagebox.showinfo("Registro de usuario", "Tu registro fué exitoso")


#var=tk.IntVar()
boton1=tk.Button(ven, text="Registrar", command=registrar)
boton1.pack(pady=10)
def mostrar():
    Usuario.mostrar_lista()

boton1=tk.Button(text="Mostrar lista",command=mostrar)
boton1.pack(pady=10)

def al_cerrar():
    print("Guardar datos antes de salir...")
    Usuario.guardar_usuarios()
    ven.destroy()

ven.protocol("WM_DELETE_WINDOW", al_cerrar)

ven.mainloop()