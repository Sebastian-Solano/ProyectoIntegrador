Funcion indice <- BuscarProducto(nombre, productos, n)
    Definir i Como Entero
    indice <- -1
    Para i <- 1 Hasta n Hacer
        Si productos[i] = nombre Entonces
            indice <- i
        FinSi
    FinPara
FinFuncion

Algoritmo FacturaConValidacionRobusta
    Definir nombreCliente, cedula, fecha, continuar, entrada Como Cadena
    Definir productoActual, char Como Cadena
    Definir cantidad, precioUnitario, subtotalItem Como Real
    Definir subtotalGeneral, iva, total Como Real
    Definir n, i, j, dia, mes, anio, pos, puntoDecimal Como Entero
    Definir fechaValida, esNumero, esNombreValido Como Logico
    Dimension productos[10], cantidades[10], precios[10], subtotales[10]
	
    Repetir
        // ===== Datos del cliente =====
        Repetir
            Escribir "Ingrese el nombre del cliente (solo letras):"
            Leer nombreCliente
            esNombreValido <- Verdadero
            Si Longitud(nombreCliente) = 0 Entonces
                esNombreValido <- Falso
            Sino
                Para i <- 1 Hasta Longitud(nombreCliente) Hacer
                    char <- Subcadena(nombreCliente, i, i)
                    Si No ((char >= "A" Y char <= "Z") O (char >= "a" Y char <= "z") O char = " ") Entonces
                        esNombreValido <- Falso
                    FinSi
                FinPara
            FinSi
            Si No esNombreValido Entonces
                Escribir "ERROR: Solo se permiten letras y espacios."
                nombreCliente <- ""
            FinSi
        Hasta Que esNombreValido
		
        Repetir
            Escribir "Ingrese la cédula (solo números):"
            Leer cedula
            esNumero <- Verdadero
            Para i <- 1 Hasta Longitud(cedula) Hacer
                Si No (Subcadena(cedula, i, i) >= "0" Y Subcadena(cedula, i, i) <= "9") Entonces
                    esNumero <- Falso
                FinSi
            FinPara
        Hasta Que esNumero Y Longitud(cedula) >= 10
		
        Repetir
            Escribir "Ingrese la fecha (dd/mm/aaaa):"
            Leer fecha
            Si Longitud(fecha) = 10 Y Subcadena(fecha, 3, 3) = "/" Y Subcadena(fecha, 6, 6) = "/" Entonces
                dia <- ConvertirANumero(Subcadena(fecha, 1, 2))
                mes <- ConvertirANumero(Subcadena(fecha, 4, 5))
                anio <- ConvertirANumero(Subcadena(fecha, 7, 10))
                fechaValida <- (dia >= 1 Y dia <= 31) Y (mes >= 1 Y mes <= 12) Y (anio >= 2020 Y anio <= 2100)
            Sino
                fechaValida <- Falso
            FinSi
        Hasta Que fechaValida
		
        Repetir
            Escribir "¿Cuántos productos desea ingresar? (1-10):"
            Leer entrada
            esNumero <- Verdadero
            Para i <- 1 Hasta Longitud(entrada) Hacer
                Si No (Subcadena(entrada, i, i) >= "0" Y Subcadena(entrada, i, i) <= "9") Entonces
                    esNumero <- Falso
                FinSi
            FinPara
            Si esNumero Entonces
                n <- ConvertirANumero(entrada)
            Sino
                n <- 0
            FinSi
        Hasta Que n >= 1 Y n <= 10
		
        subtotalGeneral <- 0
        Escribir "\n========== FACTURA =========="
        Escribir "Cliente: ", nombreCliente
        Escribir "Cédula/RUC: ", cedula
        Escribir "Fecha: ", fecha
        Escribir "----------------------------------------------"
		
        Para i <- 1 Hasta n Con Paso 1 Hacer
            Repetir
                Escribir "Nombre del producto ", i, ":"
                Leer productoActual
                esNombreValido <- Verdadero
                Si Longitud(productoActual) = 0 Entonces
                    esNombreValido <- Falso
                Sino
                    Para j <- 1 Hasta Longitud(productoActual) Hacer
                        char <- Subcadena(productoActual, j, j)
                        Si No ((char >= "A" Y char <= "Z") O (char >= "a" Y char <= "z") O (char >= "0" Y char <= "9") O char = " ") Entonces
                            esNombreValido <- Falso
                        FinSi
                    FinPara
                FinSi
                Si No esNombreValido Entonces
                    Escribir "ERROR: El nombre del producto solo puede contener letras, números y espacios."
                    productoActual <- ""
                FinSi
            Hasta Que esNombreValido
			
            Repetir
                Escribir "Cantidad:" 
                Leer entrada
                esNumero <- Verdadero
                Para j <- 1 Hasta Longitud(entrada) Hacer
                    Si No (Subcadena(entrada, j, j) >= "0" Y Subcadena(entrada, j, j) <= "9") Entonces
                        esNumero <- Falso
                    FinSi
                FinPara
                Si esNumero Entonces
                    cantidad <- ConvertirANumero(entrada)
                Sino
                    cantidad <- 0
                FinSi
            Hasta Que cantidad > 0
			
            Repetir
				Escribir "Precio unitario:" 
				Leer entrada
				esNumero <- Verdadero
				puntoDecimal <- 0
				Para j <- 1 Hasta Longitud(entrada) Hacer
					char <- Subcadena(entrada, j, j)
					Si No ((char >= "0" Y char <= "9") O char = ".") Entonces
						esNumero <- Falso
					Sino
						Si char = "." Entonces
							puntoDecimal <- puntoDecimal + 1
						FinSi
					FinSi
				FinPara
				Si esNumero Y puntoDecimal <= 1 Entonces
					precioUnitario <- ConvertirANumero(entrada)
				Sino
					Escribir "ERROR: Ingrese solo números o un punto decimal válido."
					precioUnitario <- 0
				FinSi
			Hasta Que precioUnitario > 0

			
            // Verificar si el producto ya fue ingresado
			Si i > 1 Entonces
				pos <- BuscarProducto(productoActual, productos, i - 1)
			Sino
				pos <- -1
			FinSi
			
			Si pos <> -1 Entonces
				cantidades[pos] <- cantidades[pos] + cantidad
				subtotales[pos] <- subtotales[pos] + (cantidad * precioUnitario)
			Sino
				productos[i] <- productoActual
				cantidades[i] <- cantidad
				precios[i] <- precioUnitario
				subtotales[i] <- cantidad * precioUnitario
			FinSi
            subtotalGeneral <- subtotalGeneral + (cantidad * precioUnitario)
        FinPara
		
        Escribir "Producto         Cantidad   Precio Unit.  Subtotal"
        Escribir "----------------------------------------------"
        Para i <- 1 Hasta n Hacer
            Si productos[i] <> "" Entonces
                Escribir Sin Saltar productos[i]
                Para j <- 1 Hasta (15 - Longitud(productos[i])) Hacer
                    Escribir Sin Saltar " "
                FinPara
                Escribir Sin Saltar cantidades[i], "         "
                Escribir Sin Saltar precios[i], "       "
                Escribir subtotales[i]
            FinSi
        FinPara
		
        iva <- subtotalGeneral * 0.12
        total <- subtotalGeneral + iva
		
        Escribir "----------------------------------------------"
        Escribir "Subtotal: $", subtotalGeneral
        Escribir "IVA (12%): $", iva
        Escribir "TOTAL A PAGAR: $", total
        Escribir "=============================================="
		
        Repetir
            Escribir "¿Desea generar otra factura? (S/N):"
            Leer continuar
        Hasta Que Mayusculas(continuar) = "S" O Mayusculas(continuar) = "N"
		
    Hasta Que Mayusculas(continuar) = "N"
	
    Escribir "Gracias por usar el sistema de facturación."
FinAlgoritmo
