import csv
import os

class Usuario():
    lista=[]
    ruta_csv=r"C:/Users/DELL/Documents/Estefania/Ventanas/06-03-26/base2/personas.csv"

    def __init__(self, name,age, food):
        self.nombre=name
        self.edad=age
        self.comida=food
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrar_datos(self):
        return f"El usuario {self.nombre} tiene {self.edad} y le gusta {self.comida}"
    
    @classmethod #método de clase
    def mostrar_lista(cls):
        for u in Usuario.lista:
            print (u.mostrar_datos())
        
    @classmethod
    def guardar_usuarios(cls):
        campos=["nombre","edad","comida"] #nombres de las columnas de la tabla

        directorio = os.path.dirname(cls.ruta_csv)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                print(f"Directorio creado: {directorio}")
            except Exception as e:
                print(f"Error al crear directorio: {e}")
                return False
            
        #Guardar archivo
        with open(cls.ruta_csv,"w",newline='',encoding="utf-8") as f:
            escritor=csv.DictWriter(f, fieldnames=campos, delimiter=',')
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre":u.nombre,"edad":u.edad,"comida":u.comida})


