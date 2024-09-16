class ColaSimple:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * (self.max + 1)
        self.front = 0
        self.back = 0

    def es_vacia(self):
        return self.front == 0 and self.back == 0
    
    def es_llena(self):
        return self.back == self.max
    
    def size(self):
        return self.back - self.front
    
    def enqueue(self, elemento):
        if not self.es_llena():
            self.back += 1
            self.cola[self.back] = elemento
        else:
            print("cola llena...")
    
    def dequeue(self):
        elemento = None
        if not self.es_vacia():
            self.front += 1
            elemento = self.cola[self.front]

            if self.front == self.back:
                self.front = 0 
                self.back = 0
        else:
            print("cola vacia...")
        return elemento
    
    def mostrar(self):
        if self.es_vacia():
            print("cola vacia...")
        else:
            print("Números en la cola:", self.cola[self.front + 1:self.back + 1])
            print("Números pares en la cola:", [num for num in self.cola[self.front + 1:self.back + 1] if num % 2 == 0])

cola1 = ColaSimple(10)

# Ingresar números por teclado
numeros = input("Ingrese números separados por espacio: ").split()
for num in numeros:
    cola1.enqueue(int(num))

cola1.mostrar()
