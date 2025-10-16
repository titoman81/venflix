# Importamos las funciones que creamos en los otros archivos
from bcv import obtener_tasa_oficial_bcv
from paralelo import obtener_tasa_cambiar_saldo_ar
 
def obtener_datos_brecha():
    """
    Obtiene las tasas del BCV y del paralelo, calcula la brecha
    y devuelve los tres valores.
    Retorna:
        (tasa_bcv, tasa_paralelo, brecha) o (None, None, None) si falla.
    """
    print("\nBuscando tasa oficial del BCV...")
    tasa_bcv = obtener_tasa_oficial_bcv()
    if tasa_bcv:
        print(f"✅ Tasa oficial BCV obtenida: {tasa_bcv:.4f}")
 
    print("\nBuscando tasa de Cambiar Saldo.ar...")
    tasa_paralelo = obtener_tasa_cambiar_saldo_ar()
    if tasa_paralelo:
        print(f"✅ Tasa Cambiar Saldo.ar obtenida: {tasa_paralelo:.2f}")
 
    if tasa_bcv and tasa_paralelo:
        brecha = ((tasa_paralelo - tasa_bcv) / tasa_bcv) * 100
        return tasa_bcv, tasa_paralelo, brecha
    
    return None, None, None
 
def mostrar_resumen_brecha():
    """
    Función principal que obtiene los datos y muestra el resumen.
    """
    print("📊 Iniciando cálculo de brecha cambiaria...")
    tasa_bcv, tasa_paralelo, brecha = obtener_datos_brecha()
 
    print("\n" + "="*35)
    if brecha is not None:
        print("📈 RESUMEN DE LA BRECHA CAMBIARIA 📈")
        print(f"   Tasa Oficial (BCV): {tasa_bcv:10.4f} Bs.")
        print(f"   Tasa Paralela:      {tasa_paralelo:10.2f} Bs.")
        print(f"   Brecha Porcentual:  {brecha:9.2f}%")
    else:
        print("❌ No se pudieron obtener ambas tasas. No es posible calcular la brecha.")
    print("="*35)
 
if __name__ == "__main__":
    # Al ejecutar este archivo directamente, solo mostramos el resumen.
    mostrar_resumen_brecha()