class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona1 = Persona("Ana", 25)
print(persona1.presentarse())