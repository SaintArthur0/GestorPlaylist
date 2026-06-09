from flask import Flask, render_template, request, redirect, url_for
from playlist import ListaEnlazadaDoble, Cancion
import random

app = Flask(__name__)

# Creamos la playlist global en memoria
playlist_negocio = ListaEnlazadaDoble()

# Canciones iniciales de prueba
playlist_negocio.agregar_cancion(Cancion(1, "Blinding Lights", "The Weeknd"))
playlist_negocio.agregar_cancion(Cancion(2, "Bohemian Rhapsody", "Queen"))
playlist_negocio.agregar_cancion(Cancion(3, "Shape of You", "Ed Sheeran"))

@app.route('/')
def index():
    # Pasamos los nodos de nuestra Lista Doble a un formato que el HTML entienda
    canciones_array = []
    actual = playlist_negocio.cabeza
    while actual is not None:
        canciones_array.append({
            'titulo': actual.cancion.titulo,
            'artista': actual.cancion.artista,
            'es_actual': (actual == playlist_negocio.actual)
        })
        actual = actual.siguiente
        
    # Validamos si hay alguna canción sonando actualmente
    if playlist_negocio.actual:
        txt_sonando = f"{playlist_negocio.actual.cancion.titulo} - {playlist_negocio.actual.cancion.artista}"
    else:
        txt_sonando = "Ninguna (Playlist vacía)"

    # Enviamos los datos ordenados al archivo HTML de la carpeta templates
    return render_template('index.html', canciones=canciones_array, cancion_sonando=txt_sonando)

@app.route('/siguiente')
def siguiente():
    playlist_negocio.avanzar_cancion()
    return redirect(url_for('index'))

@app.route('/anterior')
def anterior():
    playlist_negocio.retroceder_cancion()
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    playlist_negocio.eliminar_actual()
    return redirect(url_for('index'))

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form.get('titulo')
    artista = request.form.get('artista')
    nuevo_id = random.randint(100, 999)
    
    # Inserción directa en la Lista Enlazada Doble
    playlist_negocio.agregar_cancion(Cancion(nuevo_id, titulo, artista))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)