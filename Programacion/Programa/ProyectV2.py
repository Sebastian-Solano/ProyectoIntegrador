import hashlib
import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Configuración inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Archivos de datos
USERS_FILE = "users.txt"
TASKS_FILE = "tasks.txt"

class DatabaseManager:
    @staticmethod
    def initialize_files():
        try:
            if not os.path.exists(USERS_FILE):
                with open(USERS_FILE, 'w') as f:
                    f.write("1|admin|8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92|admin\n")
                    f.write("2|sebas|70bd8714a2d856538c68cb92919d6573f4c690959e148dc133f6f043c0e41199|student\n")
            
            if not os.path.exists(TASKS_FILE):
                with open(TASKS_FILE, 'w') as f:
                    f.write("1|Inventario|Comprar materiales|Compras|pending|1|2023-01-01 00:00:00|2\n")
        
        except Exception as e:
            print(f"Error inicializando archivos: {e}")

    @staticmethod
    def get_next_id(filename):
        max_id = 0
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if '|' in line:
                        entity_id = int(line.split('|')[0])
                        max_id = max(max_id, entity_id)
        except FileNotFoundError:
            pass
        return max_id + 1

    @staticmethod
    def get_users():
        users = []
        try:
            with open(USERS_FILE, 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        users.append({
                            'id': int(parts[0]),
                            'username': parts[1],
                            'password': parts[2],
                            'role': parts[3]
                        })
        except FileNotFoundError:
            DatabaseManager.initialize_files()
            return DatabaseManager.get_users()
        return users

    @staticmethod
    def get_tasks():
        tasks = []
        try:
            with open(TASKS_FILE, 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 8:
                        tasks.append({
                            'id': int(parts[0]),
                            'title': parts[1],
                            'description': parts[2],
                            'category': parts[3],
                            'status': parts[4],
                            'created_by': int(parts[5]),
                            'created_at': parts[6],
                            'assigned_to': int(parts[7])
                        })
        except FileNotFoundError:
            DatabaseManager.initialize_files()
            return DatabaseManager.get_tasks()
        return tasks

    @staticmethod
    def save_users(users):
        try:
            with open(USERS_FILE, 'w') as f:
                for user in users:
                    f.write(f"{user['id']}|{user['username']}|{user['password']}|{user['role']}\n")
            return True
        except Exception as e:
            print(f"Error guardando usuarios: {e}")
            return False

    @staticmethod
    def save_tasks(tasks):
        try:
            with open(TASKS_FILE, 'w') as f:
                for task in tasks:
                    f.write(f"{task['id']}|{task['title']}|{task['description']}|{task['category']}|{task['status']}|{task['created_by']}|{task['created_at']}|{task['assigned_to']}\n")
            return True
        except Exception as e:
            print(f"Error guardando tareas: {e}")
            return False

class Validator:
    @staticmethod
    def validate_username(username):
        if not 3 <= len(username) <= 20:
            return False, "El usuario debe tener entre 3 y 20 caracteres"
        if not re.match("^[a-zA-Z0-9_]+$", username):
            return False, "Solo se permiten letras, números y guiones bajos"
        return True, ""

    @staticmethod
    def validate_password(password):
        if len(password) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        return True, ""

    @staticmethod
    def validate_role(role):
        if role.lower() not in ['admin', 'student']:
            return False, "Rol debe ser 'admin' o 'student'"
        return True, ""

    @staticmethod
    def validate_task_title(title):
        if not title or len(title) > 50:
            return False, "El título debe tener entre 1 y 50 caracteres"
        return True, ""

class AuthService:
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def authenticate(username, password):
        users = DatabaseManager.get_users()
        hashed_password = AuthService.hash_password(password)
        
        for user in users:
            if user['username'] == username and user['password'] == hashed_password:
                return user
        return None

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vishweb Design - Login")
        self.root.geometry("1000x600")
        
        self.frame = ctk.CTkFrame(master=self.root, fg_color="#ffffff")
        self.frame.pack(pady=50, padx=50, fill="both", expand=True)
        
        ctk.CTkLabel(master=self.frame, text="VISHWEB DESIGN", 
                    font=("Arial", 24, "bold"), text_color="#2c3e50").pack(pady=(40,20))
        
        ctk.CTkLabel(master=self.frame, text="Sistema de Gestión de Tareas", 
                    font=("Arial", 14), text_color="#7f8c8d").pack(pady=(0,30))
        
        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Usuario", 
                                         width=300, height=40, border_width=1, 
                                         corner_radius=5, fg_color="#f5f5f5", 
                                         border_color="#bdc3c7")
        self.username_entry.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Contraseña", 
                                         show="*", width=300, height=40, 
                                         border_width=1, corner_radius=5, 
                                         fg_color="#f5f5f5", border_color="#bdc3c7")
        self.password_entry.pack(pady=10)
        
        ctk.CTkButton(master=self.frame, text="Ingresar", command=self.login, 
                     width=300, height=40, fg_color="#3498db", 
                     hover_color="#2980b9", corner_radius=5).pack(pady=20)
        
        self.error_label = ctk.CTkLabel(master=self.frame, text="", text_color="#e74c3c")
        self.error_label.pack(pady=10)
        
        ctk.CTkLabel(master=self.frame, 
                    text="© 2023 Vishweb Design. Todos los derechos reservados.", 
                    font=("Arial", 10), text_color="#95a5a6").pack(side="bottom", pady=20)
    
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        is_valid, message = Validator.validate_username(username)
        if not is_valid:
            self.error_label.configure(text=message)
            return
        
        is_valid, message = Validator.validate_password(password)
        if not is_valid:
            self.error_label.configure(text=message)
            return
        
        user = AuthService.authenticate(username, password)
        
        if user:
            self.root.destroy()
            if user['role'] == 'admin':
                AdminApp(user)
            else:
                StudentApp(user)
        else:
            self.error_label.configure(text="Credenciales inválidas")

class AdminApp:
    def __init__(self, user):
        self.user = user
        self.root = ctk.CTk()
        self.root.title(f"Admin Dashboard - {user['username']}")
        self.root.geometry("1200x700")
        
        # Configuración de la interfaz
        self.setup_ui()
        self.root.mainloop()
    
    def setup_ui(self):
        # Implementar interfaz admin
        pass

class StudentApp:
    def __init__(self, user):
        self.user = user
        self.root = ctk.CTk()
        self.root.title(f"Estudiante - {user['username']}")
        self.root.geometry("1200x700")
        
        # Configuración de la interfaz
        self.setup_ui()
        self.root.mainloop()
    
    def setup_ui(self):
        # Implementar interfaz estudiante
        pass

def main():
    DatabaseManager.initialize_files()
    root = ctk.CTk()
    LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()