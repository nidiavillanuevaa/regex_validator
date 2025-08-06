def to_postfix(regex: str) -> str:
    """Convierte una expresión regular a notación postfija."""
    precedence = {'*': 3, '+': 3, '?': 3, '.': 2, '|': 1}
    output = ''
    stack = []

    # Inserta el operador de concatenación '.'
    explicit = ''
    for i in range(len(regex)):
        c = regex[i]
        explicit += c
        if i + 1 < len(regex):
            next_c = regex[i + 1]
            if c not in '(|' and next_c not in ')*+?|)':
                explicit += '.'
    regex = explicit

    for c in regex:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # Elimina el '('
        elif c in precedence:
            while stack and stack[-1] in precedence and precedence[c] <= precedence[stack[-1]]:
                output += stack.pop()
            stack.append(c)
        else:
            output += c

    while stack:
        output += stack.pop()

    return output
