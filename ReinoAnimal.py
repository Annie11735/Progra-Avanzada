import tkinter as tk
from PIL import Image, ImageTk

def ventana_principal():
    global ven
    ven = tk.Tk()
    ven.title("Reino Animal")
    ven.geometry("600x400")
    ven.config(bg="pink")

    etiqueta1=tk.Label(ven, text="El Reino Animal")
    etiqueta1.grid(row=0, column=0, padx=5, pady=5)

    imagen=Image.open("C:/Users/DELL/Documents/Estefania/Ventanas/ReinoAnimal/rein_anim")
    imagen=imagen.resize((400, 200))
    imagen_tk= ImageTk.PhotoImage(imagen)
    imagen_tk =ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(ven,image=imagen_tk)
    label_imagen.grid(row=1, column=0, padx=5, pady=5)


    var=tk.IntVar()
    rad1=tk.Radiobutton(ven, text="Elefante", variable=var, value=1)
    rad1.grid(row=2, column=0, padx=5, pady=5)

    rad1=tk.Radiobutton(ven, text="Jirafa", variable=var, value=3)
    rad1.grid(row=2, column=0, padx=5, pady=5)

    rad1=tk.Radiobutton(ven, text="Castor", variable=var, value=3)
    rad1.grid(row=3, column=0, padx=5, pady=5)

    rad1=tk.Radiobutton(ven, text="León", variable=var, value=4)
    rad1.grid(row=4, column=0, padx=5, pady=5)
"""
    def info():
        if var.get()==1:
            ventana_2()



    ven.mainloop()

def ventana_2():

    ven.destroy()
    ven2 = tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("500x200")
    ven2.config(bg="pink")

    ven2.mainloop()

def ventana_3():
    ven.destroy()
    ven3 = tk.Tk()
    ven3.title("Ventana tres")
    ven3.geometry("500x200")
    ven3.config(bg="pink")

"""
ventana_principal()