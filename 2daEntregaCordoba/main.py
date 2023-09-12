from paquete1.clases import Cliente
from paquete1.modulo2 import *

cliente1 = Cliente("Leo", 24, "leoocordoba@gmail.com", 2235123456, "Ayacucho 7800")

cliente1.comprar("Celular", 20000)

cliente1.cuantas_cuotas("asdas")

cliente1.envio()

print(cliente1)
