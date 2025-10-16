import os
from flask import Flask, render_template, flash
from calculadora_brecha import obtener_datos_brecha
from actualizador_precios import CATALOGO_PRECIOS

# Inicializamos la aplicación Flask
app = Flask(__name__)

# --- CONFIGURACIÓN Y SECRETOS ---
# Leemos las variables de entorno. Usamos un valor por defecto para que la app no falle si no están definidas.
# En producción (Render), ESTOS VALORES SERÁN SOBREESCRITOS por los que configures en el dashboard.
app.secret_key = os.environ.get('SECRET_KEY', 'una-clave-secreta-para-desarrollo-local')

# --- CONFIGURACIÓN DEL NEGOCIO ---
# Coloca aquí el número de WhatsApp a donde se enviarán los comprobantes.
# Formato internacional sin '+' o '00'. Ejemplo para Venezuela: 584121234567
WHATSAPP_NUMBER = os.environ.get('WHATSAPP_NUMBER', '1231231231') # <-- VALOR POR DEFECTO

# Datos para las formas de pago
PAYMENT_INFO = {
    "binance_pay_id": "", # Ya no se muestra directamente
    "pago_movil_ci": "",         # Ya no se muestra directamente
    "pago_movil_telefono": "", # Ya no se muestra directamente
    "pago_movil_banco": "" # Ya no se muestra directamente
}

@app.route('/')
def index():
    """
    Ruta principal que muestra el catálogo de precios actualizado.
    """
    print("🔄 Petición recibida. Obteniendo datos de tasas...")
    
    # 1. Obtenemos los datos de la brecha.
    tasa_bcv, tasa_paralelo, brecha_porcentual = obtener_datos_brecha()

    # 2. Preparamos los datos para la plantilla
    productos_actualizados = []
    if brecha_porcentual is not None:
        product_id_counter = 0
        # Si tenemos brecha, calculamos los nuevos precios
        for seccion, productos in CATALOGO_PRECIOS.items():
            for nombre_producto, detalles in productos.items():
                precio_base = detalles.get("price", 0)
                descripcion = detalles.get("desc", "Sin descripción.")
                precio_nuevo = precio_base * (1 + brecha_porcentual / 100)
                # Calculamos el precio final en Bolívares
                precio_en_bs = precio_nuevo * tasa_bcv
                productos_actualizados.append({
                    "id": product_id_counter,
                    "seccion": seccion,
                    "nombre": nombre_producto,
                    "descripcion": descripcion,
                    "precio_base": precio_base,
                    "precio_nuevo": precio_nuevo,
                    "precio_bs": precio_en_bs
                })
                product_id_counter += 1
    else:
        # Si no hay brecha, mostramos un mensaje de error en la página
        flash("❌ No se pudo obtener la brecha cambiaria. No se pueden mostrar los precios actualizados.", "error")

    # 3. Renderizamos la plantilla HTML, pasándole los datos
    return render_template('index.html', 
                           productos=productos_actualizados,
                           tasa_bcv=tasa_bcv,
                           tasa_paralelo=tasa_paralelo,
                           brecha=brecha_porcentual,
                           whatsapp_number=WHATSAPP_NUMBER,
                           payment_info=PAYMENT_INFO)

if __name__ == '__main__':
    # Ejecutamos la aplicación en modo de depuración
    app.run(debug=True)