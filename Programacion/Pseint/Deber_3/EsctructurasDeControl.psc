Algoritmo EsctructurasDeControl
	Definir op, tam,dia,mes,anio,conf,totalDia,continuar,edad,regalo,total,menores15,mayores50,	entre25y45, num Como Entero
	Definir Pcoste,pvp,nun1,nun2,diferencia,i,j,producto como real
	Definir Fnac,signoZ,val como cadena
	Definir ban,bisiesto Como Logico
	
	Repetir
		Escribir "|�����������������������������������|"
		Escribir "|       Bienvenido al sistema       |"
		Escribir "|-----------------------------------|"
		Escribir "|       Seleccione una opcione      |"
		Escribir "|-----------------------------------|"
		Escribir "|1.-    Papeleria                   |"
		Escribir "|2.-    Comprobar fecha             |"
		Escribir "|3.-    Signo zodiacal              |"
		Escribir "|4.-    Diferencia de numeros       |"
		Escribir "|5.-    Dia del a�o                 |"
		Escribir "|6.-    Multiplos de tres           |"
		Escribir "|7.-    Tablas de multiplicar       |"
		Escribir "|8.-    Factorial(while)            |"
		Escribir "|9.-    Promedio(while)             |"
		Escribir "|10.-   Numeros naturales           |"
		Escribir "|11.-   Regalo de cumplea�os        |"
		Escribir "|12.-   Salir                       |"
		Escribir "|___________________________________|"
		Leer op
		si op>=1 y op<=12 Entonces
			Segun op Hacer
				1:
					Limpiar Pantalla
					ban = Verdadero
					Mientras ban  Hacer
					Escribir "Papeleria"
					Escribir "Calculo del precio de venta al publico"
					Escribir Sin Saltar "Ingrese el precio de coste"
					Leer Pcoste
						si Pcoste<3 y pcoste>0 Entonces
							pvp=Pcoste+(0.15*Pcoste)
							Escribir "El precio de venta al publico es: ",pvp
							Esperar 1 Segundos
							ban = Falso
						FinSi
						si Pcoste>=3 y Pcoste<=6 Entonces
							pvp=Pcoste+0.5
							Escribir "El precio de venta al publico es: ",pvp
							Esperar 1 Segundos
							ban = Falso
						FinSi
						si Pcoste>6 y Pcoste<=100 Entonces
							pvp=Pcoste+(0.25*Pcoste)
							Escribir "El precio de venta al publico es: ",pvp
							Esperar 1 Segundos
							ban = Falso
						FinSi
						si Pcoste<=0 o Pcoste>=101 Entonces
							Escribir "El precio esta fuera de rango intente nuevamente"
							Esperar 1 Segundos
							Limpiar Pantalla
						FinSi
					Fin Mientras
					Esperar 1 Segundos
					Limpiar Pantalla
				2:
					Limpiar Pantalla
					ban = Verdadero
					
					Mientras ban Hacer
						Escribir "Comprobaci�n de la fecha"
						Escribir Sin Saltar "Ingrese la fecha de su cumplea�os (dd-mm-aaaa): "
						Leer Fnac
						
						tam = Longitud(Fnac)
						
						Si tam = 10 Entonces
							dia = ConvertirANumero(SubCadena(Fnac,1,2))
							mes = ConvertirANumero(SubCadena(Fnac,4,5))
							anio = ConvertirANumero(SubCadena(Fnac,7,10))
							
							Si (dia>=1 Y dia<=31) Y (mes>=1 Y mes<=12) Y (anio>0) Entonces
								Escribir "Datos validados"
								Esperar 1 Segundos
								Limpiar Pantalla
								
								bisiesto = Falso
								Si (anio mod 4 = 0) Y ((anio mod 100 <> 0) O (anio mod 400 = 0)) Entonces
									bisiesto = Verdadero
									Escribir "El a�o es bisiesto"
								FinSi
								
								Segun mes Hacer
									1,3,5,7,8,10,12:
										Si dia>=1 Y dia<=31 Entonces
											Escribir "Fecha v�lida con 31 d�as"
										SiNo
											Escribir "D�a fuera de rango"
											
										FinSi
									4,6,9,11:
										Si dia>=1 Y dia<=30 Entonces
											Escribir "Fecha v�lida con 30 d�as"
										SiNo
											Escribir "D�a fuera de rango"
											
										FinSi
									2:
										Si bisiesto Entonces
											Si dia>=1 Y dia<=29 Entonces
												Escribir "Fecha v�lida en febrero bisiesto"
											SiNo
												Escribir "D�a fuera de rango en febrero bisiesto"
												
											FinSi
										SiNo
											Si dia>=1 Y dia<=28 Entonces
												Escribir "Fecha v�lida en febrero"
											SiNo
												Escribir "D�a fuera de rango en febrero"
												
											FinSi
										FinSi
								FinSegun
								
								Escribir "La fecha ingresada (", dia, "-", mes, "-", anio, ") es v�lida."
								ban = Falso
							SiNo
								Escribir "Datos err�neos: d�a, mes o a�o fuera de rango"
								Esperar 1 Segundos
								Limpiar Pantalla
							FinSi
						SiNo
							Escribir "Dato err�neo. Por favor siga el formato dd-mm-aaaa"
							Esperar 1 Segundos
							Limpiar Pantalla
						FinSi
					FinMientras
					Escribir "Presiones una tecla para continuar"
					Esperar Tecla
					Limpiar Pantalla

				3:
					Limpiar Pantalla
					ban = Verdadero
					
					Mientras ban Hacer
						// Entrada y validaci�n b�sica de formato
						Mientras ban Hacer
							Escribir "Signo zodiacal"
							Escribir Sin Saltar "Ingrese la fecha de su cumplea�os (dd-mm-aaaa): "
							Leer Fnac
							tam = Longitud(Fnac)
							
							// Validar longitud esperada
							Si tam = 10 Entonces
								dia = ConvertirANumero(Subcadena(Fnac,1,2))
								mes = ConvertirANumero(Subcadena(Fnac,4,5))
								anio = ConvertirANumero(Subcadena(Fnac,7,10))
								
								si (dia >= 1 y dia <= 31) y (mes >= 1 y mes <= 12) y (anio > 0) Entonces
									// Validaci�n de d�as seg�n mes
									valido = Verdadero
									si mes = 2 Entonces
										bisiesto = (anio mod 4 = 0) y ((anio mod 100 <> 0) o (anio mod 400 = 0))
										si bisiesto Entonces
											si dia > 29 Entonces
												valido = Falso
											FinSi
										SiNo
											si dia > 28 Entonces
												valido = Falso
											FinSi
										FinSi
									SiNo
										Segun mes Hacer
											4, 6, 9, 11:
												si dia > 30 Entonces
													valido = Falso
												FinSi
											1, 3, 5, 7, 8, 10, 12:
												si dia > 31 Entonces
													valido = Falso
												FinSi
											De Otro Modo:
												valido = Falso
										FinSegun
									FinSi
									
									si valido Entonces
										Escribir "Fecha v�lida"
										ban = Falso
									SiNo
										Escribir "El d�a no es v�lido para el mes ingresado"
									FinSi
								SiNo
									Escribir "Fecha no v�lida. Revise los valores ingresados."
								FinSi
							SiNo
								Escribir "Formato incorrecto. Use (dd-mm-aaaa)"
							FinSi
							
							Esperar 1 Segundos
							Limpiar Pantalla
					FinMientras
						
						// Determinar el signo zodiacal
						Segun mes Hacer
							1:
								si dia <= 20 Entonces 
									signoZ = "Capricornio" 
								Sino 
									signoZ = "Acuario" 
								FinSi
							2:
								si dia <= 19 Entonces 
									signoZ = "Acuario" 
								Sino 
									signoZ = "Piscis" 
								FinSi
							3:
								si dia <= 20 Entonces 
									signoZ = "Piscis" 
								Sino 
									signoZ = "Aries" 
								FinSi
							4:
								si dia <= 19 Entonces 
									signoZ = "Aries" 
								Sino 
									signoZ = "Tauro" 
								FinSi
							5:
								si dia <= 20 Entonces 
									signoZ = "Tauro" 
								Sino 
									signoZ = "Geminis" 
								FinSi
							6:
								si dia <= 21 Entonces 
									signoZ = "Geminis" 
								Sino 
									signoZ = "Cancer" 
								FinSi
							7:
								si dia <= 21 Entonces 
									signoZ = "Cancer" 
								Sino 
									signoZ = "Leo" 
								FinSi
							8:
								si dia <= 21 Entonces 
									signoZ = "Leo" 
								Sino 
									signoZ = "Virgo" 
								FinSi
							9:
								si dia <= 22 Entonces 
									signoZ = "Virgo" 
								Sino 
									signoZ = "Libra" 
								FinSi
							10:
								si dia <= 22 Entonces 
									signoZ = "Libra" 
								Sino 
									signoZ = "Escorpio" 
								FinSi
							11:
								si dia <= 21 Entonces 
									signoZ = "Escorpio" 
								Sino 
									signoZ = "Sagitario"
								FinSi
							12:
								si dia <= 21 Entonces 
									signoZ = "Sagitario" 
								Sino 
									signoZ = "Capricornio"
								FinSi
					FinSegun
																		
						// Mostrar resultado
						Escribir "La fecha ", dia, "-", mes, "-", anio, " corresponde al signo: ", signoZ
						
						// Mostrar figura art�stica del signo
						Segun signoZ Hacer
							"Aries":
								Escribir "      \\    /"
								Escribir "       )  (  "
								Escribir "      /    \\"
								Escribir "     /      \\"
							"Tauro":
								Escribir "      (__)   (__)"
								Escribir "      (oo)   (oo)"
								Escribir "  /----\\/     \\/----\\"
								Escribir " / |  ||       ||  | \\"
								Escribir "*  ||--||-----||--||  *"
								Escribir "   ^^  ^^     ^^  ^^"
							"Geminis":
								Escribir "     ________"
								Escribir "    |   ||   |"
								Escribir "    |   ||   |"
								Escribir "    |   ||   |"
								Escribir "    |   ||   |"
								Escribir "    |___||___|"
							"Cancer":
								Escribir "     _     _"
								Escribir "  __(.)< __(.)<"
								Escribir "  \\___)  \\___)"
							"Leo":
								Escribir "      /^--^\\"
								Escribir "     ( o  o )"
								Escribir "     (  =^=  )"
								Escribir "     (        )"
								Escribir "     (         )"
								Escribir "     (          ))))))"
							"Virgo":
								Escribir "     /|\\"
								Escribir "    /_|_\\"
								Escribir "     ||"
								Escribir "     ||"
								Escribir "    /__\\"
							"Libra":
								Escribir "     _______"
								Escribir "    |       |"
								Escribir " ___|_______|___"
								Escribir " \\           /"
								Escribir "  \\_________/"
							"Escorpio":
								Escribir "     /\\_/\\"
								Escribir "    ( o.o )"
								Escribir "     > ^ <==<"
							"Sagitario":
								Escribir "        \\ | /"
								Escribir "         \\|/"
								Escribir "       --(*)-->"
								Escribir "         /|\\"
								Escribir "        / | \\"
							"Capricornio":
								Escribir "      (__)"
								Escribir "      (oo)"
								Escribir " /------\\/"
								Escribir "/ |    ||"
								Escribir "*  /\\---/\\"
							"Acuario":
								Escribir "     ~~~~~    ~~~~~"
								Escribir "   ~~~~~~    ~~~~~~"
								Escribir "     ~~~~    ~~~~"
							"Piscis":
								Escribir "     ><(((�>   <�)))><"
						FinSegun
						
						Escribir "Presione una tecla para continuar"
						Esperar Tecla
						Limpiar Pantalla
						ban = Falso
					FinMientras
					
					Esperar 1 Segundos
					Limpiar Pantalla
				
				4:
					Limpiar Pantalla
					ban = Verdadero
					
					Mientras ban Hacer
						Escribir "Diferencia entre dos n�meros"
						Escribir Sin Saltar "Ingrese el primer n�mero: "
						Leer nun1
						Escribir Sin Saltar "Ingrese el segundo n�mero: "
						Leer nun2
						
						diferencia = nun1 - nun2
						si diferencia < 0 Entonces
							diferencia = diferencia * (-1)
						FinSi
						
						si diferencia <= 10 Entonces
							Escribir "La diferencia entre los dos n�meros es menor o igual a 10"
							
							// Mostrar n�meros entre ellos, sin repetir l�gica
							si nun1 <= nun2 Entonces
								Para i = nun1 Hasta nun2 Con Paso 1
									Escribir i
								FinPara
							SiNo
								Para i = nun2 Hasta nun1 Con Paso 1
									Escribir i
								FinPara
							FinSi
						SiNo
							Escribir "La diferencia entre los dos n�meros es superior a 10: ", diferencia
						FinSi
						
						Escribir "�Desea salir? (1 = S�, 0 = No)"
						Leer conf
						si conf = 1 Entonces
							ban = Falso
						FinSi
						
						Limpiar Pantalla
					FinMientras
					
				5:
					Limpiar Pantalla
					ban = Verdadero
					Mientras ban Hacer
						validado = Falso
						
						// Validaci�n de fecha
						Mientras No validado Hacer
							Escribir "Conteo de d�as del a�o"
							Escribir "Ingrese su fecha de cumplea�os (dd-mm-aaaa): "
							Leer fnac
							tam = Longitud(fnac)
							
							dia = ConvertirANumero(Subcadena(fnac,1,2))
							mes = ConvertirANumero(Subcadena(fnac,4,5))
							anio = ConvertirANumero(Subcadena(fnac,7,10))
							
							si dia >= 1 y dia <= 31 y mes >= 1 y mes <= 12 y anio > 0 Entonces
								validado = Verdadero
							SiNo
								Escribir "Datos err�neos. Intente nuevamente."
								Esperar 1 Segundos
								Limpiar Pantalla
							FinSi
						FinMientras
						
						si tam = 10 Entonces
							totalDia = 0
							
							Para i = 1 Hasta mes - 1 Con Paso 1
								Segun i Hacer
									1, 3, 5, 7, 8, 10, 12:
										totalDia = totalDia + 31
									4, 6, 9, 11:
										totalDia = totalDia + 30
									2:
										si (anio mod 4 = 0 y anio mod 100 <> 0) o (anio mod 400 = 0) Entonces
											totalDia = totalDia + 29
										SiNo
											totalDia = totalDia + 28
										FinSi
								FinSegun
							FinPara
							
							// Se suma el d�a actual
							totalDia = totalDia + dia
							
							Escribir "La fecha con d�a ", dia, ", mes ", mes, ", a�o ", anio, " corresponde al d�a ", totalDia, " del a�o."
							ban = Falso
						SiNo
							Escribir "Dato err�neo. Siga el formato establecido."
						FinSi
					FinMientras

					Esperar 1 Segundos
					Limpiar Pantalla
					
				6:
					Limpiar Pantalla
					Escribir "Bienvenidos al an�lisis num�rico del 1 al 200"
					Escribir "El programa muestra operaciones con n�meros del 1 al 200"
					Repetir
						Escribir "==================== MENU ===================="
						Escribir "1.- Cantidad de n�meros pares"
						Escribir "2.- Suma de n�meros pares"
						Escribir "3.- Cantidad de n�meros impares"
						Escribir "4.- Cantidad de n�meros primos"
						Escribir "5.- Lista de n�meros primos"
						Escribir "6.- Lista de n�meros impares"
						Escribir "7.- Salir"
						Escribir "=============================================="
						Escribir Sin Saltar "Seleccione una opci�n: "
						Leer op
						
						Segun op Hacer
							1:
								cont = 0
								Para i = 1 Hasta 200 Con Paso 1
									Si i mod 2 = 0 Entonces
										cont = cont + 1
									FinSi
								FinPara
								Escribir "Cantidad de n�meros pares: ", cont
								Esperar 1 Segundos
								
							2:
								suma = 0
								Para i = 1 Hasta 200 Con Paso 1
									Si i mod 2 = 0 Entonces
										suma = suma + i
									FinSi
								FinPara
								Escribir "Suma de n�meros pares: ", suma
								Esperar 1 Segundos
								
							3:
								cont = 0
								Para i = 1 Hasta 200 Con Paso 1
									Si i mod 2 <> 0 Entonces
										cont = cont + 1
									FinSi
								FinPara
								Escribir "Cantidad de n�meros impares: ", cont
								Esperar 1 Segundos
								
							4:
								cont = 0
								Para i = 2 Hasta 200 Con Paso 1
									div = 0
									Para j = 1 Hasta i Con Paso 1
										Si i mod j = 0 Entonces
											div = div + 1
										FinSi
									FinPara
									Si div = 2 Entonces
										cont = cont + 1
									FinSi
								FinPara
								Escribir "Cantidad de n�meros primos: ", cont
								Esperar 1 Segundos
								
							5:
								Escribir "Lista de n�meros primos del 1 al 200:"
								Para i = 2 Hasta 200 Con Paso 1
									div = 0
									Para j = 1 Hasta i Con Paso 1
										Si i mod j = 0 Entonces
											div = div + 1
										FinSi
									FinPara
									Si div = 2 Entonces
										Escribir i
									FinSi
								FinPara
								Escribir "Presione una tecla para continuar"
								Esperar Tecla
								
							6:
								Escribir "Lista de n�meros impares del 1 al 200:"
								Para i = 1 Hasta 200 Con Paso 1
									Si i mod 2 <> 0 Entonces
										Escribir i
									FinSi
								FinPara
								Escribir "Presione una tecla para continuar"
								Esperar Tecla
								
							7:
								Escribir "Saliendo del programa..."
								Esperar 1 Segundos
								
							De Otro Modo:
								Escribir "Opci�n inv�lida. Intente de nuevo."
								Esperar 1 Segundos
						FinSegun
						
						Limpiar Pantalla
						
					Hasta Que op = 7

					
					Esperar 1 Segundos
					Limpiar Pantalla
				7:
					Limpiar Pantalla
					Repetir
						Limpiar Pantalla
						Escribir "Tablas de multiplicar"
						Escribir "Recuerde que solo se muestran las tablas del 2 al 10"
						Escribir "Ingrese hasta que tabla desea visualizar"
						Leer num
					Hasta Que (num >= 2) y (num<=10)
					
					Para i <- 2 Hasta num Con Paso 1
						Para j <- 1 Hasta 10 Con Paso 1
							producto <- i * j
							Escribir i, " x ", j, " = ", producto
						FinPara
						Escribir "-------------------------"
					FinPara
					Escribir "Presione una tecla para salir"
					Esperar Tecla
					Limpiar Pantalla
				8:
					Limpiar Pantalla
					Repetir
						Escribir "Ingrese un n�mero entero positivo:"
						Leer num
					Hasta Que num >= 0
					
					factorial <- 1
					i <- 1
					
					Mientras i <= num Hacer
						factorial <- factorial * i
						i <- i + 1
					FinMientras
					
					Escribir "El factorial de ", num, " es: ", factorial
					Esperar 1 Segundos
					Limpiar Pantalla
				9:
					Limpiar Pantalla
					suma=0
					contador=0
					
					Repetir
						Limpiar Pantalla
						Repetir
							Escribir "Bienvenido al sistema de promedio"
							Escribir "El intervalo de calificacion es del 01 al 10"
							Escribir Sin Saltar "Ingrese una nota: "
							Leer nota
						Hasta Que nota >= 0 Y nota <= 10
						
						suma = suma + nota
						contador = contador + 1
						
						Escribir "�Desea ingresar otra nota? (S/N):"
						Leer val
					Hasta Que Mayusculas(val) = "N"
					
					Si contador > 0 Entonces
						Escribir "Promedio de notas: ", suma / contador
					Sino
						Escribir "No se ingresaron notas."
					FinSi
					Esperar 1 Segundos
					Limpiar Pantalla
				10:
					Limpiar Pantalla
					menores15=0
					mayores50=0
					entre25y45=0
					
					Repetir
						Escribir "Ingrese un n�mero natural:"
						Leer num
						
						Si num < 15 Entonces
							menores15=menores15 + 1
						FinSi
						
						Si num > 50 Entonces
							mayores50=mayores50 + 1
						FinSi
						
						Si num >= 25 Y num <= 45 Entonces
							entre25y45=entre25y45 + 1
						FinSi
						
						Escribir "�Desea ingresar otro n�mero? (1=S� / 0=No):"
						Leer continuar
					Hasta Que continuar = 0
					
					Escribir "Cantidad menor a 15: ", menores15
					Escribir "Cantidad mayor a 50: ", mayores50
					Escribir "Cantidad entre 25 y 45: ", entre25y45
					Esperar 1 Segundos
					Limpiar Pantalla
				11:	
					Limpiar Pantalla
					edad = 12
					regalo = 10
					total = 10
					
					Repetir
						regalo = regalo * 2
						total = total + regalo
						edad = edad + 1
					Hasta Que regalo > 1000
					
					Escribir "Edad cuando se le da el �ltimo regalo: ", edad
					Escribir "Cantidad total recibida: ", total
					Escribir "Presione un tecla para continuar"
					Esperar Tecla
					Limpiar Pantalla
				12:
					Limpiar Pantalla
					Escribir "Gracias por usar sistema"
					Esperar 1 Segundos
					Limpiar Pantalla
			Fin Segun
		SiNo
			si op<=0 o op>=13
				Limpiar Pantalla
				Escribir "Opcion incorrecta"
				Escribir "Intente nuevamente"
				Esperar 1 Segundos
				Limpiar Pantalla
			FinSi
		FinSi
	Hasta Que op=12
	
FinAlgoritmo
