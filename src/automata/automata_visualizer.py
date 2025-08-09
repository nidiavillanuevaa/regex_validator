import networkx as nx
import matplotlib.pyplot as plt

def draw_nfa(nfa):
    """Dibuja un AFN usando networkx."""
    G = nx.MultiDiGraph()

    # Agregar nodos y transiciones
    nodes_to_visit = [nfa.start]
    visited = set()

    while nodes_to_visit:
        state = nodes_to_visit.pop()
        if state in visited:
            continue
        visited.add(state)

        # Agregar transiciones normales
        for symbol, targets in state.transitions.items():
            for target in targets:
                G.add_edge(str(state), str(target), label=symbol)
                nodes_to_visit.append(target)

        # Agregar transiciones epsilon
        for target in state.epsilon:
            G.add_edge(str(state), str(target), label='ε')
            nodes_to_visit.append(target)

    # Dibujar
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=1200, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("AFN")
    plt.show()


def draw_dfa(dfa_start, accepting_states):
    """Dibuja un AFD usando networkx."""
    G = nx.MultiDiGraph()
    nodes_to_visit = [dfa_start]
    visited = set()

    while nodes_to_visit:
        state = nodes_to_visit.pop()
        if state in visited:
            continue
        visited.add(state)

        for symbol, target in state.transitions.items():
            G.add_edge(str(state), str(target), label=symbol)
            nodes_to_visit.append(target)

    # Dibujar
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')

    # Colorear estados de aceptación en verde
    node_colors = ['lightgreen' if state in accepting_states else 'lightblue' for state in visited]

    nx.draw(G, pos, with_labels=True, node_size=1200, node_color=node_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("AFD")
    plt.show()
