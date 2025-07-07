import os

# Rutas a los archivos de texto
txt_admin = "admin.txt"
txt_usuarios = "usuarios.txt"
txt_tareas = "tareas.txt"

import os

# Crear archivos base si no existen
def inicializar_archivos():
    archivos = {
        "admin.txt": ["admin1,adminpass\n"],
        "usuarios.txt": ["sebas,1234\n"],
        "tareas.txt": []  # puede estar vacío
    }

    for nombre, lineas in archivos.items():
        if not os.path.exists(nombre):
            with open(nombre, "w") as f:
                f.writelines(lineas)



def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    limpiar_pantalla()
    print("=== INICIO DE SESIÓN ===")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    with open(txt_admin, 'r') as f:
        for linea in f:
            user, pwd = linea.strip().split(',')
            if user == username and pwd == password:
                return 'admin', username

    with open(txt_usuarios, 'r') as f:
        for linea in f:
            user, pwd = linea.strip().split(',')
            if user == username and pwd == password:
                return 'usuario', username

    print("\nCredenciales incorrectas.")
    input("Presiona Enter para continuar...")
    return None, None

def menu_principal():
    inicializar_archivos()
    while True:
        limpiar_pantalla()
        rol, usuario = login()
        if rol == 'admin':
            menu_admin(usuario)
        elif rol == 'usuario':
            menu_usuario(usuario)


def menu_admin(usuario):
    while True:
        limpiar_pantalla()
        print(f"\n=== MENÚ PRINCIPAL ADMINISTRADOR ({usuario}) ===")
        print("1. Gestión de usuarios")
        print("2. Gestión de tareas")
        print("3. Reportes")
        print("4. Cerrar sesión")
        print("5. Salir")
        op = input("Seleccione una opción: ")

        if op == '1':
            gestion_usuarios()
        elif op == '2':
            gestion_tareas()
        elif op == '3':
            menu_reportes()
        elif op == '4':
            break
        elif op == '5':
            exit()
        else:
            input("Opción no válida. Presiona Enter para continuar...")

def menu_usuario(usuario):
    while True:
        limpiar_pantalla()
        print(f"\n=== MENÚ USUARIO ({usuario}) ===")
        print("1. Ver tareas asignadas")
        print("2. Marcar tarea como completada")
        print("3. Cerrar sesión")
        print("4. Salir")
        op = input("Seleccione una opción: ")

        if op == '1':
            ver_tareas_usuario(usuario)
        elif op == '2':
            completar_tarea(usuario)
        elif op == '3':
            break
        elif op == '4':
            exit()
        else:
            input("Opción no válida. Presiona Enter para continuar...")

