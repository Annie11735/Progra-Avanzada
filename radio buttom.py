import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("Opcion", "Elegiste los tacos")
    elif var.get==2:
        messagebox.showinfo("Opción", "Elegiste a las chanclas")
    elif var.get==3:
        messagebox.showinfo("Opción", "Elegiste la milanesa")  
    elif var.get==4:
        messagebox.showinfo("Opción", "Elegiste a la pizza")
    else:
        messagebox.showinfo("Opción", "No sellecionaste nada")

ven2 =tk.Tk()
ven2.title("Uso del radio buttom")
ven2.geometry("600x500")

etiqueta1=tk.Label(ven2, text="¿Cuál es tu comida favoria")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ven2, text="Tacos", variable=var, value=1)
rad1.pack()

rad2=tk.Radiobutton(ven2, text="Chanclas", variable=var, value=2)
rad2.pack()

rad3=tk.Radiobutton(ven2, text="Milanesa", variable=var, value=3)
rad3.pack()

rad4=tk.Radiobutton(ven2, text="Pizzas", variable=var, value=4)
rad4.pack()

boton1=tk.Button(ven2, text="Verificar", command=opcion)
boton1.pack(pady=30)

ven2.mainloop()