import tkinter as tk
import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Info_Grafos 
import Algoritmo_dijkstra 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Interfaz con Grafo Delimitado")
ventana.geometry("1080x720")

parte_grafo = ctk.CTkFrame(ventana, width=700, height=600, corner_radius=10)
parte_grafo.pack(side="right", padx=20, pady=20, fill="both", expand=True)

parte_grafo.pack_propagate(False) #no cambia de tamaño


contador_clicks = 0 # para clickear los nodos y ver si es 1er o 2do click

def dibujar_grafo_en_interfaz(camino_resaltado=None):
    for elemento in parte_grafo.winfo_children():
        elemento.destroy()
    G = nx.Graph()
    for nodo, vecinos in Info_Grafos.grafo_ciudades.items():
        for peso, vecino in vecinos:
            G.add_edge(nodo, vecino, weight=peso) #se grafica el grafo creado

    pos = nx.spring_layout(G, seed=42, k=0.6, scale=2) #la K separa los nodos y para que no se aprieten tant
    
    # crea la figura ajustada
    fig, ax = plt.subplots(figsize=(7, 6), dpi=100)
    
    colores_nodos = []
    for nodo in G.nodes():
        if camino_resaltado and nodo in camino_resaltado:
            if nodo == camino_resaltado[0]:       
                colores_nodos.append('green')
            elif nodo == camino_resaltado[-1]:    
                colores_nodos.append('purple')
            else:                                  
                colores_nodos.append('red')
        else:
            colores_nodos.append('lightblue')

    aristas_camino = []
    if camino_resaltado:
        aristas_camino = list(zip(camino_resaltado[:-1], camino_resaltado[1:]))

    colores_aristas = []
    anchos_aristas = []
    for u, v in G.edges():
        if (u, v) in aristas_camino or (v, u) in aristas_camino: 
            colores_aristas.append('red')
            anchos_aristas.append(3)
        else:
            colores_aristas.append('gray')
            anchos_aristas.append(1)
    
    # se hace el margen para que se vea bien el grafo
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)

    # se grafican los nodos (ahora dinámico)
    nx.draw_networkx_nodes(G, pos, node_color=colores_nodos, node_size=700, ax=ax)
    
    # se grafican las aristas (ahora dinámico)
    nx.draw_networkx_edges(G, pos, edge_color=colores_aristas, width=anchos_aristas, ax=ax)
    
    # se ponen los nombres de las ciudades
    nx.draw_networkx_labels(G, pos, font_size=7, font_weight="bold", ax=ax)

    # se el peso de cada nodo
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6, ax=ax)

    # se ocultan los numeritos de matplotlib
    ax.axis('off') 

    # se convierte el frame de matplotlib a tkinter
    canvas = FigureCanvasTkAgg(fig, master=parte_grafo)  
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

   
    #busca el nodo cercano al click y ponerlo en los entry box
    def obtener_nodo_mas_cercano(click_x, click_y, posiciones):
        mejor_nodo = None #esta vacio por el momento nomas
        mejor_distancia = float('inf')
        
        for nombre, (px, py) in posiciones.items(): #recorre los nodos y guarda sus coords
            distanciaa = ((click_x - px)**2 + (click_y - py)**2)**0.5 #con pitagoras calcula la distancia de click al noodo
            if distanciaa < mejor_distancia:
                mejor_distancia = distanciaa
                mejor_nodo = nombre
        return mejor_nodo if mejor_distancia < 0.2 else None

    def clickear_en_grafo(click):
        global contador_clicks
        if click.inaxes is None: return
        
        x, y = click.xdata, click.ydata
        if x is None or y is None: return

        nodo = obtener_nodo_mas_cercano(x, y, pos)
        
        if nodo:
            if contador_clicks== 0: # si es el primer click
                entry_inicio.delete(0, "end")
                entry_inicio.insert(0, nodo)
                contador_clicks = 1
            elif contador_clicks == 1: # si es el segundo click
                entry_destino.delete(0, "end")
                entry_destino.insert(0, nodo)

    canvas.mpl_connect('button_press_event', clickear_en_grafo)


# ejecuta el algoritmo de dijkstra al hacer click en el botón
def ejecutar_dijkstra():
    inicio = entry_inicio.get().lower().strip()
    destino = entry_destino.get().lower().strip() # strip() es para eliminar espacios de un texto
    
    if inicio not in Info_Grafos.grafo_ciudades or destino not in Info_Grafos.grafo_ciudades:
        resultado_label.configure(
            text="Una o ambas ciudades no existen.\nPor favor, ingrese ciudades válidas.",
            text_color="red")
        return
    
    camino, distancia = Algoritmo_dijkstra.dijkstra(Info_Grafos.grafo_ciudades, inicio, destino)

    if camino:
        resultado_label.configure(
            text=f"Camino más corto de {inicio} a {destino}:\n{' -> '.join(camino)}\nDistancia: {distancia} KM",
            text_color="green")
        dibujar_grafo_en_interfaz(camino_resaltado=camino)
    else:
        resultado_label.configure(
            text=f"No hay camino entre {inicio} y {destino}.",
            text_color="red")       

def limpiar_campos():
    entry_inicio.delete(0, "end")
    entry_destino.delete(0, "end")
    resultado_label.configure(text="")
    global contador_clicks
    contador_clicks = 0
    dibujar_grafo_en_interfaz()  

# se cita a la funico de graficarr
dibujar_grafo_en_interfaz()



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

boton_limpiar = ctk.CTkButton(ventana, text="Limpiar", command=limpiar_campos)
boton_limpiar.pack(pady=20)

resultado_label = ctk.CTkLabel(ventana, text="")
resultado_label.pack(pady=10)

#para que no se cierre
ventana.mainloop()
