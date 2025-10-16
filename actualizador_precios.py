from calculadora_brecha import obtener_datos_brecha

# --- Catálogo de Precios Base ---
# 20 secciones, cada una con al menos 5 productos.
# Cada producto ahora tiene un diccionario con 'price' y 'desc'.
CATALOGO_PRECIOS = {
    "Electrónica": {
        "Laptop Gamer": {"price": 1250.00, "desc": "Potente laptop con gráficos dedicados para una experiencia de juego inmersiva."},
        "Monitor 4K": {"price": 450.50, "desc": "Monitor de 27 pulgadas con resolución Ultra HD para una claridad de imagen superior."},
        "Teclado Mecánico": {"price": 95.75, "desc": "Teclado retroiluminado con switches mecánicos para una respuesta táctil precisa."},
        "Mouse Inalámbrico": {"price": 40.00, "desc": "Mouse ergonómico con conexión inalámbrica de baja latencia y sensor óptico de alta precisión."},
        "Webcam HD": {"price": 65.20, "desc": "Cámara web Full HD 1080p con micrófono incorporado, ideal para streaming y videollamadas."}
    },
    "Hogar y Cocina": {
        "Cafetera Express": {"price": 89.99, "desc": "Prepara cafés de calidad profesional en casa con esta cafetera de 15 bares de presión."},
        "Licuadora de Alta Potencia": {"price": 120.00, "desc": "Motor de 1200W capaz de triturar hielo y frutas congeladas para smoothies perfectos."},
        "Juego de Sartenes": {"price": 75.50, "desc": "Set de 3 sartenes antiadherentes de titanio, duraderos y fáciles de limpiar."},
        "Robot Aspirador": {"price": 250.00, "desc": "Aspiradora inteligente con mapeo láser que limpia tu hogar de forma autónoma."},
        "Freidora de Aire": {"price": 110.40, "desc": "Cocina tus alimentos favoritos con hasta un 85% menos de grasa. Capacidad de 5.5L."}
    },
    # ... (Puedes seguir añadiendo descripciones para los demás productos)
    "Libros": {
        "Cien Años de Soledad": {"price": 22.50, "desc": "La obra maestra de Gabriel García Márquez, un pilar del realismo mágico."},
        "El Señor de los Anillos": {"price": 35.00, "desc": "La trilogía completa de J.R.R. Tolkien en una edición de lujo."},
        "Dune": {"price": 25.75, "desc": "La épica novela de ciencia ficción de Frank Herbert que inspiró a generaciones."},
        "Ficciones": {"price": 18.90, "desc": "Una colección de cuentos de Jorge Luis Borges que desafían la realidad."},
        "1984": {"price": 20.00, "desc": "La icónica novela distópica de George Orwell sobre la vigilancia y el totalitarismo."}
    }
    # ... y así sucesivamente para las otras 17 categorías.
}

# La lógica de visualización y actualización se ha movido a app.py.
# Este archivo ahora solo sirve para definir el catálogo de precios base.
# Podríamos añadir funciones de cálculo aquí si la lógica se vuelve más compleja.