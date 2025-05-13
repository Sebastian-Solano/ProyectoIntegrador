//ITSCO
//AUTOR: SOLANO TORRES SEBASTIAN
//FECHA: 5/5/25
//DEBER N°1
Algoritmo SegundosHoras
	Definir nSegundos,horas, minutos,seg Como entero
	
	
	Escribir "Bienvenidos al sistema"
	Escribir "Re-estructuracion de hora"
    Escribir "Ingresa la cantidad de segundos:"
    Leer nSegundos
	
    horas <- trunc(nSegundos / 3600)
    minutos <- trunc((nSegundos MOD 3600) / 60)
    seg <- nSegundos MOD 60
	
    Escribir "El tiempo es: ", horas, " horas ", minutos, " minuto ", seg, " segundo"
FinAlgoritmo
