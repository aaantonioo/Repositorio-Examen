

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

# Función principal
def principal():
    vegetariana = Vegetarianas("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    no_vegetariana = NoVegetarianas("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    Utilidades.imprimir_receta(vegetariana)
    Utilidades.imprimir_receta(no_vegetariana)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingredientes in vegetariana.ingredientes:
        print(f"* {ingredientes}")
    
    print("Ingredientes de Pollo al horno:")
    for ingredientes in no_vegetariana.ingredientes:
        print(f"* {ingredientes}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
