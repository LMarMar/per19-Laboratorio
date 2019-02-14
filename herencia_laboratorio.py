class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    
class Medicamento(Producto):
    def __init__(self, nombre, precio, composicion, porcentaje):
        self.nombre = nombre
        self.precio = precio
        self.composicion = composicion
        self.porcentaje = porcentaje
    def get_composicion(self):
        return self.composicion
    def get_porcentaje(self):
        return self.porcentaje
productos = []
prod1 = Producto('pañales', 10)
prod2 = Producto('crema facial', 20)
prod3 = Medicamento('aspirina', 15, 'ácido oxalacético', 0.2)
prod4 = Medicamento('dalsy', 25, 'ibuprofeno', 0.3)
productos.append(prod1)
productos.append(prod2)
productos.append(prod3)
productos.append(prod4)

class Laboratorio():
    def __init__(self, nombre, prod1,prod2,prod3,prod4):
        self.nombre = nombre
        self.prod1 = prod1
        self.prod2 = prod2
        self.prod3 = prod3
        self.prod4 = prod4
    def get_nombre(self):
        return self.nombre
    def get_productos(self):
        return self.prod1,self.prod2,self.prod3,self.prod4
lab = Laboratorio('Bayern', productos[0],productos[1],productos[2],productos[3])

print('El laboratorio', lab.get_nombre(), 'tiene diferentes productos.')
print('Algunos de ellos son:', lab.prod1.nombre,',',lab.prod2.nombre,',',lab.prod3.nombre,',',lab.prod4.nombre)
print('EL', lab.prod1.get_nombre(), 'vale', lab.prod1.get_precio(), 'euros')
print('EL', lab.prod2.nombre, 'vale', lab.prod2.precio, 'euros')
print('EL', lab.prod3.nombre, 'vale', lab.prod3.precio, 'euros. Está compuesto por un', lab.prod3.porcentaje, '% de', lab.prod3.composicion)
print('EL', lab.prod4.nombre, 'vale', lab.prod4.precio, 'euros. Está compuesto por un', lab.prod4.porcentaje, '% de', lab.prod4.composicion)
