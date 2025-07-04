#Modulos
import os, time, stdiomask, readchar, sys
from art import text2art
from tqdm import tqdm
from colorama import Fore, init, Style
from datetime import datetime, timedelta

#Funciones
init(autoreset=True)
init()
# Diccionario de usuarios válidos
usuarios = {
    "admin": "1234",
    "sebas": "090600",
    "inv": "test"
}

# Función para limpiar pantalla
def limpiar_pantalla():
    os.system("cls")

# Función para mostrar logo decorativo con 'art'
def mostrar_logo():
    fonts = ["block", "starwars", "stellar", "avatar"]
    colors = [Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.LIGHTRED_EX]
    try:
        for i in range(20):  # 20 ciclos de animación
            os.system('cls' if os.name == 'nt' else 'clear')
            current_font = fonts[i % len(fonts)]
            current_color = colors[i % len(colors)]
            ascii_art = text2art("BIENVENIDOS", font=current_font)
            padding = " " * (i % 15)
            border = "✧" * 50
            print(current_color + border)
            print(current_color + padding + ascii_art)
            print(current_color + border)
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nAnimation stopped")

# Función para simular carga con barra de progreso
def barra_de_carga():
    for _ in tqdm(range(30), desc="Cargando programa", ncols=50, bar_format="{l_bar}{bar}| {percentage:.0f}%"):
        time.sleep(0.05)

# Función principal de inicio de sesión
def iniciar_sesion():
    limpiar_pantalla()
    mostrar_logo()
    intentos_restantes = 3
    while intentos_restantes > 0:
        # Mostrar información de intentos
        print(Fore.MAGENTA + f"\n╔{'═'*25}╗")
        print(f"║ Intentos restantes: {intentos_restantes:<2} ║")
        print(f"╚{'═'*25}╝" + Fore.RESET)

        # Solicitar credenciales
        usuario = input(Fore.CYAN + "┌───────────────────────┐\n│ Usuario: " + Fore.RESET)
        print(Fore.CYAN + "└───────────────────────┘" + Fore.RESET)
        clave = stdiomask.getpass(Fore.CYAN + "┌───────────────────────┐\n│ Contraseña: " + Fore.RESET)
        print(Fore.CYAN + "└───────────────────────┘" + Fore.RESET)

        # Validar credenciales
        if usuario in usuarios and usuarios[usuario] == clave:
            print(Fore.GREEN + "\n╔═══════════════════════╗")
            print( "║   ✔ Acceso concedido   ║")
            print( "╚═══════════════════════╝\n" + Fore.RESET)
            
            barra_de_carga()
            menu(usuario)
            return
        
        # Credenciales incorrectas
        intentos_restantes -= 1
        print(Fore.RED + "\n╔═══════════════════════╗")
        print( "║ ❌ Credenciales inválidas ║")
        print( "╚═══════════════════════╝" + Fore.RESET)
        
        time.sleep(1.5)
        limpiar_pantalla()
        mostrar_logo()

    # Si se agotan los intentos
    print(Fore.RED + "\n╔══════════════════════════════════════╗")
    print( "║                                          ║")
    print( "║   Has agotado tus intentos. Saliendo...  ║")
    print( "║                                          ║")
    print( "╚══════════════════════════════════════╝" + Fore.RESET)

# Funciones prrincipales del programa
def menu(usuario):
    opciones = [
        "Certificado de mayor de edad",
        "Palabra secreta",
        "División",
        "Par o Impar",
        "Estudiantes",
        "Declaración de renta",
        "Números primos",
        "Diferencia de X y Y",
        "Conversión de unidades",
        "Signos del Zodiaco",
        "Ciclista",
        "Capacitación de idiomas",
        "Gráfico",
        "Fábrica de computadoras",
        "Promedios",
        "Gobierno de Bolivia",
        "Salario del obrero",
        "Dirección General de Tráfico",
        "Resultados de laboratorio",
        "Emprendimiento",
        "Salir del sistema"
    ]
    seleccion = 0
    while True:
        limpiar_pantalla()
        print(Fore.CYAN + f"\nBienvenido, {usuario}! Menú principal:\n" + Fore.RESET)
        print(Fore.GREEN + "Use las flechas ↑ ↓ para navegar y ENTER para seleccionar:\n" + Fore.RESET)
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                print(Fore.YELLOW + f"> {i+1}. {opcion} <" + Fore.RESET)
            else:
                print(f"  {i+1}. {opcion}")
        tecla = readchar.readkey()
        if tecla == readchar.key.UP:
            seleccion = (seleccion - 1) % len(opciones)
        elif tecla == readchar.key.DOWN:
            seleccion = (seleccion + 1) % len(opciones)
        elif tecla == readchar.key.ENTER:
            limpiar_pantalla()
            print(Fore.BLUE + f"Ejecutando opción {seleccion + 1}: {opciones[seleccion]}" + Fore.RESET)
            funciones[seleccion]()  # Llama la función correspondiente
            if seleccion == 20:  # Salir
                input("Presione una tecla para salir...")
                break
            else:
                input("Presione una tecla para regresar al menú...")           

def Edad():
    while True:
        try:
            edad=int(input("Ingrese su edad: "))
            if 0<=edad<=100:
                if edad>=18:
                    print(Fore.GREEN+f"Usted es mayor de edad con {edad} años"+Fore.RESET)
                else:
                    print(Fore.RED+f"Usted no es mayor de edad con {edad} años"+Fore.RESET)    
            else:
                print("Edad Fuera de rango. Intentre nuevamente")
            while True:
                sys.stdout.write(f"\n{Fore.YELLOW}» ¿Nuevo cálculo? (s/n): {Style.RESET_ALL}")
                opcion = input().lower()
                if opcion in ('s', 'n'):
                    break
                sys.stdout.write(f"\033[F{Fore.YELLOW}» ¿Nuevo cálculo? (s/n): {Style.RESET_ALL}{opcion}")
                print(f"\n{Fore.RED}Error: Ingrese 's' o 'n'{Style.RESET_ALL}")
            if opcion == 'n':
                print(f"\n{Fore.GREEN}¡Gracias por usar el sistema!{Style.RESET_ALL}")
                break 
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Operación cancelada{Style.RESET_ALL}")
            break    
        except ValueError:
            print("⚠ Entrada inválida. Por favor, ingrese un número entero.")
            
def PalabraSecreta():
    cont = 3
    dato = "dato_oculto"
    
    print(Fore.BLUE + "\n" + "="*50)
    print(Fore.BLUE + "🔐 JUEGO DE ADIVINANZA DE CONTRASEÑA")
    print(Fore.BLUE + "="*50)
    print(Fore.CYAN + "Tienes 3 intentos para adivinar la contraseña secreta")
    
    while cont > 0:
        intento = input(Fore.BLUE + "\nIngrese la contraseña: " + Fore.RESET).strip()
        
        if dato == intento:
            print(Fore.GREEN + f"✅ ¡Correcto! La contraseña es: {dato}")
            break
        else:
            cont -= 1
            if cont > 0:
                print(Fore.RED + f"❌ Contraseña incorrecta. Te quedan {cont} intentos")
            else:
                print(Fore.RED + "❌ ¡Agotaste tus intentos! La contraseña era:", dato)
        
        # Preguntar si desea continuar después de cada intento fallido
        while True:
            try:
                opcion = input(Fore.YELLOW + "\n» ¿Desea seguir intentando? (s/n): ").lower().strip()
                
                if opcion == 'n':
                    print(Fore.GREEN + "\n¡Gracias por jugar!")
                    return
                elif opcion == 's':
                    break
                else:
                    print(Fore.RED + "Error: Ingrese 's' para continuar o 'n' para salir")
                    sys.stdout.write("\033[F\033[K")  # Mover cursor y borrar línea
                    
            except KeyboardInterrupt:
                print(Fore.RED + "\nOperación cancelada")
                return
    
    # Preguntar si desea jugar nuevamente al final
    while True:
        try:
            reiniciar = input(Fore.YELLOW + "\n» ¿Desea jugar nuevamente? (s/n): ").lower().strip()
            
            if reiniciar == 's':
                PalabraSecreta()  # Llamada recursiva para nuevo juego
                return
            elif reiniciar == 'n':
                print(Fore.GREEN + "\n¡Gracias por jugar!")
                return
            else:
                print(Fore.RED + "Error: Ingrese 's' para continuar o 'n' para salir")
                sys.stdout.write("\033[F\033[K")  # Mover cursor y borrar línea
                
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada")
            return
    
