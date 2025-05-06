//ITSCO
//AUTOR: SOLANO TORRES SEBASTIAN
//FECHA: 5/5/25
//DEBER N°1
Algoritmo PlanillaEmpleado
	Definir horas como entero
	Definir tarifHora, planilla Como Real
	
	Escribir "Bienvenido"
	Escribir "Calculo de la planilla mensual"
	Esperar 1 Segundos
	Limpiar Pantalla
	Escribir Sin Saltar "ingrese el numero de horas trabajadas en el mes"
	Leer horas
	Escribir Sin Saltar"Ingrese el costo de la hora: "
	Leer tarifHora
	
	planilla=horas*tarifHora
	Escribir "El valor de la planilla es: ", planilla
	
FinAlgoritmo
