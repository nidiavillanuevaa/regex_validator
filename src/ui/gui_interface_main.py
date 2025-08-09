import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

# Ruta base de los scripts
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Funciones para abrir las interfaces


# Control de instancias
proceso_regex = None
proceso_otro = None

def abrir_interfaz_regex():
    global proceso_regex
    if proceso_regex is None or proceso_regex.poll() is not None:
        path = os.path.join(BASE_PATH, 'gui_interface_regex.py')
        proceso_regex = subprocess.Popen([sys.executable, path])
        btn_regex.config(state='disabled')
        root.after(1000, checar_regex)

def checar_regex():
    global proceso_regex
    if proceso_regex is not None and proceso_regex.poll() is None:
        root.after(1000, checar_regex)
    else:
        btn_regex.config(state='normal')
        proceso_regex = None

def abrir_interfaz_otro():
    global proceso_otro
    if proceso_otro is None or proceso_otro.poll() is not None:
        path = os.path.join(BASE_PATH, 'gui_interface.py')
        proceso_otro = subprocess.Popen([sys.executable, path])
        btn_otro.config(state='disabled')
        root.after(1000, checar_otro)

def checar_otro():
    global proceso_otro
    if proceso_otro is not None and proceso_otro.poll() is None:
        root.after(1000, checar_otro)
    else:
        btn_otro.config(state='normal')
        proceso_otro = None

# Crear ventana principal
root = tk.Tk()
root.title('Selector de Interfaz - Validador de Expresiones Regulares')
root.geometry('400x250')
root.configure(bg='#f0f4f8')

frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

label = ttk.Label(frame, text='Selecciona la Opcion que deseas usar:', font=('Segoe UI', 13, 'bold'))
label.pack(pady=20)

btn_regex = ttk.Button(frame, text='Interfaz de Ejemplos Positivos/Negativos', command=abrir_interfaz_regex)
btn_regex.pack(pady=10, fill='x')

btn_otro = ttk.Button(frame, text='Interfaz de Expresión Regular y Cadena', command=abrir_interfaz_otro)
btn_otro.pack(pady=10, fill='x')

root.mainloop()
