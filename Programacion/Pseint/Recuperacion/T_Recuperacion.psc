Proceso TrianguloMitadInferiorIzquierda
	
    Definir A Como Entero
	
    Repetir
        Escribir "Altura del Triángulo (entero positivo mayor a 1): " 
        Leer A
        Si A <= 1 Entonces
            Escribir "La altura debe ser mayor a 1. Intenta de nuevo."
        FinSi
    Hasta Que A > 1
	
    CrearTriangulo(A)
	
FinProceso

// Imprime línea alineada a la derecha
SubProceso ImprimirAsteriscosDerecha(F, Altura)
    Definir i, j Como Entero
	
    Para j <- 1 Hasta (Altura - F) Con Paso 1 Hacer
        Escribir Sin Saltar "  "
    FinPara
	
    Para i <- 1 Hasta (F - 1) Con Paso 1 Hacer
        Escribir Sin Saltar "* "
    FinPara
	
    Escribir ""
FinSubProceso

// Imprime línea alineada a la izquierda
SubProceso ImprimirAsteriscosIzquierda(F)
    Definir i Como Entero
	
    Para i <- 1 Hasta (F - 1) Con Paso 1 Hacer
        Escribir Sin Saltar "* "
    FinPara
	
    Escribir ""
FinSubProceso

// Procedimiento principal
SubProceso CrearTriangulo(A)
    Definir i Como Entero
    Definir AlturaTotal Como Entero
    AlturaTotal <- A + 1
	
    // Parte superior (derecha)
    Para i <- 2 Hasta AlturaTotal Con Paso 1 Hacer
        ImprimirAsteriscosDerecha(i, AlturaTotal)
    FinPara
	
    // Parte inferior (izquierda)
    Para i <- (AlturaTotal - 1) Hasta 2 Con Paso -1 Hacer
        ImprimirAsteriscosIzquierda(i)
    FinPara
FinSubProceso
