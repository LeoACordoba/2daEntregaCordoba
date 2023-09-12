class Persona:
    def __init__(self,nombre,edad): #clase padre
        self.nombre = nombre
        self.edad = edad
        
class Cliente(Persona): #clase hija
    def __init__(self, nombre, edad, correo, celular, direccion): 
        self.nombre = nombre  
        self.edad = edad  
        self.correo = correo  
        self.celular = celular  
        self.direccion = direccion  
    def __str__(self):
        return f"Se ha creado el cliente {self.nombre}" 
    
    def comprar(self,objeto,precio): #metodo para comprar
        print(f"El Cliente {self.nombre} compro {objeto} al precio de: {precio}")
    
    def cuantas_cuotas(self, cuotas): #metodo para saber si pago en cuotas
        try:
            if int(cuotas) == 0 :
                print(f"El cliente {self.nombre} pago en efectivo")
            else:
                print (f"El cliente {self.nombre} compro en {cuotas} cuotas")      
        except:
            print("Debe asignar un numero al atributo cuotas")
        
        
    def envio(self): #metodo para envio a domicilio
        print(f"El cliente {self.nombre} quiere que su paquete sea enviado a su domicilio en {self.direccion}")        