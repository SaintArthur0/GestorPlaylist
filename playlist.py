
class Cancion:
    def __init__(self, id_cancion, titulo, artista):
        self.id = id_cancion
        self.titulo = titulo
        self.artista = artista


class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion  
        self.siguiente = None   
        self.anterior = None    


class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None  
        self.cola = None    
        self.actual = None  

   
    def agregar_cancion(self, cancion_nueva):
        nuevo_nodo = Nodo(cancion_nueva)
        
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.actual = nuevo_nodo  
        else:

            self.cola.siguiente = nuevo_nodo
           
            nuevo_nodo.anterior = self.cola
            
            self.cola = nuevo_nodo
            
        print(f"🎵 Añadida a la fila: {cancion_nueva.titulo} - {cancion_nueva.artista}")

    
    def mostrar_playlist(self):
        if self.cabeza is None:
            print("La playlist está vacía.")
            return
        
        actual = self.cabeza
        print("\n--- PLAYLIST ACTUAL ---")
        while actual is not None:
            
            marcador = "▶" if actual == self.actual else " "
            print(f"{marcador} {actual.cancion.titulo} - {actual.cancion.artista}")
            actual = actual.siguiente
        print("-----------------------\n")
    
    def avanzar_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"⏭️ Cambiando a: {self.actual.cancion.titulo}")
        else:
            print("🛑 Ya estás en la última canción de la playlist.")

    
    def retroceder_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"⏮️ Regresando a: {self.actual.cancion.titulo}")
        else:
            print("🛑 Ya estás en la primera canción de la playlist.")   
    
    def eliminar_actual(self):
        # Caso 0: Lista vacía
        if self.actual is None:
            print("🛑 No hay ninguna canción sonando para eliminar.")
            return

        nodo_a_eliminar = self.actual
        print(f"🗑️ Eliminando de la fila: {nodo_a_eliminar.cancion.titulo}")

        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            self.actual = None

        
        elif nodo_a_eliminar == self.cabeza:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            self.actual = self.cabeza  

        
        elif nodo_a_eliminar == self.cola:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.actual = self.cola  

        
        else:
            nodo_anterior = nodo_a_eliminar.anterior
            nodo_siguiente = nodo_a_eliminar.siguiente

            
            nodo_anterior.siguiente = nodo_siguiente
            nodo_siguiente.anterior = nodo_anterior
            
            
            self.actual = nodo_siguiente

        del nodo_a_eliminar         