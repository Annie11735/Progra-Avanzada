import tkinter as tk
from backend import *
from tkinter import messagebox

def ventana_principal():

    ven = tk.Tk()
    ven.title("Base de datos")
    ven.geometry("600x400")

    Usuario.cargar_usuarios()

    etiq1=tk.Label(ven,text="Nombre")
    etiq1.pack()
    entrada1=tk.Entry(ven, width=40)
    entrada1.pack(pady=15)

    etiq2=tk.Label(ven,text="Edad")
    etiq2.pack()
    entrada2=tk.Entry(ven, width=40)
    entrada2.pack(pady=15)

    etiq3=tk.Label(ven,text="Contraseña")
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

def ventana_login():
    ven2 = tk.Tk()
    ven2.title("Base de datos")
    ven2.geometry("600x400")
    Usuario.cargar_usuarios()
    
    etiqueta3=tk.Label(ven2, text="Usuario")
    etiqueta3.pack()
    entrada4=tk.Entry(ven2, width=60)
    entrada4.pack(pady=10)
    etiqueta4=tk.Label(ven2, text="Password")
    etiqueta4.pack(pady=10)
    entrada5=tk.Entry(ven2, width=60)
    entrada5.pack(pady=10)
    def iniciar():
        name=entrada4.get()
        password=entrada5.get()
        for x in Usuario.lista:
            if name==x.nombre:
                if password==x.contra:
                    ventana_principal
            else:
                messagebox.showwarning("inicio de sesión", "El usuario no existe")
    boton4=tk.Button(ven2,text="Iniciar sesión", command=iniciar)
    boton4.pack()

    ven2.mainloop()

ventana_login()