from calculadora_brecha import obtener_datos_brecha

# --- Catálogo de Precios Base ---
# 20 secciones, cada una con al menos 5 productos.
# Cada producto ahora tiene un diccionario con 'price' y 'desc'.
CATALOGO_PRECIOS = {
    "Netflix Genérico (continuas o CON pausas de hogar)": {
        "Netflix 1 pantalla por 1 mes CON pausas": {"price": 4, "desc": "Los bloqueos ocurren cada 2 semanas o 14 dias. debes contactarme para hacer el desbloqueo"},
        "Netflix 1 pantalla por 1 mes continua": {"price": 5, "desc": "Es una pantalla continua durante todo el mes, sin bloqueos."},
        "Netflix 4 pantallas por 1 mes": {"price": 14, "desc": "Cuenta completa de netflix, solo se puede ver en un solo hogar o una sola dirección IP."},
        "Netflix 1 pantalla por 3 meses CON pausas": {"price": 10, "desc": "Los bloqueos ocurren cada 2 semanas o 14 dias. debes contactarme para hacer el desbloqueo"},
        "Netflix 1 pantalla por 3 meses continua": {"price": 12, "desc": "Es una pantalla continua durante todo el trimestre, sin bloqueos."},
        "Netflix 1 pantalla por 6 meses CON pausas": {"price": 18, "desc": "Los bloqueos ocurren cada 2 semanas o 14 dias. debes contactarme para hacer el desbloqueo"},
        "Netflix 1 pantalla por 6 meses continua": {"price": 20, "desc": "Es una pantalla continua durante 6 meses, sin bloqueos."},
        "Netflix 4 pantallas por 6 meses": {"price": 60, "desc": "Cuenta completa de netflix, solo se puede ver en un solo hogar o una sola dirección IP."},
        "Netflix 1 pantalla por 12 meses CON pausas": {"price": 30, "desc": "Los bloqueos ocurren cada 2 semanas o 14 dias. debes contactarme para hacer el desbloqueo"},
        "Netflix 1 pantalla por 12 meses continua": {"price": 35, "desc": "Es una pantalla continua durante todo el año, sin bloqueos."},
        "Netflix 4 pantallas por 12 meses": {"price": 120, "desc": "Cuenta completa de netflix, solo se puede ver en un solo hogar o una sola dirección IP."}
    },
    "Spotify premium Genérico (puede que tengas una u otra caida)": {
        "Spotify genérico 3 meses": {"price": 8.5, "desc": "El correo y clave lo entregamos nosotros, no se puede editar correo, clave, foto de perfil o nombre de usuario."},
        "Spotify genérico 6 meses": {"price": 11, "desc": "El correo y clave lo entregamos nosotros, no se puede editar correo, clave, foto de perfil o nombre de usuario."},
        "Spotify genérico 12 meses": {"price": 17, "desc": "El correo y clave lo entregamos nosotros, no se puede editar correo, clave, foto de perfil o nombre de usuario."},
    },
    # ... (Puedes seguir añadiendo descripciones para los demás productos)
    "Spotify premium correo personal": {
        "Spotify correo personal 1 mes": {"price": 6.5, "desc": "Cuenta de spotify con correo y clave personal, SIN caídas, completamente personalizable."},
        "Spotify correo personal 3 meses": {"price": 17.5, "desc": "Cuenta de spotify con correo y clave personal, SIN caídas, completamente personalizable."},
        "Spotify correo personal 6 meses": {"price": 30, "desc": "Cuenta de spotify con correo y clave personal, SIN caídas, completamente personalizable."},
    },
    "Amazon Prime Video": {
        "Amazon prime video 1 pantalla 1 mes": {"price": 2.5, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de amazon personales de 1 sola pantalla."},
        "Amazon prime video 3 pantallas 1 mes": {"price": 5, "desc":  "Cuenta completa de amazon prime video, todos los perfiles son suyos"},
        "Amazon prime video 1 pantalla 3 meses": {"price": 5, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de amazon personales de 1 sola pantalla"},
        "Amazon prime video 3 pantallas 3 meses": {"price": 10, "desc":  "Cuenta completa de amazon prime video, todos los perfiles son suyos"},
        "Amazon prime video 1 pantalla 6 meses": {"price": 9, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de amazon personales de 1 sola pantalla"},
        "Amazon prime video 3 pantallas 6 meses": {"price": 18, "desc":  "Cuenta completa de amazon prime video, todos los perfiles son suyos"},
        "Amazon prime video 1 pantalla 12 meses": {"price": 18, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de amazon personales de 1 sola pantalla"},
        "Amazon prime video 3 pantallas 12 meses": {"price": 35, "desc":  "Cuenta completa de amazon prime video, todos los perfiles son suyos"},
    },
    "HboMAX": {
        "HboMAX 1 pantalla 1 mes": {"price": 2.5, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de HboMAX personales de 1 sola pantalla."},
        "HboMAX 3 pantallas 1 mes": {"price": 6, "desc":  "Cuenta completa de HboMAX, todos los perfiles son suyos"},
        "HboMAX 1 pantalla 3 meses": {"price": 6, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de HboMAX personales de 1 sola pantalla"},
        "HboMAX 3 pantallas 3 meses": {"price": 11, "desc":  "Cuenta completa de HboMAX, todos los perfiles son suyos"},
        "HboMAX 1 pantalla 6 meses": {"price": 11, "desc": "Al ser una pantalla es una cuenta compartidaHboMAX, no existen cuentas de HboMAX personales de 1 sola pantalla"},
        "Hbomax 3 pantallas 6 meses": {"price": 20, "desc":  "Cuenta completa de HboMAX, todos los perfiles son suyos"},
        "HboMAX 1 pantalla 12 meses": {"price": 20, "desc": "Al ser una pantalla es una cuenta compartida, no existen cuentas de HboMAX personales de 1 sola pantalla"},
        "HboMAX 3 pantallas 12 meses": {"price": 35, "desc":  "Cuenta completa de amazon prime video, todos los perfiles son suyos"},
    },
    "Canva Edu (correo personal)": {
        "1 mes": {"price": 4.1, "desc": "Canva con correo personal y todas sus funciones premium"},
        "3 meses": {"price": 8.2, "desc": "Canva con correo personal y todas sus funciones premium"},
    },
    "Disney+ con Star y los 7 ESPN": {
        "1 pantalla - 1 mes": {"price": 4, "desc": "1 pantalla de disney compartido, no existen cuentas personales de disney de 1 sola pantalla."},
        "4 pantallas - 1 mes": {"price": 10, "desc": "Cuenta completa de disney, todos los perfiles son suyos."},
        "1 pantalla - 3 mes": {"price": 10, "desc": "1 pantalla de disney compartido, no existen cuentas personales de disney de 1 sola pantalla."},
        "4 pantallas - 3 meses": {"price": 20, "desc": "Cuenta completa de disney, todos los perfiles son suyos."},
        "1 pantalla - 6 meses": {"price": 20, "desc": "1 pantalla de disney compartido, no existen cuentas personales de disney de 1 sola pantalla."},
        "4 pantallas - 6 meses": {"price": 35, "desc": "Cuenta completa de disney, todos los perfiles son suyos."},
        "1 pantalla - 12 meses": {"price": 35, "desc": "1 pantalla de disney compartido, no existen cuentas personales de disney de 1 sola pantalla."},
        "4 pantallas - 12 meses": {"price": 50, "desc": "Cuenta completa de disney, todos los perfiles son suyos."},
    },
        
    "CAPCUT (Correo Genérico)": {
        "1 mes": {"price": 6.8, "desc": "Capcut con todas sus funciones premium, nosotros entregamos el correo y la clave que vas a usar."},
    },
     "Youtube Premium (Correo Genérico)": {
        "1 mes": {"price": 5, "desc": "Youtube con todas sus funciones premium, nosotros entregamos el correo y la clave que vas a usar."},
        "3 mes": {"price": 15, "desc": "Youtube con todas sus funciones premium, nosotros entregamos el correo y la clave que vas a usar."},
    },
       "Crunchyroll (Plan Mega Fan)": {
        "1 mes": {"price": 5, "desc": "El plan Mega Fan es el plan más popular de Crunchyroll, que admite descargas y se puede ver hasta en dos dispositivos a la vez, nosotros entregamos el correo y la clave que vas a usar."},
        "3 mes": {"price": 12, "desc": "El plan Mega Fan es el plan más popular de Crunchyroll, que admite descargas y se puede ver hasta en dos dispositivos a la vez, nosotros entregamos el correo y la clave que vas a usar."},
        "6 meses": {"price": 20, "desc": "El plan Mega Fan es el plan más popular de Crunchyroll, que admite descargas y se puede ver hasta en dos dispositivos a la vez, nosotros entregamos el correo y la clave que vas a usar."},
        "12 meses": {"price": 35, "desc": "El plan Mega Fan es el plan más popular de Crunchyroll, que admite descargas y se puede ver hasta en dos dispositivos a la vez, nosotros entregamos el correo y la clave que vas a usar."},
    }
    # ... y así sucesivamente para las otras 17 categorías.
}

# La lógica de visualización y actualización se ha movido a app.py.
# Este archivo ahora solo sirve para definir el catálogo de precios base.
# Podríamos añadir funciones de cálculo aquí si la lógica se vuelve más compleja.