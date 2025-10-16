import requests
from bs4 import BeautifulSoup
import time
import os

# Nombre del archivo que usaremos como "memoria" para la última tasa
CACHE_FILE = 'ultima_tasa_paralelo.txt'
 
def obtener_tasa_cambiar_saldo_ar():
    """
    Obtiene la tasa de 'Cambiar Saldo.ar' desde KaskoGo Online.
    Si falla, intenta usar la última tasa guardada en caché.
    """
    URL = "https://kaskogo.online/app/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(URL, headers=HEADERS, timeout=20)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
 
            rate_cards = soup.find_all('div', class_='rate-card')
            if not rate_cards:
                print("❌ No se encontraron tarjetas de tasas. La estructura de la página pudo haber cambiado.")
                raise ValueError("No se encontraron 'rate-cards', posible página de mantenimiento.")
 
            for card in rate_cards:
                title_element = card.find('span', class_='text-lg font-semibold text-gray-200')
                if title_element and 'Cambiar Saldo.ar' in title_element.get_text():
                    price_element = card.find('span', class_='rate-value')
                    if price_element:
                        raw_price = price_element.get_text(strip=True)
                        clean_price_str = raw_price.replace('Bs.', '').strip().replace(',', '.')
                        tasa = float(clean_price_str)
                        # Guardamos la tasa obtenida exitosamente en nuestro archivo de caché
                        try:
                            with open(CACHE_FILE, 'w') as f:
                                f.write(str(tasa))
                            print(f"💾 Tasa guardada en caché ({CACHE_FILE}).")
                        except IOError as e:
                            print(f"⚠️ Advertencia: No se pudo guardar la tasa en el archivo caché: {e}")
                        return tasa
            print("❌ No se pudo encontrar la tarjeta con el título 'Cambiar Saldo.ar'.")
            # Si no se encontró la tarjeta, lo consideramos un error de scraping y forzamos un reintento
            raise AttributeError("No se encontró la tarjeta 'Cambiar Saldo.ar'")
 
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Intento {attempt + 1}/{MAX_RETRIES} fallido al contactar KaskoGo. Error de red: {e}")
        except (AttributeError, IndexError, ValueError) as e:
            print(f"⚠️ Intento {attempt + 1}/{MAX_RETRIES} fallido. Error procesando la página (scraping): {e}")
        
        # Si no es el último intento, esperamos antes de volver a intentar
        if attempt < MAX_RETRIES - 1:
            print(f"   ... Reintentando en 5 segundos ...")
            time.sleep(5)

    # Si salimos del bucle sin éxito, intentamos usar la caché
    print("❌ Se alcanzó el número máximo de reintentos o la página cambió. Intentando usar la última tasa guardada...")
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                cached_rate = float(f.read().strip())
                print(f"✅ Usando última tasa guardada en caché: {cached_rate}")
                return cached_rate
        except (IOError, ValueError) as e:
            print(f"❌ Error al leer o convertir la tasa del archivo caché: {e}")
    else:
        print(f"⚠️ El archivo de caché '{CACHE_FILE}' no existe. No hay tasa de respaldo.")
    
    print("❌ No hay una tasa en caché disponible. No se puede continuar.")
    return None
 
if __name__ == "__main__":
    # --- Prueba ---
    import os
    print("Buscando tasa de Cambiar Saldo.ar...")
    tasa_saldo_ar = obtener_tasa_cambiar_saldo_ar()
    if tasa_saldo_ar:
        print(f"✅ Tasa Cambiar Saldo.ar obtenida: {tasa_saldo_ar}")
    else:
        print("❌ No se pudo obtener la tasa de Cambiar Saldo.ar.")
