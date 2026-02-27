import tkinter as tk

def ventana_principal():

    global ven
    ven = tk.Tk()
    ven.title("Ventana principal")
    ven.geometry("600x400")
    ven.config(bg="pink")

    eti1=tk.Label(ven, text="Esta es la ventana principal")
    eti1.pack()

    boton=tk.Button(ven, text="Ventana 2", command=ventana_2)
    boton.pack(pady=20)

    boton2=tk.Button(ven, text="Ventana 3", command=ventana_3)
    boton2.pack(pady=20)

    boton3=tk.Button(ven, text="Ventana 4", command=ventana_4)
    boton3.pack(pady=20)

    boton4=tk.Button(ven, text="Ventana 5", command=ventana_5)
    boton4.pack(pady=20)

    ven.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana_2():

    ven.destroy()
    ven2 = tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("500x200")
    ven2.config(bg="pink")

    eti2=tk.Label(ven2, text="Esta es la ventana dos")
    eti2.pack()

    boton2=tk.Button(ven2, text="Ventana principal", command=lambda:destruir_ventana(ven2))
    boton2.pack(pady=20)

    ven2.mainloop()

def ventana_3():
    ven.destroy()
    ven3 = tk.Tk()
    ven3.title("Ventana tres")
    ven3.geometry("500x200")
    ven3.config(bg="pink")

    eti3=tk.Label(ven3, text="Esta es la ventana tres")
    eti3.pack()

    boton3=tk.Button(ven3, text="Ventana principal", command=lambda:destruir_ventana(ven3))
    boton3.pack(pady=20)

    ven3.mainloop()

def ventana_4():
    ven.destroy()
    ven4 = tk.Tk()
    ven4.title("Ventana cuatro")
    ven4.geometry("500x200")
    ven4.config(bg="pink")

    eti4=tk.Label(ven4, text="Esta es la ventana cuatro")
    eti4.pack()

    boton4=tk.Button(ven4, text="Ventana principal", command=lambda:destruir_ventana(ven4))
    boton4.pack(pady=20)

    ven4.mainloop()

def ventana_5():
    ven.destroy()
    ven5 = tk.Tk()
    ven5.title("Ventana cinco")
    ven5.geometry("500x200")
    ven5.config(bg="pink")

    eti5=tk.Label(ven5, text="Esta es la ventana cinco")
    eti5.pack()

    boton5=tk.Button(ven5, text="Ventana principal", command=lambda:destruir_ventana(ven5))
    boton5.pack(pady=20) 

    ven5.mainloop()

ventana_principal()