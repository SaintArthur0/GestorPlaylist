from flask import Flask, render_template, request, redirect, url_for
from playlist import ListaEnlazadaDoble, Cancion
import random

app = Flask(__name__)


playlist_negocio = ListaEnlazadaDoble()


playlist_negocio.agregar_cancion(Cancion(1, "Blinding Lights", "The Weeknd"))
playlist_negocio.agregar_cancion(Cancion(2, "Bohemian Rhapsody", "Queen"))
playlist_negocio.agregar_cancion(Cancion(3, "Shape of You", "Ed Sheeran"))

@app.route('/')

@app.route('/admin')
def admin():
    canciones_array = []
    actual = playlist_negocio.cabeza
    while actual is not None:
        canciones_array.append({
            'titulo': actual.cancion.titulo, 
            'artista': actual.cancion.artista,
            'es_actual': (actual == playlist_negocio.actual)
        })
        actual = actual.siguiente
        
    
    if playlist_negocio.actual and playlist_negocio.actual.cancion:
        txt_sonando = f"{playlist_negocio.actual.cancion.titulo} - {playlist_negocio.actual.cancion.artista}"
    else:
        txt_sonando = "Ninguna (Playlist vacía)"
    
    return render_template('index.html', canciones=canciones_array, cancion_sonando=txt_sonando, es_admin=True)



@app.route('/')
@app.route('/cliente')
def cliente():
    canciones_array = []
    actual = playlist_negocio.cabeza
    while actual is not None:
        canciones_array.append({
            'titulo': actual.cancion.titulo, 
            'artista': actual.cancion.artista,
            'es_actual': (actual == playlist_negocio.actual)
        })
        actual = actual.siguiente
        
    
    if playlist_negocio.actual and playlist_negocio.actual.cancion:
        txt_sonando = f"{playlist_negocio.actual.cancion.titulo} - {playlist_negocio.actual.cancion.artista}"
    else:
        txt_sonando = "Ninguna (Playlist vacía)"
    
    return render_template('index.html', canciones=canciones_array, cancion_sonando=txt_sonando, es_admin=False)

@app.route('/siguiente')
def siguiente():
    playlist_negocio.avanzar_cancion()
    return redirect(url_for('admin'))

@app.route('/anterior')
def anterior():
    playlist_negocio.retroceder_cancion()
    return redirect(url_for('admin'))

@app.route('/eliminar')
def eliminar():
    playlist_negocio.eliminar_actual()
    return redirect(url_for('admin'))

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form.get('titulo')
    artista = request.form.get('artista')
    nuevo_id = random.randint(100, 999)
    
    
    playlist_negocio.agregar_cancion(Cancion(nuevo_id, titulo, artista))
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)