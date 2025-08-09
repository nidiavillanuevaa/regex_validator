import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from automata.regex_parser import to_postfix
from automata.nfa_builder import build_nfa
from automata.automata_simulator import simulate_nfa_with_trace
from automata.dfa_converter import nfa_to_dfa
from automata.automata_simulator import simulate_dfa

# Prueba con AFN
regex = "a(b|c)*"
cadena = "abcbcb"

postfix = to_postfix(regex)
nfa = build_nfa(postfix)
aceptado_nfa, camino_nfa = simulate_nfa_with_trace(nfa, cadena)

print(f"\n AFN:")
print(f"¿'{cadena}' es aceptada por '{regex}'?:", "SÍ" if aceptado_nfa else "NO")
print("Estados recorridos:")
for i, step in enumerate(camino_nfa):
    print(f"Paso {i}: {', '.join(str(s) for s in step)}")

# Conversión a AFD
dfa_start, dfa_states, dfa_accepting = nfa_to_dfa(nfa)

print(f"\n AFD generado:")
print(f"Estado inicial: {dfa_start}")
for state in dfa_states:
    for symbol, target in state.transitions.items():
        print(f"{state} --{symbol}--> {target}")
print("Estados de aceptación:", [str(s) for s in dfa_accepting])

# Simulación del AFD
aceptado_dfa, traza_dfa = simulate_dfa(dfa_start, cadena, dfa_accepting)

print(f"\n AFD:")
print(f"¿'{cadena}' es aceptada?: {' SÍ' if aceptado_dfa else ' NO'}")
print("Camino recorrido en el AFD:")
for paso, estado in enumerate(traza_dfa):
    print(f"Paso {paso}: {estado}")
    
from automata.automata_visualizer import draw_nfa, draw_dfa

# Dibujar AFN
draw_nfa(nfa)

# Dibujar AFD
draw_dfa(dfa_start, dfa_accepting)