def Division():
    print(Fore.BLUE + "El siguiente código realiza la división de dos números")
    
    while True:
        try:
            num1 = int(input(Fore.BLUE + "Ingrese el 'DIVIDENDO' de la operación: "))
            while True:
                try:
                    num2 = int(input(Fore.BLUE + "Ingrese el 'DIVISOR' de la operación: "))
                    if num2 == 0:
                        print(Fore.RED + "Error: El 'DIVISOR' no puede ser cero")
                        time.sleep(1)
                        continue
                    break
                except ValueError:
                    print(Fore.RED + "Error: Ingrese solo números enteros")
                    time.sleep(1)
            total = num1 / num2
            print(Fore.GREEN + f"\nResultado: {num1} ÷ {num2} = {total:.2f}\n")
            while True:
                opcion = input(Fore.YELLOW + "» ¿Nuevo cálculo? (s/n): ").lower()
                if opcion == 's':
                    print("\n" + "="*40 + "\n")
                    break
                elif opcion == 'n':
                    print(Fore.GREEN + "\n¡Gracias por usar el sistema!\n")
                    return
                else:
                    print(Fore.RED + "Error: Ingrese 's' para continuar o 'n' para salir")
                    sys.stdout.write("\033[F") 
                    sys.stdout.write("\033[K") 
        except ValueError:
            print(Fore.RED + "Error: Ingrese solo números enteros")
            time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario\n")
            return
    
def ParImpar():
    print(Fore.BLUE+"El programa le indica si el número digitado es par o impar")
    while True:
        try:
            num1 = int(input("Ingrese su número: "))
            if num1 % 2 == 0:
                print(Fore.GREEN + f"El número {num1} es un número par")
            else:
                print(Fore.CYAN + f"El número {num1} es un número impar")
            while True:
                opcion = input(Fore.YELLOW + "» ¿Nuevo cálculo? (s/n): ").lower()
                if opcion == 's':
                    print("\n" + "="*40 + "\n")
                    break
                elif opcion == 'n':
                    print(Fore.GREEN + "\n¡Gracias por usar el sistema!\n")
                    return
                else:
                    print(Fore.RED + "Error: Ingrese 's' para continuar o 'n' para salir")
                    sys.stdout.write("\033[F") 
                    sys.stdout.write("\033[K") 
        except ValueError:
            print(Fore.RED + "Error: Ingrese solo números enteros")
            time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario\n")
            return
        except ValueError:
            print(Fore.RED + "Error: debe ingresar un número entero válido. Intente nuevamente.")
            
def Estudiantes():
    print(Fore.BLUE + "El código indica a qué grupo pertenece dependiendo del nombre y sexo")
    
    while True:
        try:
            while True:
                nom = input(Fore.BLUE + "Ingrese su nombre: ").strip().lower()
                if nom and nom.isalpha():
                    break
                print(Fore.RED + "Error: Debe ingresar un nombre válido (solo letras)")
            while True:
                sexo = input(Fore.BLUE + "Ingrese su sexo (M/F): ").strip().upper()
                if sexo in ('M', 'F'):
                    break
                print(Fore.RED + "Error: Ingrese solo 'M' o 'F'")
            if (sexo == 'F' and nom[0] < 'm') or (sexo == 'M' and nom[0] > 'n'):
                print(Fore.MAGENTA + "\n» Resultado: Pertenece al Grupo X\n")
            else:
                print(Fore.MAGENTA + "\n» Resultado: Pertenece al Grupo Y\n")
            while True:
                opcion = input(Fore.YELLOW + "» ¿Desea hacer otra consulta? (s/n): ").lower()
                if opcion == 's':
                    print("\n" + "="*40 + "\n")
                    break
                elif opcion == 'n':
                    print(Fore.GREEN + "\n¡Gracias por usar el sistema!\n")
                    return
                else:
                    print(Fore.RED + "Error: Ingrese 's' para continuar o 'n' para salir")
                    sys.stdout.write("\033[F\033[K") 
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario\n")
            return
    
def DeclaracionRenta():
    print(Fore.BLUE + "El programa indica el tipo de impositivos que le corresponde pagar")
    
    while True:
        try:
            while True:
                try:
                    renta = float(input(Fore.BLUE + "Ingrese su renta anual: "))
                    if renta >= 0:
                        break
                    print(Fore.RED + "Error: La renta no puede ser negativa")
                except ValueError:
                    print(Fore.RED + "Error: Ingrese únicamente números válidos")
            if renta < 10000:
                tipo = 5
            elif renta < 20000:
                tipo = 15
            elif renta < 35000:
                tipo = 20
            elif renta < 60000:
                tipo = 30
            else:
                tipo = 45
            print(Fore.MAGENTA + f"\n» Resultado: El tipo de impuesto que le corresponde es del {tipo}%\n")
            while True:
                opcion = input(Fore.YELLOW + "» ¿Desea hacer otra consulta? (s/n): ").lower()
                if opcion == 's':
                    print("\n" + "="*40 + "\n")
                    break
                elif opcion == 'n':
                    print(Fore.GREEN + "\n¡Gracias por usar el sistema!\n")
                    return
                else:
                    print(Fore.RED + "Error: Ingrese 's' para continuar o 'n' para salir")
                    sys.stdout.write("\033[F\033[K")
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario\n")
            return

def NumerosPrimos():
    print(Fore.BLUE + "Verificador de dígitos primos en números de 2 cifras")
    print(Fore.CYAN + "="*50)
    while True:
        while True:
            entrada = input(Fore.BLUE + "\nIngrese un número (10-99) o 'q' para salir: ").strip().lower()
            if entrada == 'q':
                print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
                return
            if not entrada.isdigit():
                print(Fore.RED + "ERROR: Solo números enteros positivos")
                continue 
            num = int(entrada)
            if num < 10 or num > 99:
                print(Fore.RED + "ERROR: Debe ser de 2 cifras (10-99)")
                continue
                
            break
        decena, unidad = num // 10, num % 10
        primos = {2, 3, 5, 7}
        d_primo = decena in primos
        u_primo = unidad in primos
        border = Fore.CYAN + "-"*40
        print(border)
        if d_primo and u_primo:
            print(Fore.GREEN + f" AMBOS dígitos son primos: {decena} y {unidad}")
        elif d_primo:
            print(Fore.MAGENTA + f" Solo la DECENA es prima: {decena}")
        elif u_primo:
            print(Fore.MAGENTA + f" Solo la UNIDAD es prima: {unidad}")
        else:
            print(Fore.YELLOW + f" NINGÚN dígito es primo: {decena} y {unidad}")
        print(border)
        continuar = input(Fore.BLUE + "¿Continuar? (Enter/Sí | 'q'/No): ").strip().lower()
        if continuar == 'q':
            print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
            return

