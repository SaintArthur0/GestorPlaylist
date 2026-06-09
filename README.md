# 🎵 Gestor de Playlist para Negocios (Multiusuario)

Este es un proyecto escolar desarrollado para la materia de **Estructura de Datos**. Consiste en un sistema web que permite a un establecimiento controlar su ambiente musical, mientras que los clientes pueden conectarse desde sus propios dispositivos móviles para sugerir canciones en tiempo real a la fila de reproducción.

## 🚀 Ver en Vivo (Sin descargas)
El proyecto ha sido desplegado en la nube para facilitar su revisión sin necesidad de descargar archivos ni configurar entornos locales. Puedes interactuar con la aplicación en el siguiente enlace:

👉 ** https://gestorplaylist-arturo.onrender.com **

---

## 🧠 Estructura de Datos Utilizada
El motor principal del sistema está construido sobre una **Lista Enlazada Doble** programada desde cero en Python (`playlist.py`). 

Se eligió esta estructura debido a las siguientes ventajas técnicas aplicadas al negocio:
1. **Inserciones y eliminaciones eficientes ($O(1)$):** Ideal para un flujo dinámico de música, donde los clientes agregan temas constantemente al final de la estructura (`agregar_cancion`) y el administrador remueve canciones de la fila conforme terminan de sonar o se cancelan (`eliminar_actual`).
2. **Recorrido bidireccional:** A través de punteros hacia adelante (`siguiente`) y hacia atrás (`anterior`), el sistema permite navegar fluidamente por el catálogo musical en tiempo real, optimizando el uso de memoria RAM en comparación con un arreglo estático.

---

## 🛠️ Tecnologías Utilizadas
* **Python**: Lógica pura de la Estructura de Datos (Nodos y Punteros).
* **Flask**: Microframework para convertir las funciones de Python en un servidor web local y multiusuario.
* **HTML5 y CSS3**: Interfaz gráfica responsiva (estilo oscuro responsivo para móviles y ordenadores).
* **Render**: Despliegue en la nube para ejecución en producción.