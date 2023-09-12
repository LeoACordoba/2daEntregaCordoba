import json

def registro(diccionario): #funcion para registrar usuarios nuevos

    usuario = input("Ingrese Usuario: ")
    contraseña = input("Ingrese Contraseña: ")
    diccionario[usuario] = contraseña
    
def leerData(diccionario): #funcion para leer datos almacenados
    
        print("La informacion almacenada en la base de datos es: ")
        for clave, valor in diccionario.items():
            print(clave, valor)    
      
          
def guardarArchivo(diccionario): #funcion para guardar archivo en json

    with open("/BaseDeDatos.json", "w" ) as file:
      json.dump(diccionario, file, indent=4)        
      
def login(diccionario): #funcion para loguear 

    usuario = input("Ingrese Usuario: ")

    if usuario in diccionario:
        contraseña = input("Ingrese Contraseña: ")

        if diccionario[usuario] == contraseña:
                print("Inicio de sesión exitoso.")
        else:
                print("Contraseña incorrecta.")
    else:
            print("Nombre de usuario no encontrado.")
            