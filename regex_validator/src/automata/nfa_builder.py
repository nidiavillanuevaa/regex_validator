class State:
    def __init__(self):
        # Transiciones por símbolo: { 'a': [estado1, estado2] }
        self.transitions = {}
        # Transiciones por epsilon: [estado1, estado2]
        self.epsilon = []

class NFA:
    def __init__(self, start, accept):
        self.start = start      # Estado inicial
        self.accept = accept    # Estado de aceptación
        
def build_nfa(postfix: str) -> NFA:
    """Construye un AFN a partir de una expresión regular en postfijo usando el algoritmo de Thompson."""
    stack = []

    for c in postfix:
        if c == '*':
            # Cierre de Kleene
            nfa = stack.pop()
            start = State()
            accept = State()
            start.epsilon += [nfa.start, accept]
            nfa.accept.epsilon += [nfa.start, accept]
            stack.append(NFA(start, accept))

        elif c == '|':
            # Unión (OR)
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon += [nfa1.start, nfa2.start]
            nfa1.accept.epsilon.append(accept)
            nfa2.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))

        elif c == '.':
            # Concatenación
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept.epsilon.append(nfa2.start)
            stack.append(NFA(nfa1.start, nfa2.accept))

        elif c == '+':
            # Uno o más repeticiones (como A+)
            nfa = stack.pop()
            start = State()
            accept = State()
            start.epsilon.append(nfa.start)
            nfa.accept.epsilon += [nfa.start, accept]
            stack.append(NFA(start, accept))

        elif c == '?':
            # Cero o una ocurrencia (como A?)
            nfa = stack.pop()
            start = State()
            accept = State()
            start.epsilon += [nfa.start, accept]
            nfa.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))

        else:
            # Símbolo literal
            start = State()
            accept = State()
            start.transitions[c] = [accept]
            stack.append(NFA(start, accept))

    return stack.pop()