def DiferenciaXY():
    print(Fore.BLUE + "Calculadora de diferencia y rango entre números")
    print(Fore.CYAN + "="*50)
    
    while True:
        try:
            x = int(input(Fore.GREEN + "\nIngrese el número x: "))
            y = int(input(Fore.GREEN + "Ingrese el número y: "))
            diferencia = x - y
            print(Fore.MAGENTA + f"\nDiferencia (x - y): {diferencia}")
            if diferencia <= 10 and diferencia >= 0:
                print(Fore.GREEN + f"Números entre {y} y {x}:")
                print(' '.join(map(str, range(y, x + 1))))
            elif diferencia < 0:
                print(Fore.YELLOW + "Nota: y es mayor que x (diferencia negativa)")
            else:
                print(Fore.CYAN + "Diferencia > 10. No se muestran números intermedios.")
            continuar = input(Fore.BLUE + "\n¿Continuar? (Enter/Sí | 'q'/No): ").strip().lower()
            if continuar == 'q':
                print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
                break
        except ValueError:
            print(Fore.RED + "ERROR: Ingrese solo números enteros válidos")
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario")
            break

def ConversionUnidades():
    while True:
        print(Fore.BLUE + "\n" + "="*50)
        print(Fore.BLUE + "SISTEMA INTEGRADO DE CÁLCULOS")
        print(Fore.BLUE + "="*50)
        print(Fore.CYAN + "Opciones disponibles:")
        print(Fore.CYAN + "1. Convertir centímetros a pulgadas")
        print(Fore.CYAN + "2. Convertir libras a kilogramos")
        print(Fore.CYAN + "3. Salir")
        print(Fore.BLUE + "="*50)
        try:
            opcion = input(Fore.YELLOW + "Seleccione una opción (1-4): ").strip()
            if opcion == "1":
                # Conversión cm a pulgadas
                cm = float(input(Fore.GREEN + "Ingrese centímetros: "))
                pulgadas = cm / 2.54
                print(Fore.MAGENTA + f"\nResultado: {cm} cm = {pulgadas:.2f} pulgadas")
            elif opcion == "2":
                # Conversión lb a kg
                lb = float(input(Fore.GREEN + "Ingrese libras: "))
                kg = lb * 0.453592
                print(Fore.MAGENTA + f"\nResultado: {lb} lb = {kg:.2f} kg")
            elif opcion == "3":
                print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
                break
            else:
                print(Fore.RED + "Opción no válida. Intente nuevamente.")
            input(Fore.BLUE + "\nPresione Enter para continuar...") 
        except ValueError:
            print(Fore.RED + "Error: Ingrese valores numéricos válidos")
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario")
            break

def SignosZodiaco():
    signos = {
        "Capricornio": "(♑)",
        "Acuario":     "(♒)",
        "Piscis":      "(♓)",
        "Aries":       "(♈)",
        "Tauro":       "(♉)",
        "Géminis":     "(♊)",
        "Cáncer":      "(♋)",
        "Leo":         "(♌)",
        "Virgo":       "(♍)",
        "Libra":       "(♎)",
        "Escorpio":    "(♏)",
        "Sagitario":   "(♐)"
    }
    while True:
        print(Fore.BLUE + "\n" + "="*50)
        print(Fore.BLUE + "🔮 CALCULADORA DE SIGNO ZODIACAL Y EDAD")
        print(Fore.BLUE + "="*50)
        valido = False
        while not valido:
            fnac = input(Fore.BLUE + "Ingrese su fecha de nacimiento (dd-mm-aaaa): ").strip()
            if len(fnac) == 10 and fnac[2] == '-' and fnac[5] == '-':
                try:
                    dia = int(fnac[:2])
                    mes = int(fnac[3:5])
                    anio = int(fnac[6:])
                    try:
                        fecha_nac = datetime(anio, mes, dia)
                        hoy = datetime.now()
                        edad = hoy.year - fecha_nac.year
                        if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                            edad -= 1
                        valido = True
                        if mes == 1:
                            signoZ = "Capricornio" if dia <= 20 else "Acuario"
                        elif mes == 2:
                            signoZ = "Acuario" if dia <= 19 else "Piscis"
                        elif mes == 3:
                            signoZ = "Piscis" if dia <= 20 else "Aries"
                        elif mes == 4:
                            signoZ = "Aries" if dia <= 19 else "Tauro"
                        elif mes == 5:
                            signoZ = "Tauro" if dia <= 20 else "Géminis"
                        elif mes == 6:
                            signoZ = "Géminis" if dia <= 21 else "Cáncer"
                        elif mes == 7:
                            signoZ = "Cáncer" if dia <= 21 else "Leo"
                        elif mes == 8:
                            signoZ = "Leo" if dia <= 21 else "Virgo"
                        elif mes == 9:
                            signoZ = "Virgo" if dia <= 22 else "Libra"
                        elif mes == 10:
                            signoZ = "Libra" if dia <= 22 else "Escorpio"
                        elif mes == 11:
                            signoZ = "Escorpio" if dia <= 21 else "Sagitario"
                        elif mes == 12:
                            signoZ = "Sagitario" if dia <= 21 else "Capricornio"
                        else:
                            signoZ = "Desconocido"
                        simbolo = signos.get(signoZ, "")
                        print(Fore.GREEN + f"\n🎉 Edad actual: {edad} años")
                        print(Fore.GREEN + f"🔮 Signo zodiacal: {signoZ} {simbolo}")
                    except ValueError as e:
                        print(Fore.RED + f"❌ Error: Fecha inválida ({str(e)})")
                except ValueError:
                    print(Fore.RED + "❌ Error: Formato numérico incorrecto")
            else:
                print(Fore.RED + "⚠ Formato incorrecto. Use dd-mm-aaaa")
            if not valido:
                time.sleep(1)
                print("\n" * 2)
        continuar = input(Fore.BLUE + "\n¿Desea hacer otra consulta? (s/n): ").strip().lower()
        if continuar != 's':
            print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
            break

def Ciclista():
    print(Fore.BLUE + "\n" + "="*50)
    print(Fore.BLUE + "🚴‍♂️ PROGRAMA DE CÁLCULO DE LLEGADA DE CICLISTA")
    print(Fore.BLUE + "="*50)

    def pedir_hora():
        """Función para solicitar y validar la hora"""
        while True:
            try:
                hh = int(input(Fore.BLUE + "Ingrese la hora de salida (0-23): "))
                if 0 <= hh <= 23:
                    return hh
                print(Fore.RED + "Error: La hora debe estar entre 0 y 23")
            except ValueError:
                print(Fore.RED + "Error: Ingrese un número entero válido")

    def pedir_minuto_segundo(tipo):
        """Función para solicitar minutos o segundos"""
        while True:
            try:
                valor = int(input(Fore.GREEN + f"Ingrese los {tipo} de salida (0-59): "))
                if 0 <= valor <= 59:
                    return valor
                print(Fore.RED + f"Error: Los {tipo} deben estar entre 0 y 59")
            except ValueError:
                print(Fore.RED + "Error: Ingrese un número entero válido")

    def pedir_tiempo_viaje():
        """Función para solicitar el tiempo de viaje"""
        while True:
            try:
                t = int(input(Fore.GREEN + "Ingrese tiempo de viaje en segundos (0-604800): "))
                if 0 <= t <= 604800:
                    return t
                print(Fore.RED + "Error: El tiempo debe estar entre 0 y 604800 segundos (7 días)")
            except ValueError:
                print(Fore.RED + "Error: Ingrese un número entero válido")

    while True:
        try:
            hh = pedir_hora()
            mm = pedir_minuto_segundo("minutos")
            ss = pedir_minuto_segundo("segundos")
            t = pedir_tiempo_viaje()
            print(Fore.CYAN + "\nCalculando llegada...")
            for _ in tqdm(range(100), desc=Fore.GREEN + "Procesando"):
                time.sleep(0.01)
            salida = datetime.now().replace(hour=hh, minute=mm, second=ss, microsecond=0)
            llegada = salida + timedelta(seconds=t)
            hora_12 = llegada.strftime("%I:%M:%S %p")
            dias_viaje = t / 86400  
            dia_semana = llegada.strftime("%A")
            hora = llegada.hour
            if 5 <= hora < 12:
                franja = "en la mañana"
            elif 12 <= hora < 18:
                franja = "en la tarde"
            else:
                franja = "en la noche"
            print(Fore.MAGENTA + "\n" + "="*50)
            print(Fore.MAGENTA + "📅 RESULTADOS DEL CÁLCULO")
            print(Fore.MAGENTA + "="*50)
            print(Fore.MAGENTA + f"🕒 Hora de llegada: {hora_12}")
            print(Fore.MAGENTA + f"📅 Día de llegada: {dia_semana} {franja}")
            print(Fore.MAGENTA + f"⏱️  Duración total: {dias_viaje:.0f} días")
            print(Fore.MAGENTA + "="*50)
            continuar = input(Fore.BLUE + "\n¿Desea hacer otra consulta? (s/n): ").strip().lower()
            if continuar != 's':
                print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
                break
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario")
            break
        except Exception as e:
            print(Fore.RED + f"\nError inesperado: {e}")
            break
    
