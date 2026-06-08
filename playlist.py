
class Cancion:
    def __init__(self, id_cancion, titulo, artista):
        self.id = id_cancion
        self.titulo = titulo
        self.artista = artista

# 2. El contenedor (Nodo) con sus dos punteros
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion  # Guarda el objeto Cancion
        self.siguiente = None   # Puntero al que sigue (vacío al inicio)
        self.anterior = None    # Puntero al de atrás (vacío al inicio)

# 3. La estructura de datos que controlará todo
class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None  # Primera canción de la playlist
        self.cola = None    # Última canción de la playlist
        self.actual = None  # Canción que se está reproduciendo actualmente

    # FUNCIÓN 1: Agregar canción al final (La que usarán los clientes)
    def agregar_cancion(self, cancion_nueva):
        nuevo_nodo = Nodo(cancion_nueva)
        
        # Si la lista está vacía, el nuevo nodo es el primero y el último
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.actual = nuevo_nodo  # También se vuelve la actual por defecto
        else:
            # El último nodo actual apunta hacia adelante al nuevo nodo
            self.cola.siguiente = nuevo_nodo
            # El nuevo nodo apunta hacia atrás al que era el último
            nuevo_nodo.anterior = self.cola
            # Ahora el nuevo nodo se convierte en la cola oficial
            self.cola = nuevo_nodo
            
        print(f"🎵 Añadida a la fila: {cancion_nueva.titulo} - {cancion_nueva.artista}")

    # FUNCIÓN 2: Mostrar toda la playlist en consola (Para probar)
    def mostrar_playlist(self):
        if self.cabeza is None:
            print("La playlist está vacía.")
            return
        
        actual = self.cabeza
        print("\n--- PLAYLIST ACTUAL ---")
        while actual is not None:
            # Marcamos con una flecha cuál está sonando
            marcador = "▶" if actual == self.actual else " "
            print(f"{marcador} {actual.cancion.titulo} - {actual.cancion.artista}")
            actual = actual.siguiente
        print("-----------------------\n")
# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    # Creamos nuestra playlist vacía
    mi_playlist = ListaEnlazadaDoble()

    # Simulamos que los clientes agregan canciones
    c1 = Cancion(1, "Blinding Lights", "The Weeknd")
    c2 = Cancion(2, "Bohemian Rhapsody", "Queen")
    c3 = Cancion(3, "Shape of You", "Ed Sheeran")

    mi_playlist.agregar_cancion(c1)
    mi_playlist.agregar_cancion(c2)
    mi_playlist.agregar_cancion(c3)

    # Mostramos el resultado
    mi_playlist.mostrar_playlist()