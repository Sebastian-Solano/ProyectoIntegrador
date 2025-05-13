//ITSCO
//AUTOR: SOLANO TORRES SEBASTIAN
//FECHA: 5/5/25
//DEBER N°1
Algoritmo NotaExamen
	Definir pregCor, pregInc, total Como Real
	
	Escribir "Programa para el calculo de notas"
	Esperar 1 Segundos
	Limpiar Pantalla
	Escribir Sin Saltar"Ingrese el numero de aciertos: "
	Leer pregCor
	Escribir Sin Saltar"Ingrese el numero de pruntas incorrectas: "
	Leer pregInc
	
	total=(pregCor*4)+(pregInc*(-1))
	Escribir "La nota final del examen es: ", total
	
FinAlgoritmo
