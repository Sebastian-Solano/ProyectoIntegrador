'''
Elaborar un ejercicios que pida la siguiente informacion al cliente:
1)Nombres
2)Apellidos
3)Edad
4)Direccion
5)Fecha actual
6)Tres Productos

y mostrar en pantalla de la siguiente manera

*-----------------------------------------------*
|   Nombre Completo: ------------------------   |
|   Fecha: -------------- Edad: -------------   |
|   Direccion: ------------------------------   |
-------------------------------------------------
|                  PRODUCTOS                    |
|        1) Nombre: "------", Precio: -----$    |
|        2) Nombre: \------\, Precio: -----$    |
|        3) Nombre: '------', Precio: -----$    |
|-----------------------------------------------|
|                               |SubTotal: ---- |
|                               |Iva:   ------- |
|                               |Total: ------- |
*-----------------------------------------------*    

el objetivo del sistema es que el alumno encuentre la manera de mostrar el diseño con la informacion ingresada sin que se descuadre dicho diseño para lo cual debera investigar un modo que le permita realizar dicho proceso
Nota: se recomienda investigar el print con formato.
'''
# ESCRIBE LA SOLUCION AQUI

# Solicitar datos al cliente
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
fecha = input("Ingrese la fecha actual (dd/mm/aaaa): ")

# Ingreso de productos
productos = []
for i in range(1, 4):
    nombre_prod = input(f"Ingrese el nombre del producto {i}: ")
    precio_prod = float(input(f"Ingrese el precio del producto {i}: "))
    productos.append((nombre_prod, precio_prod))

# Cálculos
subtotal = sum([precio for _, precio in productos])
iva = subtotal * 0.12  # IVA del 12%
total = subtotal + iva

# Impresión formateada
print("*" + "-" * 47 + "*")
print(f"|   Nombre Completo: {nombre} {apellido:<24}|")
print(f"|   Fecha: {fecha:<15} Edad: {edad:<14}|")
print(f"|   Direccion: {direccion:<30}|")
print("-" * 49)
print(f"|{'PRODUCTOS':^47}|")

# Productos con distintos tipos de comillas
tipos_comillas = ['"', '\\', "'"]

for i, (prod, precio) in enumerate(productos):
    prod_formateado = f'{tipos_comillas[i]}{prod}{tipos_comillas[i]}'
    print(f"|   {i+1}) Nombre: {prod_formateado:<15} Precio: {precio:7.2f}$   |")

print("|" + "-" * 47 + "|")
print(f"|{'':33}|SubTotal: {subtotal:7.2f} |")
print(f"|{'':33}|Iva:      {iva:7.2f} |")
print(f"|{'':33}|Total:    {total:7.2f} |")
print("*" + "-" * 47 + "*")
