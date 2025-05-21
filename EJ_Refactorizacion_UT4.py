

# Clase abstracta para representar una receta
class Receta():
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingredientes in self.ingredientes:
            print(f"- {ingredientes}")
        print("Pasos:")
        for pasos in self.pasos:
            print(f"{pasos}")


# Clase para recetas vegetarianas
class Vegetarianas(Receta):
    def __init__(self, nombre, ingredientes, pasos):
        super().__init__(nombre, ingredientes, pasos)
        


# Clase para recetas no vegetarianas
class NoVegetarianas(Receta):
    def __init__(self, nombre, ingredientes, pasos):
        super().__init__(nombre, ingredientes, pasos)
        

# Clase con utilidades del restaurante
class Utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for list in lista:
            print(f"* {list}")
    

def crear_receta():
    nombre = str(input("Dime el nombre de tu receta: "))
    ingredientes = []
    print("Introduce todos los ingredientes: (escribe fin para terminar)")
    while True:
        ingrediente = str(input("Dime un ingrediente: "))
        if ingrediente.lower() == "fin":
            break
        ingredientes.append(ingrediente)
    
    pasos =[]
    print("Introduce los pasos necesarios para hacerlo: (escribe fin para terminar)")
    
    while True:
        paso = str(input("Dime los pasos que tiene: "))
        if paso.lower() == "fin":
            break
        pasos.append(paso)
    return nombre, ingredientes, pasos

    

# Función principal
def principal():
    nombre, ingredientes, pasos = crear_receta()

    tipo = str(input("Dime que tipo de receta quieres crear Vegetariana /Carnivora "))

    if tipo.lower() == "vegetariana":
        print("Receta Creada 1 (Vegetariana)")
        receta1 = Vegetarianas(nombre,ingredientes,pasos)
        Utilidades.imprimir_receta(receta1)
    elif tipo.lower() == "carnivora":
        print("Receta Creada 2 (Carnivora)")
        receta2 = NoVegetarianas(nombre,ingredientes,pasos)
        Utilidades.imprimir_receta(receta2)
    else:
        print("El tipo de receta no es el correcto")
    

# Ejecutar el programa
if __name__ == "__main__":
    principal()
