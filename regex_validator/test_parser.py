from src.automata.nfa_builder import State, NFA

# Creamos dos estados
s1 = State()
s2 = State()

# Creamos un NFA básico de s1 a s2 con símbolo 'a'
s1.transitions['a'] = [s2]
nfa = NFA(s1, s2)

# Verificamos
print(nfa.start.transitions)  # Debe imprimir: {'a': [<__main__.State object at ...>]}

from src.automata.regex_parser import to_postfix
from src.automata.nfa_builder import build_nfa

postfix = to_postfix("a(b|c)*")
nfa = build_nfa(postfix)

print("Estado inicial:", nfa.start)
print("Transiciones del estado inicial:", nfa.start.transitions)
print("Transiciones epsilon del estado inicial:", nfa.start.epsilon)
