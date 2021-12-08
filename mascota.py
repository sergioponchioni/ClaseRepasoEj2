class Mascota:
    def __init__(self, tipo, color):
        self.tipo= tipo
        self.color= color
    
    def mostrar(self):
        print(f"Tipo ---> {self.tipo}")
        print(f"Color ---> {self.color}")
    