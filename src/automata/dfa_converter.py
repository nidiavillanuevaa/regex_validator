from src.automata.automata_simulator import epsilon_closure, move
from src.automata.nfa_builder import State, NFA

class DFAState:
    _id_counter = 0

    def __init__(self, nfa_states):
        self.id = DFAState._id_counter
        DFAState._id_counter += 1
        self.nfa_states = frozenset(nfa_states)
        self.transitions = {}

    def __repr__(self):
        return f"D{self.id}"

def nfa_to_dfa(nfa: NFA):
    """Convierte un AFN a un AFD usando el algoritmo de subconjuntos."""

    start_closure = frozenset(epsilon_closure([nfa.start]))
    dfa_states_map = {}  # {frozenset: DFAState}
    dfa_start = DFAState(start_closure)
    dfa_states_map[start_closure] = dfa_start
    unmarked = [dfa_start]
    dfa_accepting = set()

    while unmarked:
        current = unmarked.pop()

        # Obtener todos los símbolos posibles desde estos estados
        symbols = set()
        for state in current.nfa_states:
            symbols.update(state.transitions.keys())

        for symbol in symbols:
            # Mover por el símbolo y cerrar por epsilon
            next_nfa_states = set()
            for nfa_state in current.nfa_states:
                next_nfa_states.update(move([nfa_state], symbol))

            closure = frozenset(epsilon_closure(next_nfa_states))
            if closure not in dfa_states_map:
                new_state = DFAState(closure)
                dfa_states_map[closure] = new_state
                unmarked.append(new_state)

            current.transitions[symbol] = dfa_states_map[closure]

    # Determinar estados de aceptación
    for dfa_state in dfa_states_map.values():
        if nfa.accept in dfa_state.nfa_states:
            dfa_accepting.add(dfa_state)

    return dfa_start, list(dfa_states_map.values()), dfa_accepting
