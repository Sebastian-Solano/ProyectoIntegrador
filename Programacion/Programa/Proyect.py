import hashlib
from datetime import datetime
import re
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os

# File paths
USERS_FILE = "users.txt"
TASKS_FILE = "tasks.txt"

# Initialize text files with predefined users
def init_files():
    try:
        # Check if users.txt is empty or doesn't exist
        try:
            with open(USERS_FILE, 'r') as f:
                content = f.read().strip()
                if content:
                    # Verify users.txt integrity
                    lines = content.split('\n')
                    valid = all(len(line.split('|')) == 4 for line in lines if line)
                    if valid:
                        return  # File is valid, no need to initialize
        except (FileNotFoundError, IOError):
            pass

        # Create users.txt with predefined users (updated hashes from console)
        predefined_users = [
            (1, "admin", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", "admin"),
            (2, "sebas", "70bd8714a2d856538c68cb92919d6573f4c690959e148dc133f6f043c0e41199", "student")
        ]
        with open(USERS_FILE, 'w') as f:
            for user in predefined_users:
                f.write(f"{user[0]}|{user[1]}|{user[2]}|{user[3]}\n")
        print(f"Initialized users.txt with predefined users: {predefined_users}")

        # Create tasks.txt if it doesn't exist
        with open(TASKS_FILE, 'a') as f:
            pass
    except IOError as e:
        print(f"Error initializing files: {e}")

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Validation functions
def validate_username(username):
    if not username or len(username) < 3 or len(username) > 20 or not re.match("^[a-zA-Z0-9_]+$", username):
        return False, "Username must be 3-20 characters, letters, numbers, or underscores"
    return True, ""

def validate_password(password):
    if not password or len(password) < 6:
        return False, "Password must be at least 6 characters"
    return True, ""

def validate_role(role):
    if role.lower() not in ['admin', 'student']:
        return False, "Role must be 'admin' or 'student'"
    return True, ""

def validate_title(title):
    if not title or len(title) > 50:
        return False, "Title must be 1-50 characters"
    return True, ""

def validate_description(description):
    if len(description) > 200:
        return False, "Description cannot exceed 200 characters"
    return True, ""

def validate_category(category):
    if len(category) > 30:
        return False, "Category cannot exceed 30 characters"
    return True, ""

def validate_status(status):
    if status.lower() not in ['pending', 'in_progress', 'completed']:
        return False, "Status must be 'pending', 'in_progress', or 'completed'"
    return True, ""

def validate_id(id_input):
    try:
        entity_id = int(id_input)
        if entity_id <= 0:
            return False, "ID must be a positive integer"
        return True, entity_id
    except ValueError:
        return False, "ID must be a valid integer"

# Read users from users.txt
def read_users():
    users = []
    try:
        with open(USERS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    users.append((int(parts[0]), parts[1], parts[2], parts[3]))
    except FileNotFoundError:
        print("users.txt not found, reinitializing...")
        init_files()
        return read_users()  # Retry after reinitializing
    except IOError as e:
        print(f"Error reading users.txt: {e}")
    return users

# Read tasks from tasks.txt
def read_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 8:
                    tasks.append((int(parts[0]), parts[1], parts[2], parts[3], parts[4], int(parts[5]), parts[6], int(parts[7])))
    except FileNotFoundError:
        pass
    except IOError as e:
        print(f"Error reading tasks.txt: {e}")
    return tasks

# Get next ID for users or tasks
def get_next_id(file_path):
    max_id = 0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if parts and parts[0].isdigit():
                    max_id = max(max_id, int(parts[0]))
    except FileNotFoundError:
        pass
    return max_id + 1

# Login window
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(master=self.frame, text="User & Task Manager Login").pack(pady=10)
        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username", width=300)
        self.username_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*", width=300)
        self.password_entry.pack(pady=10)
        ctk.CTkButton(master=self.frame, text="Login", command=self.login, width=150).pack(pady=10)
        self.error_label = ctk.CTkLabel(master=self.frame, text="", text_color="red")
        self.error_label.pack(pady=10)

    def login(self):
        try:
            username = self.username_entry.get().strip()
            is_valid, message = validate_username(username)
            if not is_valid:
                self.error_label.configure(text=message)
                return

            password = self.password_entry.get()
            is_valid, message = validate_password(password)
            if not is_valid:
                self.error_label.configure(text=message)
                return

            users = read_users()
            print(f"Login attempt: username={username}, hashed_password={hash_password(password)}")
            print(f"Users in file: {users}")
            user = next((u for u in users if u[1] == username and u[2] == hash_password(password)), None)

            if user:
                print(f"Login successful for user: {user}")
                self.root.destroy()
                if user[3].lower() == 'admin':
                    AdminApp(user={'id': user[0], 'username': username, 'role': 'admin'})
                else:
                    StudentApp(user={'id': user[0], 'username': username, 'role': 'student'})
            else:
                self.error_label.configure(text="Invalid credentials")
                print("Login failed: Invalid credentials")
        except Exception as e:
            print(f"Error in login: {e}")
            self.error_label.configure(text="An error occurred during login")

# Admin application
class AdminApp:
    def __init__(self, user):
        self.user = user
        self.root = ctk.CTk()
        self.root.title("Admin Dashboard")
        self.root.geometry("1400x700")  # Increased for wider layout
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.tabview = ctk.CTkTabview(master=self.root)
        self.tabview.pack(pady=20, padx=20, fill="both", expand=True)
        self.tabview.add("Users")
        self.tabview.add("Tasks")
        self.tabview.add("Task Progress")

        self.setup_user_tab()
        self.setup_task_tab()
        self.setup_progress_tab()

        # Ensure Logout button is visible
        self.logout_button = ctk.CTkButton(master=self.root, text="Logout", command=self.logout, width=150)
        self.logout_button.pack(pady=15, side="bottom")
        print("Logout button packed in Admin Dashboard")

        self.root.mainloop()

    def setup_user_tab(self):
        frame = self.tabview.tab("Users")
        ctk.CTkLabel(master=frame, text="Create User").grid(row=0, column=0, columnspan=4, padx=20, pady=15, sticky="w")
        self.user_username_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=300)
        self.user_username_entry.grid(row=1, column=0, padx=20, pady=15, sticky="w")
        self.user_password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*", width=300)
        self.user_password_entry.grid(row=1, column=1, padx=20, pady=15, sticky="w")
        self.user_role_entry = ctk.CTkEntry(master=frame, placeholder_text="Role (admin/student)", width=300)
        self.user_role_entry.grid(row=1, column=2, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=frame, text="Create", command=self.create_user, width=150).grid(row=1, column=3, padx=20, pady=15, sticky="w")
        self.user_error_label = ctk.CTkLabel(master=frame, text="", text_color="red")
        self.user_error_label.grid(row=2, column=0, columnspan=4, padx=20, pady=15, sticky="w")

        ctk.CTkButton(master=frame, text="Refresh Users", command=self.view_users, width=150).grid(row=3, column=0, padx=20, pady=15, sticky="w")
        self.user_table_frame = ctk.CTkFrame(master=frame)
        self.user_table_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.view_users()

        ctk.CTkLabel(master=frame, text="Update/Delete User").grid(row=5, column=0, columnspan=4, padx=20, pady=15, sticky="w")
        self.user_id_entry = ctk.CTkEntry(master=frame, placeholder_text="User ID", width=300)
        self.user_id_entry.grid(row=6, column=0, padx=20, pady=15, sticky="w")
        self.user_new_role_entry = ctk.CTkEntry(master=frame, placeholder_text="New Role (admin/student)", width=300)
        self.user_new_role_entry.grid(row=6, column=1, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=frame, text="Update", command=self.update_user, width=150).grid(row=6, column=2, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=frame, text="Delete", command=self.delete_user, width=150).grid(row=6, column=3, padx=20, pady=15, sticky="w")
        self.user_action_error_label = ctk.CTkLabel(master=frame, text="", text_color="red")
        self.user_action_error_label.grid(row=7, column=0, columnspan=4, padx=20, pady=15, sticky="w")

    def setup_task_tab(self):
        print("Setting up Tasks tab with wider components: width=300 for fields, 150 for buttons")
        frame = self.tabview.tab("Tasks")
        # Create Task section
        create_frame = ctk.CTkFrame(master=frame)
        create_frame.grid(row=0, column=0, columnspan=5, padx=20, pady=15, sticky="ew")
        ctk.CTkLabel(master=create_frame, text="Create Task").grid(row=0, column=0, columnspan=5, padx=20, pady=15, sticky="w")
        self.task_title_entry = ctk.CTkEntry(master=create_frame, placeholder_text="Title", width=300)
        self.task_title_entry.grid(row=1, column=0, padx=20, pady=15, sticky="w")
        self.task_description_entry = ctk.CTkEntry(master=create_frame, placeholder_text="Description", width=300)
        self.task_description_entry.grid(row=1, column=1, padx=20, pady=15, sticky="w")
        self.task_category_entry = ctk.CTkEntry(master=create_frame, placeholder_text="Category", width=300)
        self.task_category_entry.grid(row=1, column=2, padx=20, pady=15, sticky="w")
        self.task_assigned_to = ctk.CTkComboBox(master=create_frame, values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'], width=300)
        self.task_assigned_to.grid(row=1, column=3, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=create_frame, text="Create", command=self.create_task, width=150).grid(row=1, column=4, padx=20, pady=15, sticky="w")
        self.task_error_label = ctk.CTkLabel(master=frame, text="", text_color="red")
        self.task_error_label.grid(row=1, column=0, columnspan=5, padx=20, pady=15, sticky="w")

        # Refresh Tasks button
        ctk.CTkButton(master=frame, text="Refresh Tasks", command=self.view_tasks, width=150).grid(row=2, column=0, padx=20, pady=15, sticky="w")

        # Task table
        self.task_table_frame = ctk.CTkScrollableFrame(master=frame, orientation="horizontal")
        self.task_table_frame.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        self.view_tasks()

        # Update/Delete Task section
        update_frame = ctk.CTkFrame(master=frame)
        update_frame.grid(row=4, column=0, columnspan=5, padx=20, pady=15, sticky="ew")
        ctk.CTkLabel(master=update_frame, text="Update/Delete Task").grid(row=0, column=0, columnspan=5, padx=20, pady=15, sticky="w")
        self.task_id_entry = ctk.CTkEntry(master=update_frame, placeholder_text="Task ID", width=300)
        self.task_id_entry.grid(row=1, column=0, padx=20, pady=15, sticky="w")
        self.task_status_entry = ctk.CTkEntry(master=update_frame, placeholder_text="Status (pending/in_progress/completed)", width=300)
        self.task_status_entry.grid(row=1, column=1, padx=20, pady=15, sticky="w")
        self.task_assign_entry = ctk.CTkComboBox(master=update_frame, values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'], width=300)
        self.task_assign_entry.grid(row=1, column=2, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=update_frame, text="Update", command=self.update_task, width=150).grid(row=1, column=3, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=update_frame, text="Delete", command=self.delete_task, width=150).grid(row=1, column=4, padx=20, pady=15, sticky="w")
        self.task_action_error_label = ctk.CTkLabel(master=frame, text="", text_color="red")
        self.task_action_error_label.grid(row=5, column=0, columnspan=5, padx=20, pady=15, sticky="w")

    def setup_progress_tab(self):
        frame = self.tabview.tab("Task Progress")
        self.user_filter = ctk.CTkComboBox(master=frame, values=["All Users"] + [u[1] for u in read_users() if u[3] == 'student'], command=self.generate_task_report, width=300)
        self.user_filter.grid(row=0, column=0, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=frame, text="Refresh Report", command=self.generate_task_report, width=150).grid(row=0, column=1, padx=20, pady=15, sticky="w")
        self.progress_frame = ctk.CTkFrame(master=frame)
        self.progress_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.generate_task_report()

    def create_user(self):
        username = self.user_username_entry.get().strip()
        is_valid, message = validate_username(username)
        if not is_valid:
            self.user_error_label.configure(text=message)
            return
        password = self.user_password_entry.get()
        is_valid, message = validate_password(password)
        if not is_valid:
            self.user_error_label.configure(text=message)
            return
        role = self.user_role_entry.get().strip().lower()
        is_valid, message = validate_role(role)
        if not is_valid:
            self.user_error_label.configure(text=message)
            return
        users = read_users()
        if any(u[1] == username for u in users):
            self.user_error_label.configure(text="Username already exists")
            return
        user_id = get_next_id(USERS_FILE)
        try:
            with open(USERS_FILE, 'a') as f:
                f.write(f"{user_id}|{username}|{hash_password(password)}|{role}\n")
            self.user_error_label.configure(text="User created successfully", text_color="green")
            self.view_users()
            self.user_filter.configure(values=["All Users"] + [u[1] for u in read_users() if u[3] == 'student'])
            self.task_assigned_to.configure(values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'])
            self.task_assign_entry.configure(values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'])
        except IOError as e:
            self.user_error_label.configure(text=f"Error creating user: {e}")

    def view_users(self):
        for widget in self.user_table_frame.winfo_children():
            widget.destroy()
        users = read_users()
        if not users:
            ctk.CTkLabel(master=self.user_table_frame, text="No users found").pack()
            return
        tree = ttk.Treeview(self.user_table_frame, columns=("ID", "Username", "Role"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.column("ID", width=60)
        tree.column("Username", width=300)
        tree.column("Role", width=150)
        for user in users:
            tree.insert("", tk.END, values=(user[0], user[1], user[3]))
        tree.pack(fill="both", expand=True)

    def update_user(self):
        user_id = self.user_id_entry.get().strip()
        is_valid, result = validate_id(user_id)
        if not is_valid:
            self.user_action_error_label.configure(text=result)
            return
        user_id = result
        role = self.user_new_role_entry.get().strip().lower()
        is_valid, message = validate_role(role)
        if not is_valid:
            self.user_action_error_label.configure(text=message)
            return
        users = read_users()
        user_exists = False
        updated_users = []
        for user in users:
            if user[0] == user_id:
                user_exists = True
                updated_users.append((user[0], user[1], user[2], role))
            else:
                updated_users.append(user)
        if not user_exists:
            self.user_action_error_label.configure(text="User not found")
            return
        try:
            with open(USERS_FILE, 'w') as f:
                for user in updated_users:
                    f.write(f"{user[0]}|{user[1]}|{user[2]}|{user[3]}\n")
            self.user_action_error_label.configure(text="User updated successfully", text_color="green")
            self.view_users()
            self.user_filter.configure(values=["All Users"] + [u[1] for u in read_users() if u[3] == 'student'])
            self.task_assigned_to.configure(values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'])
            self.task_assign_entry.configure(values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'])
        except IOError as e:
            self.user_action_error_label.configure(text=f"Error updating user: {e}")

    def delete_user(self):
        user_id = self.user_id_entry.get().strip()
        is_valid, result = validate_id(user_id)
        if not is_valid:
            self.user_action_error_label.configure(text=result)
            return
        user_id = result
        users = read_users()
        user_to_delete = None
        for user in users:
            if user[0] == user_id:
                user_to_delete = user
                break
        if not user_to_delete:
            self.user_action_error_label.configure(text="User not found")
            return
        if user_to_delete[3] == 'admin' and sum(1 for u in users if u[3] == 'admin') <= 1:
            self.user_action_error_label.configure(text="Cannot delete the last admin user")
            return
        updated_users = [u for u in users if u[0] != user_id]
        try:
            with open(USERS_FILE, 'w') as f:
                for user in updated_users:
                    f.write(f"{user[0]}|{user[1]}|{user[2]}|{user[3]}\n")
            self.user_action_error_label.configure(text="User deleted successfully", text_color="green")
            self.view_users()
            self.user_filter.configure(values=["All Users"] + [u[1] for u in read_users() if u[3] == 'student'])
            self.task_assigned_to.configure(values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'])
            self.task_assign_entry.configure(values=["Unassigned"] + [u[1] for u in read_users() if u[3] == 'student'])
        except IOError as e:
            self.user_action_error_label.configure(text=f"Error deleting user: {e}")

    def create_task(self):
        title = self.task_title_entry.get().strip()
        is_valid, message = validate_title(title)
        if not is_valid:
            self.task_error_label.configure(text=message)
            return
        description = self.task_description_entry.get().strip()
        is_valid, message = validate_description(description)
        if not is_valid:
            self.task_error_label.configure(text=message)
            return
        category = self.task_category_entry.get().strip()
        is_valid, message = validate_category(category)
        if not is_valid:
            self.task_error_label.configure(text=message)
            return
        assigned_to = self.task_assigned_to.get()
        users = read_users()
        assigned_to_id = 0
        if assigned_to != "Unassigned":
            assigned_user = next((u for u in users if u[1] == assigned_to and u[3] == 'student'), None)
            if not assigned_user:
                self.task_error_label.configure(text="Invalid student selected")
                return
            assigned_to_id = assigned_user[0]
        status = "pending"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_id = get_next_id(TASKS_FILE)
        try:
            with open(TASKS_FILE, 'a') as f:
                f.write(f"{task_id}|{title}|{description}|{category}|{status}|{self.user['id']}|{created_at}|{assigned_to_id}\n")
            self.task_error_label.configure(text="Task created successfully", text_color="green")
            self.view_tasks()
        except IOError as e:
            self.task_error_label.configure(text=f"Error creating task: {e}")

    def view_tasks(self):
        for widget in self.task_table_frame.winfo_children():
            widget.destroy()
        tasks = read_tasks()
        users = read_users()
        user_dict = {u[0]: u[1] for u in users}
        if not tasks:
            ctk.CTkLabel(master=self.task_table_frame, text="No tasks found").pack()
            return
        tree = ttk.Treeview(self.task_table_frame, columns=("ID", "Title", "Category", "Status", "Created By", "Created At", "Assigned To"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Category", text="Category")
        tree.heading("Status", text="Status")
        tree.heading("Created By", text="Created By")
        tree.heading("Created At", text="Created At")
        tree.heading("Assigned To", text="Assigned To")
        tree.column("ID", width=60)
        tree.column("Title", width=300)
        tree.column("Category", width=150)
        tree.column("Status", width=150)
        tree.column("Created By", width=150)
        tree.column("Created At", width=200)
        tree.column("Assigned To", width=150)
        for task in tasks:
            created_by = user_dict.get(task[5], "Unknown")
            assigned_to = user_dict.get(task[7], "Unassigned")
            tree.insert("", tk.END, values=(task[0], task[1], task[3], task[4], created_by, task[6], assigned_to))
        tree.pack(fill="both", expand=True)

    def update_task(self):
        task_id = self.task_id_entry.get().strip()
        is_valid, result = validate_id(task_id)
        if not is_valid:
            self.task_action_error_label.configure(text=result)
            return
        task_id = result
        status = self.task_status_entry.get().strip().lower()
        is_valid, message = validate_status(status)
        if not is_valid:
            self.task_action_error_label.configure(text=message)
            return
        assigned_to = self.task_assign_entry.get()
        users = read_users()
        assigned_to_id = 0
        if assigned_to != "Unassigned":
            assigned_user = next((u for u in users if u[1] == assigned_to and u[3] == 'student'), None)
            if not assigned_user:
                self.task_action_error_label.configure(text="Invalid student selected")
                return
            assigned_to_id = assigned_user[0]
        tasks = read_tasks()
        task_exists = False
        updated_tasks = []
        for task in tasks:
            if task[0] == task_id and task[5] == self.user['id']:
                task_exists = True
                updated_tasks.append((task[0], task[1], task[2], task[3], status, task[5], task[6], assigned_to_id))
            else:
                updated_tasks.append(task)
        if not task_exists:
            self.task_action_error_label.configure(text="Task not found or unauthorized")
            return
        try:
            with open(TASKS_FILE, 'w') as f:
                for task in updated_tasks:
                    f.write(f"{task[0]}|{task[1]}|{task[2]}|{task[3]}|{task[4]}|{task[5]}|{task[6]}|{task[7]}\n")
            self.task_action_error_label.configure(text="Task updated successfully", text_color="green")
            self.view_tasks()
        except IOError as e:
            self.task_action_error_label.configure(text=f"Error updating task: {e}")

    def delete_task(self):
        task_id = self.task_id_entry.get().strip()
        is_valid, result = validate_id(task_id)
        if not is_valid:
            self.task_action_error_label.configure(text=result)
            return
        task_id = result
        tasks = read_tasks()
        updated_tasks = [t for t in tasks if t[0] != task_id or t[5] != self.user['id']]
        if len(updated_tasks) == len(tasks):
            self.task_action_error_label.configure(text="Task not found or unauthorized")
            return
        try:
            with open(TASKS_FILE, 'w') as f:
                for task in updated_tasks:
                    f.write(f"{task[0]}|{task[1]}|{task[2]}|{task[3]}|{task[4]}|{task[5]}|{task[6]}|{task[7]}\n")
            self.task_action_error_label.configure(text="Task deleted successfully", text_color="green")
            self.view_tasks()
        except IOError as e:
            self.task_action_error_label.configure(text=f"Error deleting task: {e}")

    def generate_task_report(self, event=None):
        for widget in self.progress_frame.winfo_children():
            widget.destroy()

        tasks = read_tasks()
        users = read_users()
        user_dict = {u[0]: u[1] for u in users}
        selected_user = self.user_filter.get()

        if selected_user != "All Users":
            user_id = next((u[0] for u in users if u[1] == selected_user and u[3] == 'student'), None)
            if user_id is not None:
                tasks = [t for t in tasks if t[7] == user_id]
            else:
                ctk.CTkLabel(master=self.progress_frame, text="No tasks for selected user").pack()
                return

        if not tasks:
            ctk.CTkLabel(master=self.progress_frame, text="No tasks available").pack()
            return

        students = sorted(set(user_dict.get(t[7], "Unassigned") for t in tasks if t[7] != 0 or selected_user == "All Users"))
        if not students:
            ctk.CTkLabel(master=self.progress_frame, text="No tasks assigned to students").pack()
            return

        statuses = ['pending', 'in_progress', 'completed']
        counts = {status: {student: 0 for student in students} for status in statuses}

        for task in tasks:
            if task[7] != 0:  # Only count assigned tasks
                student = user_dict.get(task[7], "Unassigned")
                counts[task[4]][student] += 1

        fig, ax = plt.subplots(figsize=(8, 4))
        bar_width = 0.25
        indices = np.arange(len(students))

        ax.bar(indices - bar_width, [counts['pending'][student] for student in students], bar_width, label='Pending', color='#FFA500')
        ax.bar(indices, [counts['in_progress'][student] for student in students], bar_width, label='In Progress', color='#1E90FF')
        ax.bar(indices + bar_width, [counts['completed'][student] for student in students], bar_width, label='Completed', color='#32CD32')

        ax.set_xlabel('Student')
        ax.set_ylabel('Number of Tasks')
        ax.set_title(f"Task Progress Report ({selected_user})")
        ax.set_xticks(indices)
        ax.set_xticklabels(students, rotation=45, ha='right')
        ax.legend()
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.progress_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)

    def logout(self):
        try:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.root.destroy()
            main()
        except Exception as e:
            print(f"Error in logout: {e}")

# Student application
class StudentApp:
    def __init__(self, user):
        self.user = user
        self.root = ctk.CTk()
        self.root.title("Student Dashboard")
        self.root.geometry("1400x700")  # Match Admin window size
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkButton(master=self.frame, text="Refresh Tasks", command=self.view_tasks, width=150).grid(row=0, column=0, padx=20, pady=15, sticky="w")
        self.task_table_frame = ctk.CTkScrollableFrame(master=self.frame, orientation="horizontal")
        self.task_table_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.view_tasks()

        ctk.CTkLabel(master=self.frame, text="Update Task Status").grid(row=2, column=0, columnspan=3, padx=20, pady=15, sticky="w")
        self.task_id_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Task ID", width=300)
        self.task_id_entry.grid(row=3, column=0, padx=20, pady=15, sticky="w")
        self.task_status_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Status (pending/in_progress/completed)", width=300)
        self.task_status_entry.grid(row=3, column=1, padx=20, pady=15, sticky="w")
        ctk.CTkButton(master=self.frame, text="Update Status", command=self.update_task, width=150).grid(row=3, column=2, padx=20, pady=15, sticky="w")
        self.task_action_error_label = ctk.CTkLabel(master=self.frame, text="", text_color="red")
        self.task_action_error_label.grid(row=4, column=0, columnspan=3, padx=20, pady=15, sticky="w")

        ctk.CTkButton(master=self.frame, text="Logout", command=self.logout, width=150).grid(row=5, column=0, padx=20, pady=15, sticky="w")
        print("Logout button packed in Student Dashboard")
        self.root.mainloop()

    def view_tasks(self):
        for widget in self.task_table_frame.winfo_children():
            widget.destroy()
        tasks = read_tasks()
        users = read_users()
        user_dict = {u[0]: u[1] for u in users}
        # Students see all tasks created by admin
        tasks = [t for t in tasks if t[5] == 1]  # Admin ID is 1
        if not tasks:
            ctk.CTkLabel(master=self.task_table_frame, text="No tasks assigned").pack()
            return
        tree = ttk.Treeview(self.task_table_frame, columns=("ID", "Title", "Category", "Status", "Created By", "Created At", "Assigned To", "Actions"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Category", text="Category")
        tree.heading("Status", text="Status")
        tree.heading("Created By", text="Created By")
        tree.heading("Created At", text="Created At")
        tree.heading("Assigned To", text="Assigned To")
        tree.heading("Actions", text="Actions")
        tree.column("ID", width=60)
        tree.column("Title", width=300)
        tree.column("Category", width=150)
        tree.column("Status", width=150)
        tree.column("Created By", width=150)
        tree.column("Created At", width=200)
        tree.column("Assigned To", width=150)
        tree.column("Actions", width=250)
        for task in tasks:
            created_by = user_dict.get(task[5], "Unknown")
            assigned_to = user_dict.get(task[7], "Unassigned")
            values = (task[0], task[1], task[3], task[4], created_by, task[6], assigned_to, "")
            tree.insert("", tk.END, iid=str(task[0]), values=values)
            if task[7] == self.user['id']:  # Add buttons for tasks assigned to the student
                frame = ctk.CTkFrame(master=self.task_table_frame)
                ctk.CTkButton(master=frame, text="Pending", command=lambda t=task[0]: self.update_task_status(t, "pending"), width=80).pack(side=tk.LEFT, padx=2)
                ctk.CTkButton(master=frame, text="In Progress", command=lambda t=task[0]: self.update_task_status(t, "in_progress"), width=80).pack(side=tk.LEFT, padx=2)
                ctk.CTkButton(master=frame, text="Completed", command=lambda t=task[0]: self.update_task_status(t, "completed"), width=80).pack(side=tk.LEFT, padx=2)
                tree.insert("", tk.END, values=("", "", "", "", "", "", "", frame), tags=("buttons",))
        tree.tag_configure("buttons", background="white")
        tree.pack(fill="both", expand=True)

    def update_task_status(self, task_id, status):
        tasks = read_tasks()
        task_exists = False
        updated_tasks = []
        for task in tasks:
            if task[0] == task_id and task[7] == self.user['id']:
                task_exists = True
                updated_tasks.append((task[0], task[1], task[2], task[3], status, task[5], task[6], task[7]))
            else:
                updated_tasks.append(task)
        if not task_exists:
            self.task_action_error_label.configure(text="Task not found or not assigned to you")
            return
        try:
            with open(TASKS_FILE, 'w') as f:
                for task in updated_tasks:
                    f.write(f"{task[0]}|{task[1]}|{task[2]}|{task[3]}|{task[4]}|{task[5]}|{task[6]}|{task[7]}\n")
            self.task_action_error_label.configure(text=f"Task {task_id} status updated to {status}", text_color="green")
            self.view_tasks()
        except IOError as e:
            self.task_action_error_label.configure(text=f"Error updating task: {e}")

    def update_task(self):
        task_id = self.task_id_entry.get().strip()
        is_valid, result = validate_id(task_id)
        if not is_valid:
            self.task_action_error_label.configure(text=result)
            return
        task_id = result
        status = self.task_status_entry.get().strip().lower()
        is_valid, message = validate_status(status)
        if not is_valid:
            self.task_action_error_label.configure(text=message)
            return
        tasks = read_tasks()
        task_exists = False
        updated_tasks = []
        for task in tasks:
            if task[0] == task_id and task[7] == self.user['id']:
                task_exists = True
                updated_tasks.append((task[0], task[1], task[2], task[3], status, task[5], task[6], task[7]))
            else:
                updated_tasks.append(task)
        if not task_exists:
            self.task_action_error_label.configure(text="Task not found or not assigned to you")
            return
        try:
            with open(TASKS_FILE, 'w') as f:
                for task in updated_tasks:
                    f.write(f"{task[0]}|{task[1]}|{task[2]}|{task[3]}|{task[4]}|{task[5]}|{task[6]}|{task[7]}\n")
            self.task_action_error_label.configure(text="Task status updated successfully", text_color="green")
            self.view_tasks()
        except IOError as e:
            self.task_action_error_label.configure(text=f"Error updating task: {e}")

    def logout(self):
        try:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.root.destroy()
            main()
        except Exception as e:
            print(f"Error in logout: {e}")

# Main function
def main():
    init_files()
    root = ctk.CTk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()