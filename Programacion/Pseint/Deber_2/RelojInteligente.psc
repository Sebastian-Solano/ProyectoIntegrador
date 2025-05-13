Proceso RelojInteligente
	Definir frecuenciaCardiaca, nivelOxigeno, temperaturaCorporal Como Real
    Definir activarVibracion, mostrarNotificacion, enviarAlertaEmergencia Como Logico
	Definir user,pass,userAdm,passAdm como cadena
	userAdm="Sebastian"
	passAdm="09062000"

    Escribir "--------------------------------------------"
    Escribir "   Bienvenido al Reloj Inteligente de Salud"
    Escribir "--------------------------------------------"
    Escribir ""
    Escribir "Este sistema simula las funciones de un reloj"
    Escribir "que monitorea tus signos vitales y activa alertas"
    Escribir "cuando detecta valores anormales."
    Escribir ""
    Escribir "Funciones que puede activar:"
    Escribir "- Vibración por frecuencia cardíaca irregular"
    Escribir "- Notificación por bajo nivel de oxígeno"
    Escribir "- Alerta de emergencia por fiebre alta"
    Escribir "--------------------------------------------"
    Escribir ""
    Esperar 1 Segundos
	
	Escribir Sin Saltar"Ingrese el usuario: "
	Leer user
	escribir Sin Saltar"Ingrese la contraseña(ddmmaaaa): "
	Leer pass
	Limpiar Pantalla
	
	si (pass=passAdm)y(user=userAdm) Entonces
		Escribir "<----------Bienvenido al sistema-------------------->"
		Escribir "!-----",user,"-----¡"
		Esperar 1 Segundos
		Escribir "Ingrese la frecuencia cardíaca (latidos por minuto):"
		Leer frecuenciaCardiaca
		
		Escribir "Ingrese la saturación de oxígeno (%):"
		Leer nivelOxigeno
		
		Escribir "Ingrese la temperatura corporal (°C):"
		Leer temperaturaCorporal
		
		activarVibracion <- FALSO
		mostrarNotificacion <- FALSO
		enviarAlertaEmergencia <- FALSO
		
		Si frecuenciaCardiaca < 50 o frecuenciaCardiaca > 110 Entonces
			activarVibracion <- VERDADERO
		FinSi
		
		Si nivelOxigeno < 92 Entonces
			mostrarNotificacion <- VERDADERO
		FinSi
		
		Si temperaturaCorporal > 38.5 Entonces
			enviarAlertaEmergencia <- VERDADERO
		FinSi
		
		Escribir ""
		Escribir "--------------------------------------------"
		Escribir "Estado del reloj inteligente:"
		Escribir ""
		
		Si activarVibracion Entonces
			Escribir "- Vibración activada por frecuencia cardíaca anormal."
		FinSi
		
		Si mostrarNotificacion Entonces
			Escribir "- Notificación mostrada por bajo nivel de oxígeno."
		FinSi
		
		Si enviarAlertaEmergencia Entonces
			Escribir "- Alerta enviada a contacto de emergencia por fiebre alta."
		FinSi
		
		Si No activarVibracion y No mostrarNotificacion y No enviarAlertaEmergencia Entonces
			Escribir "- Todos los signos vitales están en rangos normales. Sin alertas."
		FinSi
		
		Escribir "--------------------------------------------"
		Escribir "Gracias por usar el Reloj Inteligente de Salud."
		Escribir "Mantente saludable :)"
		Escribir "--------------------------------------------"
	SiNo
		Escribir "Eroro en la digitacion de usuario y contraseña"
	finSi
FinProceso
