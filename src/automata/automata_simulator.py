# def epsilon_closure(states):
#     """Devuelve el conjunto de estados alcanzables con transiciones epsilon."""
#     stack = list(states)
#     closure = set(states)

#     while stack:
#         state = stack.pop()
#         for next_state in state.epsilon:
#             if next_state not in closure:
#                 closure.add(next_state)
#                 stack.append(next_state)

#     return closure

# def move(states, symbol):
#     """Devuelve el conjunto de estados alcanzables desde 'states' con el símbolo dado."""
#     result = set()
#     for state in states:
#         if symbol in state.transitions:
#             result.update(state.transitions[symbol])
#     return result

# def simulate_nfa_with_trace(nfa, input_string):
#     """Simula el AFN y devuelve si acepta y el camino recorrido."""
#     current_states = epsilon_closure([nfa.start])
#     trace = [set(current_states)]  # Guardamos estados tras cada símbolo

#     for symbol in input_string:
#         next_states = move(current_states, symbol)
#         current_states = epsilon_closure(next_states)
#         trace.append(set(current_states))

#     accepted = nfa.accept in current_states
#     return accepted, trace

# src/automata/dfa_simulator.py
# src/automata/automata_simulator.py

def epsilon_closure(states):
    """Devuelve el conjunto de estados alcanzables con transiciones epsilon."""
    stack = list(states)
    closure = set(states)

    while stack:
        state = stack.pop()
        for next_state in state.epsilon:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return closure

def move(states, symbol):
    """Devuelve el conjunto de estados alcanzables desde 'states' con el símbolo dado."""
    result = set()
    for state in states:
        if symbol in state.transitions:
            result.update(state.transitions[symbol])
    return result

def simulate_nfa_with_trace(nfa, input_string):
    """Simula el AFN y devuelve si acepta y el camino recorrido."""
    current_states = epsilon_closure([nfa.start])
    trace = [set(current_states)]

    for symbol in input_string:
        next_states = move(current_states, symbol)
        current_states = epsilon_closure(next_states)
        trace.append(set(current_states))

    accepted = nfa.accept in current_states
    return accepted, trace

def simulate_dfa(dfa_start, input_string, accepting_states):
    """Simula un AFD y devuelve si la cadena es aceptada junto con el camino recorrido."""
    current = dfa_start
    trace = [current]

    for symbol in input_string:
        if symbol in current.transitions:
            current = current.transitions[symbol]
            trace.append(current)
        else:
            return False, trace  # No hay transición, rechazada

    return current in accepting_states, trace

