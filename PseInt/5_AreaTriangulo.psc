//ITSCO
//AUTOR: SOLANO TORRES SEBASTIAN
//FECHA: 5/5/25
//DEBER N°1
Algoritmo AreaTriangulo
	Definir a,b,c, semiP, area como real
	
	Escribir "Calculo del area de un triangulo"
	
	Escribir Sin Saltar "Ingrese el primer lado del triangulo: "
	Leer a
	Escribir Sin Saltar"Ingrese el segundo lado del triangulo: "
	Leer b
	Escribir Sin Saltar"Ingrese el tercer lado del triangulo: "	
	Leer c
	semiP=(a+b+c)/2
	area=((semiP*(semiP-a)*(semiP-b)*(semiP-c)))^(1/2)
	
	Escribir "El area del triangulo es: ", area," metros cuadrados"
	
FinAlgoritmo