# -----------------------------
# GESTIÓN DE USUARIOS (ADMIN)
# -----------------------------
def gestion_usuarios():
    while True:
        limpiar_pantalla()
        print("\n=== GESTIÓN DE USUARIOS ===")
        print("1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("5. Volver")
        op = input("Seleccione una opción: ")

        if op == '1':
            crear_usuario()
        elif op == '2':
            ver_usuarios()
        elif op == '3':
            editar_usuario()
        elif op == '4':
            eliminar_usuario()
        elif op == '5':
            break
        else:
            input("Opción no válida. Presiona Enter para continuar...")

# -----------------------------
# GESTIÓN DE TAREAS (ADMIN)
# -----------------------------
def gestion_tareas():
    while True:
        limpiar_pantalla()
        print("\n=== GESTIÓN DE TAREAS ===")
        print("1. Crear tarea")
        print("2. Ver todas las tareas")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Volver")
        op = input("Seleccione una opción: ")

        if op == '1':
            crear_tarea()
        elif op == '2':
            ver_tareas()
        elif op == '3':
            editar_tarea()
        elif op == '4':
            eliminar_tarea()
        elif op == '5':
            break
        else:
            input("Opción no válida. Presiona Enter para continuar...")

# -----------------------------
# REPORTES (ADMIN)
# -----------------------------
def menu_reportes():
    limpiar_pantalla()
    print("\n=== REPORTES ===")
    input("Funcionalidad en desarrollo. Presiona Enter para volver...")

# -----------------------------
# FUNCIONES USUARIO
# -----------------------------
def crear_usuario():
    limpiar_pantalla()
    print("\n--- CREAR USUARIO ---")
    nombre = input("Nombre de usuario: ")
    clave = input("Contraseña: ")
    with open(txt_usuarios, 'a') as f:
        f.write(f"{nombre},{clave}\n")
    input("Usuario creado. Presiona Enter para continuar...")

def ver_usuarios():
    limpiar_pantalla()
    print("\n--- LISTA DE USUARIOS ---")
    with open(txt_usuarios, 'r') as f:
        for linea in f:
            print("-", linea.strip().split(',')[0])
    input("\nPresiona Enter para continuar...")

def editar_usuario():
    limpiar_pantalla()
    print("\n--- EDITAR USUARIO ---")
    user_edit = input("Nombre del usuario a editar: ")
    nuevas_lineas = []
    encontrado = False
    with open(txt_usuarios, 'r') as f:
        for linea in f:
            user, pwd = linea.strip().split(',')
            if user == user_edit:
                nuevo_pwd = input("Nueva contraseña: ")
                nuevas_lineas.append(f"{user},{nuevo_pwd}\n")
                encontrado = True
            else:
                nuevas_lineas.append(linea)
    if encontrado:
        with open(txt_usuarios, 'w') as f:
            f.writelines(nuevas_lineas)
        input("Usuario actualizado. Presiona Enter...")
    else:
        input("Usuario no encontrado. Presiona Enter...")

def eliminar_usuario():
    limpiar_pantalla()
    print("\n--- ELIMINAR USUARIO ---")
    user_delete = input("Nombre del usuario a eliminar: ")
    nuevas_lineas = []
    eliminado = False
    with open(txt_usuarios, 'r') as f:
        for linea in f:
            user, pwd = linea.strip().split(',')
            if user != user_delete:
                nuevas_lineas.append(linea)
            else:
                eliminado = True
    with open(txt_usuarios, 'w') as f:
        f.writelines(nuevas_lineas)
    if eliminado:
        input("Usuario eliminado. Presiona Enter...")
    else:
        input("Usuario no encontrado. Presiona Enter...")

# -----------------------------
# FUNCIONES TAREAS
# -----------------------------
def crear_tarea():
    limpiar_pantalla()
    print("\n--- CREAR TAREA ---")
    descripcion = input("Descripción: ")
    asignado = input("Asignar a (usuario): ")
    fecha = input("Fecha entrega (YYYY-MM-DD): ")
    estado = "pendiente"
    # Obtener nuevo ID
    try:
        with open(txt_tareas, 'r') as f:
            tareas = f.readlines()
            if tareas:
                ultimo_id = int(tareas[-1].split(';')[0])
            else:
                ultimo_id = 0
    except FileNotFoundError:
        ultimo_id = 0
    nuevo_id = ultimo_id + 1
    with open(txt_tareas, 'a') as f:
        f.write(f"{nuevo_id};{descripcion};{asignado};{estado};{fecha}\n")
    input("Tarea creada. Presiona Enter...")

def ver_tareas():
    limpiar_pantalla()
    print("\n--- TODAS LAS TAREAS ---")
    with open(txt_tareas, 'r') as f:
        for linea in f:
            print(linea.strip())
    input("\nPresiona Enter para continuar...")

def ver_tareas_usuario(usuario):
    limpiar_pantalla()
    print("\n--- TUS TAREAS ---")
    with open(txt_tareas, 'r') as f:
        for linea in f:
            idt, desc, asignado, estado, fecha = linea.strip().split(';')
            if asignado == usuario:
                print(f"{idt}. {desc} - {estado} - Entrega: {fecha}")
    input("\nPresiona Enter para continuar...")

def completar_tarea(usuario):
    limpiar_pantalla()
    print("\n--- COMPLETAR TAREA ---")
    id_buscar = input("ID de la tarea a completar: ")
    nuevas_lineas = []
    completado = False
    with open(txt_tareas, 'r') as f:
        for linea in f:
            idt, desc, asignado, estado, fecha = linea.strip().split(';')
            if idt == id_buscar and asignado == usuario:
                nuevas_lineas.append(f"{idt};{desc};{asignado};completado;{fecha}\n")
                completado = True
            else:
                nuevas_lineas.append(linea)
    with open(txt_tareas, 'w') as f:
        f.writelines(nuevas_lineas)
    if completado:
        input("Tarea marcada como completada. Presiona Enter...")
    else:
        input("Tarea no encontrada o no autorizada. Presiona Enter...")

def editar_tarea():
    limpiar_pantalla()
    input("Funcionalidad en desarrollo. Presiona Enter para continuar...")

def eliminar_tarea():
    limpiar_pantalla()
    input("Funcionalidad en desarrollo. Presiona Enter para continuar...")

# Punto de entrada
if __name__ == '__main__':
    menu_principal()
