Algoritmo EsctructurasDeControl
	Definir op, tam,dia,mes,anio,conf Como Entero
	Definir Pcoste,pvp,nun1,nun2,diferencia,i como real
	Definir Fnac,signoZ como cadena
	Definir ban,bisiesto Como Logico
	
	Repetir
		Escribir "|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|"
		Escribir "|       Bienvenido al sistema       |"
		Escribir "|-----------------------------------|"
		Escribir "|       Seleccione una opcione      |"
		Escribir "|-----------------------------------|"
		Escribir "|1.-    Papeleria                   |"
		Escribir "|2.-    Comprobar fecha             |"
		Escribir "|3.-    Signo zodiacal              |"
		Escribir "|4.-    Diferencia de numeros       |"
		Escribir "|5.-    Dia del año                 |"
		Escribir "|6.-    Multiplos de tres           |"
		Escribir "|7.-    Tablas de multiplicar       |"
		Escribir "|8.-    Factorial(while)            |"
		Escribir "|9.-    Promedio(while)             |"
		Escribir "|10.-   Numeros naturales           |"
		Escribir "|11.-   Regalo de cumpleaños        |"
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
						
						Escribir "Comprobacion de la fecha"
						Escribir Sin Saltar"Ingrese la fecha de su cumpleaños (dd-mm-aaaa)"
						Leer Fnac
						tam=Longitud(Fnac)
						
						si tam=10 Entonces
							
							dia=ConvertirANumero(SubCadena(Fnac,1,2))
							mes=ConvertirANumero(SubCadena(Fnac,4,5))
							anio=ConvertirANumero(SubCadena(Fnac,7,10))
							
							si anio>0 Entonces
								Escribir "El año esta dentro del rango"
								Escribir "Presione una tecla para continuar"
								Esperar Tecla
								Limpiar Pantalla
								bisiesto=Falso
							FinSi
							si mes>=1 y mes<=12 Entonces
								Escribir "El mes esta dentro del rango"
								Escribir "Presione una tecla para continuar"
								Esperar Tecla
								Limpiar Pantalla
							FinSi
							si (anio mod 4 = 0) o ((anio mod 100 = 0) y (anio mod 400 = 0)) Entonces
								Escribir "El año es bisiesto"
								Escribir "Presione una tecla para continuar"
								Esperar Tecla
								Limpiar Pantalla
								bisiesto=Verdadero
							FinSi
							
							Segun mes Hacer
								1,3,5,7,8,10,12:
									Escribir "El mes tiene 31 dias"
									si dia>=1 y dia<=31 Entonces
										Escribir "El dia esta dentro del rango"
										Escribir "Presione una tecla para continuar"
										Esperar Tecla
										Limpiar Pantalla
									FinSi
								4,6,9,11:
									Escribir "El mes tiene 30 dias"
									si dia>=1 y dia<=30 Entonces
										Escribir "El dia esta dentro del rango"
										Escribir "Presione una tecla para continuar"
										Esperar Tecla
										Limpiar Pantalla
								FinSi
								2:
									si bisiesto= Verdadero Entonces
										Escribir "El mes tiene 29 dias"
										Escribir "Su año es bisiesto"
										si dia>=1 y dia<=29 Entonces
											Escribir "El dia esta dentro del rango"
											Escribir "Presione una tecla para continuar"
											Esperar Tecla
											Limpiar Pantalla
										FinSi
									SiNo
										si dia>=1 y dia<=28 Entonces
											Escribir "El mes tiene 28 dias"
											Escribir "El dia esta dentro del rango"
											Escribir "Presione una tecla para continuar"
											Esperar Tecla
											Limpiar Pantalla
										FinSi
									FinSi
							Fin Segun
							
							
							Escribir "La fecha con dia ",dia," mes ",mes," año ",anio," es correcto"
							Escribir "Presione una tecla para continuar"
							Esperar Tecla
							Limpiar Pantalla
							ban=Falso
						SiNo
							si tam <>10 Entonces
								Escribir "Dato erroneo"
								Escribir "Por favor siga el formato"
								Esperar 1 Segundos
								Limpiar Pantalla
							FinSi
						FinSi
					Fin Mientras
					Esperar 1 Segundos
					Limpiar Pantalla
				3:
					Limpiar Pantalla
					ban = Verdadero
					Mientras ban Hacer
						
						Escribir "Signo zodiacal"
						Escribir Sin Saltar"Ingrese la fecha de su cumpleaños (dd-mm-aaaa)"
						Leer Fnac
						tam=Longitud(Fnac)
						
						si tam=10 Entonces
							
							dia=ConvertirANumero(SubCadena(Fnac,1,2))
							mes=ConvertirANumero(SubCadena(Fnac,4,5))
							anio=ConvertirANumero(SubCadena(Fnac,7,10))
							
							Segun mes Hacer
								1://enero
									si dia>=1 y dia<=20 Entonces
										signoZ="Capricornio"
									SiNo
										si dia>=21 y dia<=31 Entonces
											signoZ="Acuario"
										FinSi
									FinSi
								2://febrero
									si dia>=1 y dia<=19 Entonces
										signoZ="Acuario"
									SiNo
										si dia>=20 y dia<=29 Entonces
											signoZ="Piscis"
										FinSi
									FinSi
								3://marzo
									si dia>=1 y dia<=20 Entonces
										signoZ="Piscis"
									SiNo
										si dia>=21 y dia<=31 Entonces
											signoZ="Aries"
										FinSi
									FinSi
								4://abril
									si dia>=1 y dia<=19 Entonces
										signoZ="Aries"
									SiNo
										si dia>=20 y dia<=30 Entonces
											signoZ="Tauro"
										FinSi
									FinSi
								5://mayo
									si dia>=1 y dia<=20 Entonces
										signoZ="Tauro"
									SiNo
										si dia>=21 y dia<=31 Entonces
											signoZ="Geminis"
										FinSi
									FinSi
								6://junio
									si dia>=1 y dia<=21 Entonces
										signoZ="Geminis"
									SiNo
										si dia>=22 y dia<=30 Entonces
											signoZ="Cancer"
										FinSi
									FinSi
								7://julio
									si dia>=1 y dia<=21 Entonces
										signoZ="Cancer"
									SiNo
										si dia>=22 y dia<=31 Entonces
											signoZ="Leo"
										FinSi
									FinSi
								8://agosto
									si dia>=1 y dia<=21 Entonces
										signoZ="Leo"
									SiNo
										si dia>=22 y dia<=31 Entonces
											signoZ="Virgo"
										FinSi
									FinSi
								9://septiembre
									si dia>=1 y dia<=22 Entonces
										signoZ="Virgo"
									SiNo
										si dia>=23 y dia<=30 Entonces
											signoZ="Libra"
										FinSi
									FinSi
								10://octubre
									si dia>=1 y dia<=22 Entonces
										signoZ="Libra"
									SiNo
										si dia>=23 y dia<=31 Entonces
											signoZ="Escorpio"
										FinSi
									FinSi
								11://noviembre
									si dia>=1 y dia<=21 Entonces
										signoZ="Escorpio"
									SiNo
										si dia>=22 y dia<=30 Entonces
											signoZ="Sagitario"
										FinSi
									FinSi
								12:	//diciembre
									si dia>=1 y dia<=21 Entonces
										signoZ="Sagitario"
									SiNo
										si dia>=22 y dia<=31 Entonces
											signoZ="Capricornio"
										FinSi
									FinSi
							Fin Segun
							
							Escribir "La fecha con dia ",dia," mes ",mes," año ",anio," es de signo ", signoZ
							
							si signoZ="Aries" Entonces
								Escribir "      \\    /"
								Escribir "       )  (  "
								Escribir "      /    \\"
								Escribir "     /      \\"
							FinSi
							si signoZ="Tauro" Entonces
								Escribir "      (__)   (__)"
								Escribir "      (oo)   (oo)"
								Escribir "  /----\\/     \\/----\\"
								Escribir " / |  ||       ||  | \\"
								Escribir "*  ||--||-----||--||  *"
								Escribir "   ^^  ^^     ^^  ^^"
							FinSi
							si signoZ="Geminis" Entonces
								Escribir "     ________"
								Escribir "    |   ||   |"
								Escribir "    |   ||   |"
								Escribir "    |   ||   |"
								Escribir "    |   ||   |"
								Escribir "    |___||___|"
							FinSi
							si signoZ="Cancer" Entonces
								Escribir "     _     _"
								Escribir "  __(.)< __(.)<"
								Escribir "  \\___)  \\___)"
							FinSi
							si signoZ="Leo" Entonces
								Escribir "      /^--^\\"
								Escribir "     ( o  o )"
								Escribir "     (  =^=  )"
								Escribir "     (        )"
								Escribir "     (         )"
								Escribir "     (          ))))))"
							FinSi
							si signoZ="Virgo" Entonces
								Escribir "     /|\\"
								Escribir "    /_|_\\"
								Escribir "     ||"
								Escribir "     ||"
								Escribir "    /__\\"
							FinSi
							si signoZ="Libra" Entonces
								Escribir "     _______"
								Escribir "    |       |"
								Escribir " ___|_______|___"
								Escribir " \\           /"
								Escribir "  \\_________/"
							FinSi
							si signoZ="Escorpio" Entonces
								Escribir "     /\\_/\\"
								Escribir "    ( o.o )"
								Escribir "     > ^ <==<"
							FinSi
							si signoZ="Sagitario" Entonces
								Escribir "        \\ | /"
								Escribir "         \\|/"
								Escribir "       --(*)-->"
								Escribir "         /|\\"
								Escribir "        / | \\"
							FinSi
							si signoZ="Capricornio" Entonces
								Escribir "      (__) "
								Escribir "      (oo) "
								Escribir " /------\\/ "
								Escribir "/ |    ||  "
								Escribir "*  /\\---/\\"
							FinSi
							si signoZ="Acuario" Entonces
								Escribir "     ~~~~~    ~~~~~"
								Escribir "   ~~~~~~    ~~~~~~"
								Escribir "     ~~~~    ~~~~"
							FinSi
							si signoZ="Piscis" Entonces
								Escribir "     ><(((º>   <º)))><"
							FinSi
							Escribir "Presione una tecla para continuar"
							Esperar Tecla
							Limpiar Pantalla
							ban=Falso
						SiNo
							si tam <>10 Entonces
								Escribir "Dato erroneo"
								Escribir "Por favor siga el formato"
								Esperar 1 Segundos
								Limpiar Pantalla
							FinSi
						FinSi
					Fin Mientras
					Esperar 1 Segundos
					Limpiar Pantalla
					
				4:
					Limpiar Pantalla
					ban=Verdadero
					Mientras ban Hacer
						Escribir "Diferencia entre dos numeros"
						Escribir Sin Saltar "Ingrese el primer numero"
						Leer nun1
						Escribir Sin Saltar"Ingrese el segundo numero"
						leer nun2
						
						diferencia=nun1-nun2
						
						si diferencia<0 Entonces
							diferencia=diferencia*(-1)
						FinSi
						si diferencia<=10 Entonces
							Escribir "La diferencia entre los dos numeros es menor o igual a 10"
							si nun1>=num2 Entonces
								para i=nun2 Hasta nun1 Con Paso 1
									Escribir i
								FinPara	
							SiNo
								si nun1<nun2 Entonces
									para i=nun1 Hasta nun2 Con Paso 1
										Escribir i
									FinPara
								FinSi
							FinSi
						SiNo
							si diferencia >10 Entonces
								Escribir "La diferencia entre los dos numeros es supeior a 10: ",diferencia
							FinSi
						FinSi
						Escribir "Desea salir si=1; no=0"
						leer conf
						si conf=1 Entonces
							ban=Falso
						FinSi
						Limpiar Pantalla
					Fin Mientras
					
				5:
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
					
				6:
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
				7:
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
				8:
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
				9:
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
				10:
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
				11:	
					Escribir "salio"
					Esperar 1 Segundos
					Limpiar Pantalla
				12:
					Escribir "salio"
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
