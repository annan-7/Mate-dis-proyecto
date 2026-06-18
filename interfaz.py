import Algoritmo_dijkstra
import Info_Grafos
import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
import networkx as nx

# configuración de la apariencia de la interfaz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# creación de la ventana principal
ventana = ctk.CTk()
ventana.title("Algoritmo de Dijkstra - Ciudades")
ventana.geometry("720x480")

# ejecuta el algoritmo de dijkstra al hacer click en el botón
def ejecutar_dijkstra():
    inicio = entry_inicio.get().lower().strip()
    destino = entry_destino.get().lower().strip()
    
    if inicio not in Info_Grafos.grafo_ciudades or destino not in Info_Grafos.grafo_ciudades:
        resultado_label.configure(
            text="Una o ambas ciudades no existen.\nPor favor, ingrese ciudades válidas.",
            text_color="red")
        return
    
    camino, distancia = Algoritmo_dijkstra.dijkstra(Info_Grafos.grafo_ciudades, inicio, destino)

    if camino:
        resultado_label.configure(
            text=f"Camino más corto de {inicio} a {destino}:\n{' -> '.join(camino)}\nDistancia: {distancia}",
            text_color="green")
        mostrar_grafo(camino) # muestra el grafo con el camino resaltado en rojo
    else:
        resultado_label.configure(
            text=f"No hay camino entre {inicio} y {destino}.",
            text_color="red")
        
def construir_grafo():
    G = nx.Graph()
    for nodo, vecinos in Info_Grafos.grafo_ciudades.items():
        for peso, vecino in vecinos:
            G.add_edge(nodo, vecino, weight=peso) # agrega las aristas al grafo con el peso como atributo
    return G

# muestra el grafo con el mejor camino al destino en rojo
def mostrar_grafo(camino):
    plt.close("all")  # cierra cualquier pestaña de grafo abierta si es q se ejecuta varias veces
    G = construir_grafo()

    pos = nx.spring_layout(G, seed=42)  # spring_layout es para mantener la posicion de los nodos consistente entre grafo completo y grafo con camino resaltado
    plt.figure(figsize=(8, 6))

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

    labels = nx.get_edge_attributes(G, 'weight') # obtiene los pesos de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # dibuja los pesos en las aristas
    
    edges_camino = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_camino, edge_color='red', width=2)
    
    plt.title("Grafo de Ciudades con Camino Resaltado")
    plt.show()

# muestra el grafo completo sin ningún camino en rojo
def mostrar_grafo_completo():
    plt.close("all")  # cierra cualquier pestaña de grafo abierta si es q se ejecuta
    G = construir_grafo()
    pos = nx.spring_layout(G, seed=42) # spring_layout es para mantener la posicion de los nodos
    plt.figure(figsize=(8, 6))
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10) # dibuja el grafo con los nodos y las etiquetas
    
    labels = nx.get_edge_attributes(G, 'weight') # obtiene los pesos de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # dibuja los pesos en las aristas
    
    plt.title("Grafo Completo de Ciudades")
    plt.show()

# usamos el menu libreria tkinter para las opciones :V
menu_bar = tk.Menu(ventana)
menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label="Mostrar Grafo Completo", command=mostrar_grafo_completo)
menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
ventana.configure(menu=menu_bar)

# elementos de la interfaz para ingresar las ciudades de origen y destino
label_inicio = ctk.CTkLabel(ventana, text="Ciudad de Origen:")
label_inicio.pack(pady=10)
entry_inicio = ctk.CTkEntry(ventana)
entry_inicio.pack(pady=5)

label_destino = ctk.CTkLabel(ventana, text="Ciudad de Destino:")
label_destino.pack(pady=10)
entry_destino = ctk.CTkEntry(ventana)
entry_destino.pack(pady=5)

boton_ejecutar = ctk.CTkButton(ventana, text="Ejecutar Dijkstra", command=ejecutar_dijkstra)
boton_ejecutar.pack(pady=20)

resultado_label = ctk.CTkLabel(ventana, text="")
resultado_label.pack(pady=10)

ventana.mainloop()