import random
class Proceso:
    
    def __init__(self, cant):
        self.nombre = "proceso #" , cant
        self.ram = random.randint(1,10)
        self.instrucciones = random.randint(1,10)

    def solicitarMemoria(self):
        return self.ram
    

        

