import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Agregar carpeta src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from automata.regex_parser import to_postfix
from automata.nfa_builder import build_nfa
from automata.automata_simulator import simulate_nfa_with_trace
from automata.dfa_converter import nfa_to_dfa
from automata.automata_simulator import simulate_dfa
from automata.automata_visualizer import draw_nfa, draw_dfa

def validar():
    regex = entry_regex.get()
    cadena = entry_cadena.get()

    if not regex or not cadena:
        messagebox.showwarning("Advertencia", "Ingrese la regex y la cadena.")
        return

    postfix = to_postfix(regex)
    nfa = build_nfa(postfix)

    aceptado_nfa, camino_nfa = simulate_nfa_with_trace(nfa, cadena)
    dfa_start, _, dfa_accepting = nfa_to_dfa(nfa)
    aceptado_dfa, traza_dfa = simulate_dfa(dfa_start, cadena, dfa_accepting)

    # Mostrar resultados
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"AFN: {'Aceptada' if aceptado_nfa else 'Rechazada'}\n")
    result_text.insert(tk.END, "Estados recorridos AFN:\n")
    for i, step in enumerate(camino_nfa):
        result_text.insert(tk.END, f"  Paso {i}: {', '.join(str(s) for s in step)}\n")

    result_text.insert(tk.END, f"\nAFD: {'Aceptada' if aceptado_dfa else 'Rechazada'}\n")
    result_text.insert(tk.END, "Camino recorrido en el AFD:\n")
    for paso, estado in enumerate(traza_dfa):
        result_text.insert(tk.END, f"  Paso {paso}: {estado}\n")

def mostrar_afn():
    regex = entry_regex.get()
    if not regex:
        messagebox.showwarning("Advertencia", "Ingrese la regex.")
        return
    postfix = to_postfix(regex)
    nfa = build_nfa(postfix)
    draw_nfa(nfa)

def mostrar_afd():
    regex = entry_regex.get()
    if not regex:
        messagebox.showwarning("Advertencia", "Ingrese la regex.")
        return
    postfix = to_postfix(regex)
    nfa = build_nfa(postfix)
    dfa_start, _, dfa_accepting = nfa_to_dfa(nfa)
    draw_dfa(dfa_start, dfa_accepting)

# Crear ventana principal
root = tk.Tk()
root.title("Validador de Expresiones Regulares")
root.geometry("700x500")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Campos de entrada
ttk.Label(frame, text="Expresión Regular:").grid(row=0, column=0, sticky="w")
entry_regex = ttk.Entry(frame, width=40)
entry_regex.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Cadena a validar:").grid(row=1, column=0, sticky="w")
entry_cadena = ttk.Entry(frame, width=40)
entry_cadena.grid(row=1, column=1, pady=5)

# Botones
ttk.Button(frame, text="Validar", command=validar).grid(row=2, column=0, pady=5)
ttk.Button(frame, text="Mostrar AFN", command=mostrar_afn).grid(row=2, column=1, pady=5, sticky="w")
ttk.Button(frame, text="Mostrar AFD", command=mostrar_afd).grid(row=2, column=1, pady=5, sticky="e")

# Área de resultados
result_text = tk.Text(frame, height=20)
result_text.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
