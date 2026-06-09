
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
    # FUNCIÓN 3: Avanzar a la siguiente canción (Botón Siguiente)
    def avanzar_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"⏭️ Cambiando a: {self.actual.cancion.titulo}")
        else:
            print("🛑 Ya estás en la última canción de la playlist.")

    # FUNCIÓN 4: Regresar a la canción anterior (Botón Anterior)
    def retroceder_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"⏮️ Regresando a: {self.actual.cancion.titulo}")
        else:
            print("🛑 Ya estás en la primera canción de la playlist.")   
    # FUNCIÓN 5: Eliminar la canción actual (Porque ya terminó o se canceló)
    def eliminar_actual(self):
        # Caso 0: Lista vacía
        if self.actual is None:
            print("🛑 No hay ninguna canción sonando para eliminar.")
            return

        nodo_a_eliminar = self.actual
        print(f"🗑️ Eliminando de la fila: {nodo_a_eliminar.cancion.titulo}")

        # Caso 1: Es la única canción en la lista
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            self.actual = None

        # Caso 2: Es la primera canción (La cabeza)
        elif nodo_a_eliminar == self.cabeza:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            self.actual = self.cabeza  # La nueva actual es la que sigue

        # Caso 3: Es la última canción (La cola)
        elif nodo_a_eliminar == self.cola:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.actual = self.cola  # La nueva actual es la anterior

        # Caso 4: Está en medio de la lista
        else:
            nodo_anterior = nodo_a_eliminar.anterior
            nodo_siguiente = nodo_a_eliminar.siguiente

            # Puenteamos el nodo a eliminar
            nodo_anterior.siguiente = nodo_siguiente
            nodo_siguiente.anterior = nodo_anterior
            
            # Pasamos a la siguiente canción automáticamente
            self.actual = nodo_siguiente

        del nodo_a_eliminar  # Liberamos memoria         