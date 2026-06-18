
import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(grafo_dict, ruta_optima=None):
   
    G = nx.Graph()
    
    for origen, conexiones in grafo_dict.items():
        for peso, destino in conexiones:
            G.add_edge(origen, destino, weight=peso)
            
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42, k=0.5)
    
    # Nodos y etiquetas
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=600)
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    # Aristas base (grises)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.0, alpha=0.5)
    
    # Pesos en las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7)
    
    # RUTA ÓPTIMA DESTACADA
    if ruta_optima and len(ruta_optima) > 1:
        path_edges = list(zip(ruta_optima, ruta_optima[1:]))
        nx.draw_networkx_edges(G, pos, path_edges, edge_color='red', width=3.5, alpha=0.9)
        nx.draw_networkx_nodes(G, pos, nodelist=[ruta_optima[0]], node_color='green', node_size=1000)
        nx.draw_networkx_nodes(G, pos, nodelist=[ruta_optima[-1]], node_color='purple', node_size=1000)
        plt.legend(['Origen', 'Destino', 'Ruta Óptima'], loc='upper right', fontsize=10)

    plt.title("Ruta Óptima Calculada", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
