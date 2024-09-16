class ColaSimple:
    def __init__(self, max_size):
        self.max = max_size
        self.C = [None] * (self.max + 1)
        self.back = 0
        self.front = 0

    def es_vacia(self):
        return self.back == self.front

    def es_llena(self):
        return (self.back + 1) % (self.max + 1) == self.front

    def enqueue(self, dato):
        if not self.es_llena():
            self.C[self.back] = dato
            self.back = (self.back + 1) % (self.max + 1)
        else:
            print("La cola está llena")

    def dequeue(self):
        if not self.es_vacia():
            dato = self.C[self.front]
            self.front = (self.front + 1) % (self.max + 1)
            return dato
        else:
            print("La cola está vacía")
            return None

    def mostrar(self):
        if self.es_vacia():
            print("La cola está vacía")
        else:
            i = self.front
            while i != self.back:
                print(self.C[i], end=" ")
                i = (i + 1) % (self.max + 1)
            print()

# Ejemplo de uso
cola = ColaSimple(5)
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.mostrar()  # Salida: 1 2 3
cola.dequeue()
cola.mostrar()  # Salida: 2 3
