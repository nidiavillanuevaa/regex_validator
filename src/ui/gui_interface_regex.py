
import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Agregar carpeta src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.heuristics import generar_regex_heuristica
from ai.evaluator import evaluar_regex



print("Iniciando GUI...")
# Crear ventana principal
root = tk.Tk()
root.title("Crear Expresiones Regulares")
root.geometry("400x300")
# Forzar ventana al frente
root.lift()
root.attributes('-topmost', True)
root.after(100, lambda: root.attributes('-topmost', False))

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)


# Campos de entrada
ttk.Label(frame, text="Expresiones Positivas:").grid(row=0, column=0, sticky="w")
entry_regex = ttk.Entry(frame, width=30)
entry_regex.grid(row=0, column=1, pady=5, padx=5)

ttk.Label(frame, text="Expresiones Negativas:").grid(row=1, column=0, sticky="w")
entry_cadena = ttk.Entry(frame, width=30)
entry_cadena.grid(row=1, column=1, pady=5, padx=5)


# Función para validar
def validar():
	positivos = [s.strip() for s in entry_regex.get().split(',') if s.strip()]
	negativos = [s.strip() for s in entry_cadena.get().split(',') if s.strip()]
	if not positivos:
		messagebox.showerror("Error", "Ingresa al menos un ejemplo positivo.")
		return
	regex = generar_regex_heuristica(positivos)
	resultado = evaluar_regex(regex, positivos, negativos)
	result_text.delete(1.0, tk.END)
	result_text.insert(tk.END, f"Regex generada: {regex}\n")
	result_text.insert(tk.END, f"Evaluación: {resultado}\n")

btn_validar = ttk.Button(frame, text="Validar", command=validar)
btn_validar.grid(row=2, column=0, columnspan=2, pady=10)

# Área de resultados
result_text = tk.Text(frame, height=10, width=45)
result_text.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
