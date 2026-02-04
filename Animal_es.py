#Clase padre
class Animales:
    def __init__ (self, nombre, color, patas)
        self.nombre=nombre
        self.color=color
        self.patas=patas

class Conejo (Animales):
    def __init__ (self, nombre, color, patas)
        super():__init__(nombre,color,patas)
        
    def caract(self):
        print(f"Mi conejo se llama {self.nombre}, es color {self.color} y tiene {self.patas}")

    def sonido (self):
        print("Squick squick")

class Ornitorrinco(Animales):
    def __init__ (self, nombre, color, patas,tamañoPico)
        super():__init__(nombre,color,patas)
        self.tamañoPico=tamañoPico

    def caract(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es color {self.color}, tiene {self.patas} y si pico mide {self.tamañoPico}")

    def sonido (self):
        print("Grrrrr")

#class Dinosaurio(Animales):
    