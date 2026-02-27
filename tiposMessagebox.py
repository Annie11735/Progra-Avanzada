import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var.get()==1:
        messagebox.showinfo("Ventana de información", "Información del ususario")
    elif var.get()==2:
        messagebox.showinfo("Ventana de advertencia", "¡¡¡Advertencia!!!")
    elif var.get()==3:
        messagebox.showinfo("Ventana de error", "Error")
    elif var.get()==4:
        respuesta = messagebox.askyesno("Ventana de información", "¿Te gusta esta clase?")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta", "Mas te vale")
        else:
            messagebox.showinfo("Ventana de respuesta", "Por eso vas a reprobar")
    elif var.get()==5:
        respuesta = messagebox.askyesno("Ventana de opción", "¿Das tu alma a esta clase?")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta", "Por eso vas a sacar 10")
        else:
            messagebox.showinfo("Ventana de respuesta", "Por eso repruebas")
    else:
        messagebox.showinfo("Ventana de respuesta", "No elegiste ninguna opción")

ven = tk.Tk() #creacion de la ventana
ven.title("Tipos de messagebox")
ven.geometry("400x500")

etiqueta1=tk.Label(ven, text="Veremos el uso de las massagebox")
etiqueta1.pack()

var=tk.IntVar() #definicion de la variable
rad1=tk.Radiobutton(ven, text="Mostrar información", variable=var, value=1)
rad1.pack(pady=20)

rad2=tk.Radiobutton(ven, text="Advertencia", variable=var, value=2)
rad2.pack(pady=20)

rad3=tk.Radiobutton(ven, text="Error", variable=var, value=3)
rad3.pack(pady=20)

rad4=tk.Radiobutton(ven, text="Si o no", variable=var, value=4)
rad4.pack(pady=20)

rad5=tk.Radiobutton(ven, text="Aceptar o cancelar", variable=var, value=5)
rad5.pack(pady=20)

boton1=tk.Button(ven, text="Sacar ventana", command=ventanas)
boton1.pack(pady=30)

ven.mainloop()