def CapacitacionIdiomas():
    dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    niveles_validos = ["inicial", "intermedio", "avanzado", "traveler"]
    
    while True:
        print(Fore.BLUE + "\n" + "="*50)
        print(Fore.BLUE + "📅 SISTEMA DE REGISTRO DE CLASES")
        print(Fore.BLUE + "="*50)
        
        # Validación de día de la semana
        while True:
            dia = input(Fore.BLUE + "Ingrese el día de la semana (ej: lunes): ").strip().lower()
            if dia in dias_validos:
                break
            print(Fore.RED + "Error: Día inválido. Opciones válidas: " + ", ".join(dias_validos))
        
        # Validación de día del mes
        while True:
            dd = input(Fore.BLUE + "Ingrese el día del mes (1-31): ").strip()
            if dd.isdigit() and 1 <= int(dd) <= 31:
                dd = int(dd)
                break
            print(Fore.RED + "Error: Debe ser un número entre 1 y 31")
        
        # Validación de mes
        while True:
            mm = input(Fore.BLUE + "Ingrese el número del mes (1-12): ").strip()
            if mm.isdigit() and 1 <= int(mm) <= 12:
                mm = int(mm)
                break
            print(Fore.RED + "Error: Debe ser un número entre 1 y 12")
        
        print(Fore.GREEN + f"\nFecha registrada: {dia.capitalize()}, {dd:02d}/{mm:02d}")
        
        # Validación de nivel
        while True:
            nivel = input(Fore.BLUE + "Ingrese el nivel (inicial/intermedio/avanzado/traveler): ").strip().lower()
            if nivel in niveles_validos:
                break
            print(Fore.RED + "Error: Nivel inválido. Opciones: " + ", ".join(niveles_validos))
        
        # Lógica específica por combinación día/nivel
        try:
            if nivel in ["inicial", "intermedio"] and dia in ["lunes", "martes", "miércoles"]:
                # Cálculo de porcentaje de aprobados
                while True:
                    try:
                        aprobados = int(input(Fore.BLUE + "Ingrese cantidad de alumnos aprobados: "))
                        if aprobados >= 0:
                            break
                        print(Fore.RED + "Error: No puede ser negativo")
                    except ValueError:
                        print(Fore.RED + "Error: Ingrese un número entero")
                
                while True:
                    try:
                        reprobados = int(input(Fore.BLUE + "Ingrese cantidad de alumnos reprobados: "))
                        if reprobados >= 0:
                            break
                        print(Fore.RED + "Error: No puede ser negativo")
                    except ValueError:
                        print(Fore.RED + "Error: Ingrese un número entero")
                
                total = aprobados + reprobados
                if total > 0:
                    porcentaje = (aprobados / total) * 100
                    print(Fore.GREEN + f"Resultados: {porcentaje:.1f}% aprobados")
                    print(Fore.CYAN + f"Reprobados: {reprobados}")
                else:
                    print(Fore.YELLOW + "Advertencia: No hay alumnos registrados")
            
            elif nivel == "avanzado" and dia == "jueves":
                while True:
                    try:
                        asistencia = float(input(Fore.BLUE + "Ingrese porcentaje de asistencia (0-100): "))
                        if 0 <= asistencia <= 100:
                            break
                        print(Fore.RED + "Error: Debe ser entre 0 y 100")
                    except ValueError:
                        print(Fore.RED + "Error: Ingrese un número válido")
                if asistencia > 50:
                    print(Fore.GREEN + "Asistencia: Mayoría presente")
                else:
                    print(Fore.YELLOW + "Asistencia: Menos del 50%")
            elif nivel == "traveler" and dia == "viernes" and dd == 1 and mm in [1, 7]:
                while True:
                    try:
                        alumnos = int(input(Fore.BLUE + "Ingrese cantidad de alumnos: "))
                        if alumnos >= 0:
                            break
                        print(Fore.RED + "Error: No puede ser negativo")
                    except ValueError:
                        print(Fore.RED + "Error: Ingrese un número entero")
                while True:
                    try:
                        arancel = float(input(Fore.BLUE + "Ingrese arancel por alumno ($): "))
                        if arancel >= 0:
                            break
                        print(Fore.RED + "Error: No puede ser negativo")
                    except ValueError:
                        print(Fore.RED + "Error: Ingrese un monto válido")
                ingreso = alumnos * arancel
                print(Fore.GREEN + f"Ingreso total: ${ingreso:,.2f}")
            else:
                print(Fore.CYAN + "No hay acciones específicas para esta combinación")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")
        continuar = input(Fore.BLUE + "\n¿Desea hacer otra consulta? (s/n): ").strip().lower()
        if continuar != 's':
            print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
            break

def Grafico():
    print(Fore.BLUE + "\n" + "="*40)
    print(Fore.BLUE + "🟦 PROGRAMA DE DIBUJO DE RECTÁNGULOS")
    print(Fore.BLUE + "="*40)
    while True:
        try:
            while True:
                tamaño = input(Fore.BLUE + "Ingrese tamaño del rectángulo (4-20): ").strip()
                sys.stdout.write("\033[K")
                if not tamaño.isdigit():
                    print(Fore.RED + "Error: Debe ser un número entero", end="\r")
                    continue
                tamaño = int(tamaño)
                if 4 <= tamaño <= 20:
                    break
                print(Fore.RED + "Error: El tamaño debe estar entre 4 y 20", end="\r")
            borde = "+" + "*" * (tamaño - 2) + "+"
            rectangulo = "\n".join([borde] * tamaño)
            print(Fore.GREEN + "\nRectángulo de tamaño", tamaño, ":\n")
            print(Fore.CYAN + rectangulo)
            continuar = input(Fore.BLUE + "\n¿Desea dibujar otro rectángulo? (s/n): ").strip().lower()
            if continuar != 's':
                print(Fore.GREEN + "\n¡Gracias por usar el sistema!")
                break
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario")
            break

