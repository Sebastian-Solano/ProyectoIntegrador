//ITSCO
//AUTOR: SOLANO TORRES SEBASTIAN
//FECHA: 5/5/25
//DEBER N°1
Algoritmo CreacionContraseña
	Definir letraA, letraN, nombre, apellido, cedula, edad, fNacimiento como cadena
	Definir contN, contA, digito Como Entero
	
	Escribir "Bienvenido a la creacion de su nueva clave"
	
	Escribir Sin Saltar"Ingrese su nombre: "
	Leer nombre
	Escribir Sin Saltar"Ingrese su apellido: "
	Leer apellido
	Escribir Sin Saltar"Ingrese su cedula: "
	Leer cedula
	Escribir Sin Saltar"Ingrese su edad: "
	Leer edad
	Escribir Sin Saltar"Ingrese su fecha de nacimiento(dd-mm-aaaa) : "
	Leer fNacimiento
	
	contN= trunc(Longitud(nombre)/2)
	letraN=Mayusculas(Subcadena(nombre,contN+1,contN+1))
	contA=Longitud(apellido)
	letraA=Mayusculas((Subcadena(apellido,contA-1,contA-1)))
	digito=Aleatorio(1000,9999)
	Escribir "Su contaseña es: ",Subcadena(nombre,contN,contN),letraN,letraA,Subcadena(apellido,contA,contA),Subcadena(cedula,9,9),Subcadena(edad,1,1),Subcadena(fNacimiento,3,6),digito
	
FinAlgoritmo
