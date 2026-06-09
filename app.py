from flask import Flask, render_template, request, redirect, url_for, jsonify
from playlist import ListaEnlazadaDoble, Cancion

app = Flask(__name__)

# Creamos la playlist global que compartirá todo el negocio
playlist_negocio = ListaEnlazadaDoble()

# Agregamos unas canciones por defecto para que no inicie vacío
playlist_negocio.agregar_cancion(Cancion(1, "Blinding Lights", "The Weeknd"))
playlist_negocio.agregar_cancion(Cancion(2, "Bohemian Rhapsody", "Queen"))
playlist_negocio.agregar_cancion(Cancion(3, "Shape of You", "Ed Sheeran"))

# 1. RUTA PRINCIPAL: Aquí entra el administrador (la pantalla del negocio)
@app.route('/')
def index():
    # Convertimos la lista enlazada a un arreglo de Python temporal 
    # SOLO para poder pasárselo fácil a la vista HTML
    canciones_array = []
    actual = playlist_negocio.cabeza
    while actual is not None:
        canciones_array.append({
            'id': actual.cancion.id,
            'titulo': actual.cancion.titulo,
            'artista': actual.cancion.artista,
            'es_actual': (actual == playlist_negocio.actual)
        })
        actual = actual.siguiente
        
    cancion_sonando = playlist_negocio.actual.cancion if playlist_negocio.actual else None

    return f"""
    <h1>🎵 Panel del Negocio (Reproductor)</h1>
    <h2>Reproduciendo ahora: {cancion_sonando.titulo if cancion_sonando else 'Ninguna'} - {cancion_sonando.artista if cancion_sonando else ''}</h2>
    
    <a href="/siguiente"><button style="font-size:20px;">⏭️ Siguiente</button></a>
    <a href="/anterior"><button style="font-size:20px;">⏮️ Anterior</button></a>
    <a href="/eliminar"><button style="font-size:20px; background-color:red; color:white;">🗑️ Terminar/Eliminar</button></a>

    <h3>Fila de reproducción actual:</h3>
    <ul>
        {"".join([f"<li>{'<b>▶ ' if c['es_actual'] else ''}{c['titulo']} - {c['artista']}</b></li>" for c in canciones_array])}
    </ul>
    
    <hr>
    <h3>🔒 Agregar canción (Simulación Cliente/Admin)</h3>
    <form action="/agregar" method="POST">
        <input type="text" name="titulo" placeholder="Título" required>
        <input type="text" name="artista" placeholder="Artista" required>
        <button type="submit">Agregar a la fila</button>
    </form>
    """

@app.route('/api/canciones')
def api_canciones():
    canciones_array = []
    actual = playlist_negocio.cabeza
    while actual is not None:
        canciones_array.append({
            'id': actual.cancion.id,
            'titulo': actual.cancion.titulo,
            'artista': actual.cancion.artista,
            'es_actual': (actual == playlist_negocio.actual)
        })
        actual = actual.siguiente
    return jsonify(canciones_array)

# 2. RUTAS DE ACCIÓN: Mueven los punteros de la lista doble y redirigen a la pantalla principal
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
    import random
    nuevo_id = random.randint(100, 999) # ID rápido para la prueba
    
    # Usamos el método de tu estructura de datos
    playlist_negocio.agregar_cancion(Cancion(nuevo_id, titulo, artista))
    return redirect(url_for('index'))

if __name__ == '__main__':
    # host='0.0.0.0' permite que otros celulares en la misma red Wi-Fi se conecten
    app.run(debug=True, host='0.0.0.0', port=5000)