def FabricaComputadoras():
    PRECIO_UNITARIO = 4000
    print(Fore.CYAN + "╔════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.YELLOW + "  SISTEMA DE DESCUENTOS-FÁBRICA DE PCs  " +Fore.CYAN +"║")
    print(Fore.CYAN + "╚════════════════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.GREEN + f"\nPrecio por computadora: ${PRECIO_UNITARIO:,}" + Style.RESET_ALL)
    print(Fore.MAGENTA + "\nEscala de descuentos:")
    print(Fore.WHITE + "- " + Fore.YELLOW + "Menos de 5: " + Fore.GREEN + "10%")
    print(Fore.WHITE + "- " + Fore.YELLOW + "5 a 9: " + Fore.GREEN + "20%")
    print(Fore.WHITE + "- " + Fore.YELLOW + "10 o más: " + Fore.GREEN + "40%\n" + Style.RESET_ALL)
    while True:
        try:
            entrada = input(Fore.BLUE + "\nIngrese cantidad (o 'q' para salir): " + Fore.WHITE).strip()
            if entrada.lower() == 'q':
                print(Fore.YELLOW + "\n¡Gracias por usar nuestro sistema!" + Style.RESET_ALL)
                break
            if not entrada.isdigit():
                print(Fore.RED + "❌ Error: Debe ingresar un número entero" + Style.RESET_ALL)
                continue
            cantidad = int(entrada)
            if cantidad <= 0:
                print(Fore.RED + "❌ Error: La cantidad debe ser mayor a 0" + Style.RESET_ALL)
                continue
            if cantidad < 5:
                descuento = 10
                color_descuento = Fore.YELLOW
            elif cantidad < 10:
                descuento = 20
                color_descuento = Fore.CYAN
            else:
                descuento = 40
                color_descuento = Fore.GREEN     
            subtotal = cantidad * PRECIO_UNITARIO
            monto_descuento = subtotal * descuento / 100
            total = subtotal - monto_descuento
            print(Fore.MAGENTA + "\n═"*40 + Style.RESET_ALL)
            print(Fore.WHITE + f"Cantidad: " + Fore.CYAN + f"{cantidad} computadoras")
            print(Fore.WHITE + f"Subtotal: " + Fore.YELLOW + f"${subtotal:,}")
            print(Fore.WHITE + f"Descuento: " + color_descuento + f"{descuento}% "+Fore.YELLOW + f"(-${monto_descuento:,.2f})")
            print(Fore.WHITE + "Total a pagar: " + Fore.GREEN + f"${total:,.2f}")
            print(Fore.MAGENTA + "═"*40 + Style.RESET_ALL)
            nueva = input(Fore.BLUE + "\n¿Nueva cotización? (s/n): " + Fore.WHITE).strip().lower()
            if nueva != 's':
                print(Fore.YELLOW + "\n¡Gracias por su preferencia!" + Style.RESET_ALL)
                break             
        except KeyboardInterrupt:
            print(Fore.RED + "\nOperación cancelada por el usuario" + Style.RESET_ALL)
            break

def Promedios():
    COLOR_PROMPT = Fore.BLUE
    COLOR_ERROR = Fore.RED
    COLOR_RESULT = Fore.CYAN
    COLOR_SUCCESS = Fore.GREEN
    COLOR_WARNING = Fore.YELLOW
    COLOR_HEADER = Fore.MAGENTA
    RESET = Style.RESET_ALL
    print(f"{COLOR_HEADER}\n╔════════════════════════════════════════╗")
    print(f"║{'  SISTEMA DE PAGO DE COLEGIATURA  '.center(36)}║")
    print(f"╚════════════════════════════════════════╝{RESET}")
    print(f"{COLOR_HEADER}\nPolíticas:{RESET}")
    print(f"- Promedio ≥ 9.0: {COLOR_SUCCESS}30% descuento y sin IVA{RESET}")
    print(f"- Promedio < 9.0: {COLOR_WARNING}Pago completo + 10% IVA{RESET}")
    while True:
        def obtener_dato(mensaje, tipo=float, min_val=None, max_val=None):
            while True:
                try:
                    entrada = input(f"{COLOR_PROMPT}{mensaje}{RESET}").strip()
                    valor = tipo(entrada)
                    if min_val is not None and valor < min_val:
                        print(f"\033[F{COLOR_PROMPT}{mensaje}{RESET}{entrada}")
                        print(f"{COLOR_ERROR}Error: El valor no puede ser menor que {min_val}{RESET}")
                        continue    
                    if max_val is not None and valor > max_val:
                        print(f"\033[F{COLOR_PROMPT}{mensaje}{RESET}{entrada}")
                        print(f"{COLOR_ERROR}Error: El valor no puede ser mayor que {max_val}{RESET}")
                        continue  
                    return valor
                except ValueError:
                    print(f"\033[F{COLOR_PROMPT}{mensaje}{RESET}{entrada}")
                    print(f"{COLOR_ERROR}Error: Ingrese un número válido{RESET}")
        colegiatura = obtener_dato("\nIngrese el monto de la colegiatura: ", float, 0.01)
        promedio = obtener_dato("Ingrese el promedio del alumno (0-10): ", float, 0, 10)
        if promedio >= 9:
            descuento = colegiatura * 0.30
            total = colegiatura - descuento
            iva = 0
            mensaje = f"{COLOR_SUCCESS}✓ Descuento aplicado (30%) y exento de IVA{RESET}"
        else:
            iva = colegiatura * 0.10
            total = colegiatura + iva
            descuento = 0
            mensaje = f"{COLOR_WARNING}Pago normal con 10% de IVA aplicado{RESET}"
        print(f"{COLOR_HEADER}\n{'═'*45}")
        print(f"{'  DETALLE DE PAGO  '.center(45)}")
        print(f"{'═'*45}{RESET}")
        print(f"Colegiatura base:".ljust(25) + f"{COLOR_RESULT}${colegiatura:,.2f}{RESET}")
        if descuento > 0:
            print(f"Descuento (30%):".ljust(25) + f"{COLOR_SUCCESS}-${descuento:,.2f}{RESET}")      
        if iva > 0:
            print(f"IVA (10%):".ljust(25) + f"{COLOR_WARNING}+${iva:,.2f}{RESET}")
        print(f"{'-'*45}")
        print(f"TOTAL A PAGAR:".ljust(25) + f"{COLOR_SUCCESS}${total:,.2f}{RESET}")
        print(f"{COLOR_HEADER}{'═'*45}{RESET}")
        print(f"\n{mensaje}")
        while True:
            continuar = input(f"{COLOR_PROMPT}\n¿Calcular otro pago? (s/n): {RESET}").lower()
            if continuar in ['s', 'n']:
                break
            print(f"\033[F{COLOR_PROMPT}¿Calcular otro pago? (s/n): {RESET}{continuar}")
            print(f"{COLOR_ERROR}Error: Ingrese 's' para sí o 'n' para no{RESET}")
        if continuar == 'n':
            print(f"{COLOR_SUCCESS}\n¡Gracias por usar el sistema!{RESET}")
            break

def GobiernoBolivia():
    HECTAREA_A_M2 = 10000
    LIMITE_SUPERFICIE = 1000000
    DENSIDAD = {
        'Araguaney': {'arboles': 8, 'm2': 10},
        'Samán': {'arboles': 15, 'm2': 15},
        'Ceiba': {'arboles': 10, 'm2': 18}
    }
    ESQUEMAS = {
        'grande': {'Araguaney': 0.70, 'Samán': 0.20, 'Ceiba': 0.10},  # > 1M m²
        'pequeño': {'Araguaney': 0.50, 'Samán': 0.30, 'Ceiba': 0.20}   # ≤ 1M m²
    }
    print(f"\n{Fore.CYAN}=== PROGRAMA DE REFORESTACIÓN ===")
    print(f"{Fore.YELLOW}Gobierno del Estado de Bolívar")
    print(f"{Fore.CYAN}==============================={Style.RESET_ALL}")
    print(f"Cálculo de árboles para reforestación según superficie")
    print(f"{Fore.CYAN}● {Style.RESET_ALL}1 hectárea = {HECTAREA_A_M2:,} m²")
    print(f"{Fore.CYAN}● {Style.RESET_ALL}Límite: {LIMITE_SUPERFICIE:,} m² para cambio de esquema")
    while True:
        try:
            def input_con_color(mensaje, tipo=float, min_val=None):
                while True:
                    sys.stdout.write(f"\r{Fore.YELLOW}{mensaje}{Style.RESET_ALL}")
                    entrada = input().strip()
                    try:
                        valor = tipo(entrada)
                        if min_val is not None and valor < min_val:
                            sys.stdout.write(f"\033[F{Fore.YELLOW}{mensaje}{Style.RESET_ALL}{entrada}")
                            print(f"\n{Fore.RED}Error: El valor debe ser ≥ {min_val}{Style.RESET_ALL}")
                            continue
                        return valor
                    except ValueError:
                        sys.stdout.write(f"\033[F{Fore.YELLOW}{mensaje}{Style.RESET_ALL}{entrada}")
                        print(f"\n{Fore.RED}Error: Ingrese un número válido{Style.RESET_ALL}")
            hectareas = input_con_color("» Ingrese hectáreas del bosque: ", float, 0.01)
            m2 = hectareas * HECTAREA_A_M2
            esquema = 'grande' if m2 > LIMITE_SUPERFICIE else 'pequeño'
            resultados = {}
            for arbol, porcentaje in ESQUEMAS[esquema].items():
                area = m2 * porcentaje
                densidad = DENSIDAD[arbol]['arboles'] / DENSIDAD[arbol]['m2']
                cantidad = int(area * densidad)
                resultados[arbol] = {'area': area, 'cantidad': cantidad}
            print(f"\n{Fore.CYAN}── Resultados ─────────{Style.RESET_ALL}")
            print(f"Superficie: {Fore.GREEN}{m2:,.2f} m² ({hectareas:,.2f} ha){Style.RESET_ALL}")
            print(f"Esquema: {Fore.BLUE}{'Grande' if esquema == 'grande' else 'Pequeño'}{Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}Árboles a sembrar:{Style.RESET_ALL}")
            for arbol, datos in resultados.items():
                print(f"{Fore.YELLOW}● {arbol+':':<10} {Fore.GREEN}{datos['cantidad']:,}{Style.RESET_ALL} árboles")
                print(f"  {Fore.LIGHTBLACK_EX}Área: {datos['area']:,.2f} m² ({datos['area']/m2:.0%}){Style.RESET_ALL}")
            while True:
                sys.stdout.write(f"\n{Fore.YELLOW}» ¿Nuevo cálculo? (s/n): {Style.RESET_ALL}")
                opcion = input().lower()
                if opcion in ('s', 'n'):
                    break
                sys.stdout.write(f"\033[F{Fore.YELLOW}» ¿Nuevo cálculo? (s/n): {Style.RESET_ALL}{opcion}")
                print(f"\n{Fore.RED}Error: Ingrese 's' o 'n'{Style.RESET_ALL}")
            if opcion == 'n':
                print(f"\n{Fore.GREEN}¡Gracias por usar el sistema!{Style.RESET_ALL}")
                break 
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Operación cancelada{Style.RESET_ALL}")
            break

def SalarioObrero():
    TARIFA = {
        'normal': 16,
        'extra': 20,
        'limite_horas': 40,
        'max_horas_semana': 168
    }
    COLOR = {
        'titulo': Fore.CYAN,
        'subtitulo': Fore.LIGHTBLUE_EX,
        'entrada': Fore.YELLOW,
        'error': Fore.RED,
        'advertencia': Fore.MAGENTA,
        'resultado': Fore.GREEN,
        'detalle': Fore.LIGHTWHITE_EX,
        'reset': Style.RESET_ALL
    }
    print(f"\n{COLOR['titulo']}╔══════════════════════════════╗")
    print(f"║{'CALCULADORA DE SALARIO'.center(26)}║")
    print(f"╚══════════════════════════════╝{COLOR['reset']}")
    print(f"{COLOR['subtitulo']}● {COLOR['detalle']}Tarifa normal (≤40 hrs): {COLOR['resultado']}${TARIFA['normal']}/h")
    print(f"{COLOR['subtitulo']}● {COLOR['detalle']}Tarifa extra (>40 hrs): {COLOR['resultado']}${TARIFA['extra']}/h{COLOR['reset']}")
    while True:
        def input_con_correccion(mensaje, tipo=float, min_val=0, max_val=TARIFA['max_horas_semana']):
            while True:
                sys.stdout.write(f"\r{COLOR['entrada']}{mensaje}{COLOR['reset']}")
                entrada = input().strip()
                try:
                    valor = tipo(entrada)
                    if valor < min_val:
                        sys.stdout.write(f"\033[F{COLOR['entrada']}{mensaje}{COLOR['reset']}{entrada}")
                        print(f"\n{COLOR['error']}✖ Error: No puede ser menor que {min_val}{COLOR['reset']}")
                        continue
                    if valor > max_val:
                        sys.stdout.write(f"\033[F{COLOR['entrada']}{mensaje}{COLOR['reset']}{entrada}")
                        print(f"\n{COLOR['advertencia']}⚠ Advertencia: Máximo {max_val} horas por semana{COLOR['reset']}")
                        continue
                    return valor
                except ValueError:
                    sys.stdout.write(f"\033[F{COLOR['entrada']}{mensaje}{COLOR['reset']}{entrada}")
                    print(f"\n{COLOR['error']}✖ Error: Ingrese un número válido{COLOR['reset']}")
        horas = input_con_correccion("» Ingrese horas trabajadas: ")
        if horas <= TARIFA['limite_horas']:
            salario = horas * TARIFA['normal']
            detalle = f"{COLOR['resultado']}{horas} hrs normales{COLOR['reset']}"
        else:
            normales = TARIFA['limite_horas']
            extras = horas - normales
            salario = (normales * TARIFA['normal']) + (extras * TARIFA['extra'])
            detalle = (f"{COLOR['resultado']}{normales} normales{COLOR['reset']} + "f"{COLOR['advertencia']}{extras} extras{COLOR['reset']}")
        print(f"\n{COLOR['titulo']}┌────────────────────────────┐")
        print(f"│{'RESUMEN DE PAGO'.center(26)}│")
        print(f"├────────────────────────────┤{COLOR['reset']}")
        print(f"│ {COLOR['detalle']}Horas trabajadas: {detalle.ljust(15)}│")
        print(f"│ {COLOR['detalle']}Salario total: {COLOR['resultado']}${salario:,.2f}".ljust(26) + f"{COLOR['reset']} │")
        print(f"{COLOR['titulo']}└────────────────────────────┘{COLOR['reset']}")
        while True:
            sys.stdout.write(f"\n{COLOR['entrada']}» ¿Desea otro cálculo? (s/n): {COLOR['reset']}")
            opcion = input().lower()
            if opcion in ('s', 'n'):
                break
            sys.stdout.write(f"\033[F{COLOR['entrada']}» ¿Desea otro cálculo? (s/n): {COLOR['reset']}{opcion}")
            print(f"\n{COLOR['error']}✖ Error: Ingrese 's' o 'n'{COLOR['reset']}")
        
        if opcion == 'n':
            print(f"\n{COLOR['titulo']}¡Gracias por usar el sistema!{COLOR['reset']}")
            break

def DireccionTrafico():
    TASAS = {
        'C': {'nombre': 'Camión', 'tasa': 0.3},
        'A': {'nombre': 'Autobús', 'tasa': 0.3},
        'T': {'nombre': 'Turismo', 'tasa': 0.5},
        'M': {'nombre': 'Motocicleta', 'tasa': 0.3}
    }
    
    COLOR = {
        'titulo': Fore.CYAN,
        'entrada': Fore.YELLOW,
        'error': Fore.RED,
        'positivo': Fore.RED + Style.BRIGHT,
        'negativo': Fore.GREEN + Style.BRIGHT,
        'reset': Style.RESET_ALL
    }
    print(f"\n{COLOR['titulo']}=== CONTROL DE ALCOHOLEMIA - DGT ===")
    print("==================================")
    print(f"{COLOR['reset']}Sistema de verificación de tasas de alcohol")
    print(f"\n{COLOR['titulo']}Tasas máximas permitidas:{COLOR['reset']}")
    for cod, datos in TASAS.items():
        print(f"- {datos['nombre']} ({cod}): {datos['tasa']} g/L")
    while True:
        def input_con_correccion(prompt, validacion, mensaje_error):
            while True:
                sys.stdout.write(f"\r{COLOR['entrada']}{prompt}{COLOR['reset']}")
                entrada = input().strip()
                if validacion(entrada):
                    return entrada
                sys.stdout.write(f"\033[F{COLOR['entrada']}{prompt}{COLOR['reset']}{entrada}")
                print(f"\n{COLOR['error']}{mensaje_error}{COLOR['reset']}")
        tipo = input_con_correccion("» Tipo de vehículo (C/A/T/M): ",lambda x: x.upper() in TASAS,"Error: Ingrese C (Camión), A (Autobús), T (Turismo) o M (Motocicleta)").upper()
        tasa = float(input_con_correccion("» Tasa de alcohol (g/L): ",lambda x: x.replace('.', '', 1).isdigit() and float(x) >= 0,"Error: Ingrese un número positivo (ej: 0.4)"))
        vehiculo = TASAS[tipo]
        if tasa > vehiculo['tasa']:
            resultado = f"{COLOR['positivo']}⛔ POSITIVO (Supera {vehiculo['tasa']} g/L){COLOR['reset']}"
        else:
            resultado = f"{COLOR['negativo']}✅ NEGATIVO (Dentro del límite){COLOR['reset']}"
        print(f"\n{COLOR['titulo']}════════ RESULTADO ════════{COLOR['reset']}")
        print(f"Vehículo: {vehiculo['nombre']}")
        print(f"Tasa máxima permitida: {vehiculo['tasa']} g/L")
        print(f"Tasa medida: {tasa} g/L")
        print(f"Resultado: {resultado}")
        print(f"{COLOR['titulo']}══════════════════════════{COLOR['reset']}")
        continuar = input_con_correccion("\n» ¿Nuevo control? (s/n): ",lambda x: x.lower() in ('s', 'n'),"Error: Ingrese 's' para sí o 'n' para no").lower()
        if continuar == 'n':
            print(f"\n{COLOR['titulo']}¡Gracias por usar el sistema de la DGT!{COLOR['reset']}")
            break

def ResultadosLaboratorio():
    RANGOS = {
        1: {'desc': f"{Fore.LIGHTBLUE_EX}0-1 mes{Fore.RESET}", 'min': 13, 'max': 26},
        2: {'desc': f"{Fore.LIGHTBLUE_EX}1-6 meses{Fore.RESET}", 'min': 10, 'max': 18},
        3: {'desc': f"{Fore.LIGHTBLUE_EX}6-12 meses{Fore.RESET}", 'min': 11, 'max': 15},
        4: {'desc': f"{Fore.LIGHTBLUE_EX}1-5 años{Fore.RESET}", 'min': 11.5, 'max': 15},
        5: {'desc': f"{Fore.LIGHTBLUE_EX}5-10 años{Fore.RESET}", 'min': 12.6, 'max': 15.5},
        6: {'desc': f"{Fore.LIGHTBLUE_EX}10-15 años{Fore.RESET}", 'min': 13, 'max': 15.5},
        7: {'desc': f"{Fore.LIGHTMAGENTA_EX}Mujeres >15 años{Fore.RESET}", 'min': 12, 'max': 16},
        8: {'desc': f"{Fore.LIGHTCYAN_EX}Hombres >15 años{Fore.RESET}", 'min': 14, 'max': 15}
    }
    COLOR = {
        'titulo': Fore.CYAN + Style.BRIGHT,
        'borde': Fore.LIGHTWHITE_EX,
        'menu': Fore.LIGHTBLUE_EX,
        'entrada': Fore.YELLOW + Style.BRIGHT,
        'error': Fore.RED + Style.BRIGHT,
        'positivo': Fore.RED + Style.BRIGHT,
        'negativo': Fore.GREEN + Style.BRIGHT,
        'alto': Fore.MAGENTA + Style.BRIGHT,
        'valor': Fore.LIGHTYELLOW_EX,
        'reset': Style.RESET_ALL
    }
    print(f"\n{COLOR['borde']}╔{'═'*30}╗")
    print(f"║{COLOR['titulo']}  DIAGNÓSTICO DE ANEMIA  {COLOR['borde']}║")
    print(f"╚{'═'*30}╗{COLOR['reset']}")
    print(f"{COLOR['titulo']}Sistema clínico con corrección selectiva{COLOR['reset']}")
    print(f"{COLOR['borde']}╔{'═'*30}╝{COLOR['reset']}")
    while True:
        def input_color(prompt, tipo, validacion, mensaje_error):
            while True:
                sys.stdout.write(f"\r{COLOR['entrada']}{prompt}{COLOR['reset']}")
                entrada = input().strip()
                try:
                    valor = tipo(entrada)
                    if not validacion(valor):
                        raise ValueError
                    return valor
                except ValueError:
                    sys.stdout.write(f"\033[F{COLOR['entrada']}{prompt}{COLOR['reset']}{entrada}")
                    print(f"\n{COLOR['error']}✖ {mensaje_error}{COLOR['reset']}")
        print(f"\n{COLOR['menu']}┌{'─'*28}┐")
        print(f"│{'GRUPOS ETARIOS DISPONIBLES'.center(28)}│")
        print(f"├{'─'*28}┤{COLOR['reset']}")
        for opcion, datos in RANGOS.items():
            print(f"{COLOR['menu']}│{COLOR['reset']} {opcion}. {datos['desc']} {COLOR['valor']}({datos['min']}-{datos['max']} g%){COLOR['reset']} {COLOR['menu']}│{COLOR['reset']}")
        print(f"{COLOR['menu']}└{'─'*28}┘{COLOR['reset']}")
        grupo_opcion = input_color(f"{COLOR['entrada']}» Seleccione grupo (1-8): {COLOR['reset']}",int,lambda x: x in RANGOS,"Ingrese un número entre 1 y 8")
        grupo = RANGOS[grupo_opcion]
        hemoglobina = input_color(f"{COLOR['entrada']}» Ingrese hemoglobina (g%): {COLOR['reset']}",float,lambda x: x > 0,"Ingrese un valor numérico positivo")
        if hemoglobina < grupo['min']:
            diagnostico = f"{COLOR['positivo']}⚠️ POSITIVO PARA ANEMIA (Por debajo del rango)"
        elif hemoglobina > grupo['max']:
            diagnostico = f"{COLOR['alto']}⬆️ NIVEL ELEVADO DE HEMOGLOBINA"
        else:
            diagnostico = f"{COLOR['negativo']}✅ DENTRO DEL RANGO NORMAL"
        print(f"\n{COLOR['borde']}╔{'═'*30}╗")
        print(f"║{COLOR['titulo']}     RESULTADOS      {COLOR['borde']}║")
        print(f"╠{'═'*30}╣{COLOR['reset']}")
        print(f"{COLOR['menu']}│{COLOR['reset']} {'Grupo:'.ljust(15)} {grupo['desc']} {COLOR['menu']}│{COLOR['reset']}")
        print(f"{COLOR['menu']}│{COLOR['reset']} {'Rango normal:'.ljust(15)} {COLOR['valor']}{grupo['min']}-{grupo['max']} g%{COLOR['reset']} {COLOR['menu']}│{COLOR['reset']}")
        print(f"{COLOR['menu']}│{COLOR['reset']} {'Valor medido:'.ljust(15)} {COLOR['valor']}{hemoglobina} g%{COLOR['reset']} {COLOR['menu']}│{COLOR['reset']}")
        print(f"{COLOR['menu']}│{COLOR['reset']} {'Diagnóstico:'.ljust(15)} {diagnostico}{COLOR['reset']} {COLOR['menu']}│{COLOR['reset']}")
        print(f"{COLOR['borde']}╚{'═'*30}╝{COLOR['reset']}")
        continuar = input_color(f"\n{COLOR['entrada']}» ¿Desea otro diagnóstico? (s/n): {COLOR['reset']}",str,lambda x: x.lower() in ('s', 'n'),"Ingrese 's' para sí o 'n' para no").lower()
        if continuar == 'n':
            print(f"\n{COLOR['titulo']}¡Gracias por usar el sistema de diagnóstico!{COLOR['reset']}")
            print(f"{COLOR['borde']}╔{'═'*30}╗")
            print(f"║{Fore.LIGHTGREEN_EX}  Programa finalizado  {COLOR['borde']}║")
            print(f"╚{'═'*30}╝{COLOR['reset']}")
            break

def Emprendimiento():
    COLOR = {
        'titulo': Fore.CYAN + Style.BRIGHT,
        'borde': Fore.LIGHTWHITE_EX,
        'entrada': Fore.YELLOW + Style.BRIGHT,
        'error': Fore.RED + Style.BRIGHT,
        'positivo': Fore.GREEN + Style.BRIGHT,
        'advertencia': Fore.MAGENTA + Style.BRIGHT,
        'valor': Fore.LIGHTYELLOW_EX,
        'reset': Style.RESET_ALL
    }
    print(f"\n{COLOR['borde']}╔{'═'*40}╗")
    print(f"║{COLOR['titulo']}   PLANIFICADOR DE INVERSIÓN   {COLOR['borde']}║")
    print(f"╚{'═'*40}╗{COLOR['reset']}")
    print(f"{COLOR['titulo']}Sistema para distribución de capital inicial{COLOR['reset']}")
    print(f"{COLOR['borde']}╔{'═'*40}╝{COLOR['reset']}")
    print(f"{COLOR['titulo']}●{COLOR['reset']} Si hipoteca < $1M: {COLOR['positivo']}50% usted - 50% socio{COLOR['reset']}")
    print(f"{COLOR['titulo']}●{COLOR['reset']} Si hipoteca ≥ $1M: {COLOR['positivo']}Hipoteca completa + resto 50/50{COLOR['reset']}")

    while True:
        def input_con_correccion(prompt, validacion, mensaje_error, tipo=float):
            while True:
                sys.stdout.write(f"\r{COLOR['entrada']}{prompt}{COLOR['reset']}")
                entrada = input().strip()
                try:
                    valor = tipo(entrada)
                    if not validacion(valor):
                        raise ValueError
                    return valor
                except ValueError:
                    sys.stdout.write(f"\033[F{COLOR['entrada']}{prompt}{COLOR['reset']}{entrada}")
                    print(f"\n{COLOR['error']}✖ {mensaje_error}{COLOR['reset']}")
        hipoteca = input_con_correccion("» Monto de la hipoteca ($): ",lambda x: x >= 0,"Ingrese un valor numérico positivo")
        inversion_total = input_con_correccion("» Inversión total requerida ($): ",lambda x: x >= 0,"Ingrese un valor numérico positivo")
        if inversion_total < hipoteca:
            print(f"\n{COLOR['advertencia']}⚠ Atención: La hipoteca cubre toda la inversión{COLOR['reset']}")
        if hipoteca < 1000000:
            su_aporte = inversion_total * 0.5
            socio_aporte = inversion_total * 0.5
            estrategia = f"{COLOR['positivo']}Distribución equitativa 50/50{COLOR['reset']}"
        else:
            su_aporte = min(hipoteca, inversion_total)
            resto = max(0, inversion_total - hipoteca)
            su_aporte += resto * 0.5
            socio_aporte = resto * 0.5
            estrategia = f"{COLOR['positivo']}Hipoteca completa + división del resto{COLOR['reset']}"
        print(f"\n{COLOR['borde']}╔{'═'*40}╗")
        print(f"║{COLOR['titulo']}      RESUMEN DE INVERSIÓN      {COLOR['borde']}║")
        print(f"╠{'═'*40}╣{COLOR['reset']}")
        print(f"║ {COLOR['titulo']}Estrategia:{COLOR['reset']} {estrategia.ljust(36)} ║")
        print(f"║ {COLOR['titulo']}Su aporte:{COLOR['reset']} {COLOR['valor']}${su_aporte:,.2f}".ljust(39) + f"{COLOR['borde']} ║{COLOR['reset']}")
        print(f"║ {COLOR['titulo']}Aporte socio:{COLOR['reset']} {COLOR['valor']}${socio_aporte:,.2f}".ljust(39) + f"{COLOR['borde']} ║{COLOR['reset']}")
        print(f"║ {COLOR['titulo']}Total inversión:{COLOR['reset']} {COLOR['valor']}${inversion_total:,.2f}".ljust(39) + f"{COLOR['borde']} ║{COLOR['reset']}")
        print(f"{COLOR['borde']}╚{'═'*40}╝{COLOR['reset']}")
        continuar = input_con_correccion(f"\n{COLOR['entrada']}» ¿Nuevo cálculo? (s/n): {COLOR['reset']}",lambda x: x.lower() in ('s', 'n'),"Ingrese 's' para sí o 'n' para no",str).lower()
        if continuar == 'n':
            print(f"\n{COLOR['titulo']}¡Éxito en su emprendimiento!{COLOR['reset']}")
            print(f"{COLOR['borde']}╔{'═'*40}╗")
            print(f"║ {Fore.LIGHTGREEN_EX} Programa finalizado ".center(38) + f"{COLOR['borde']} ║")
            print(f"╚{'═'*40}╝{COLOR['reset']}")
            break

def Salir():
    print(Fore.GREEN + text2art("CERRANDO SISTEMA") + Fore.RESET)
    for _ in tqdm(range(30), desc="Log out", ncols=50, bar_format="{l_bar}{bar}| {percentage:.0f}%"):
        time.sleep(0.05)

# Diccionario para llamar funciones por índice
funciones = {
    0: Edad,
    1: PalabraSecreta,
    2: Division,
    3: ParImpar,
    4: Estudiantes,
    5: DeclaracionRenta,
    6: NumerosPrimos,
    7: DiferenciaXY,
    8: ConversionUnidades,
    9: SignosZodiaco,
    10: Ciclista,
    11: CapacitacionIdiomas,
    12: Grafico,
    13: FabricaComputadoras,
    14: Promedios,
    15: GobiernoBolivia,
    16: SalarioObrero,
    17: DireccionTrafico,
    18: ResultadosLaboratorio,
    19: Emprendimiento,
    20: Salir
}

#Proceso
iniciar_sesion()
