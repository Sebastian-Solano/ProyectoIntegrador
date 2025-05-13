//ITSCO
//AUTOR: SOLANO TORRES SEBASTIAN
//FECHA: 5/5/25
//DEBER N°1
Algoritmo AreaYVolumen
	Definir area, vol, r, h Como Real
	
	Escribir "Calculo del area y volumen del cilindro"
	Escribir Sin Saltar"Ingrese el radio del cilindro"
	leer r
	Escribir Sin Saltar"Ingrese la altura del cilindro"
	leer h
	
	vol=pi*(r^2)*h
	area= (2*pi*r*h)+(2*pi*r^2)
	
	Escribir "El area de cilindro es: ", area," el volumen es: ", vol
	
FinAlgoritmo
