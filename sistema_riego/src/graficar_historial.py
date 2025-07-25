import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

DB_PATH = "../sistema_riego.db"

# 1. Lee los datos desde la base de datos
def obtener_lecturas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, estado_sensor FROM lecturas ORDER BY timestamp ASC")
    datos = cursor.fetchall()
    conn.close()
    return datos

# 2. Procesa los datos para graficar
def procesar_datos(datos):
    tiempos = []
    valores = []
    for ts, estado in datos:
        tiempos.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"))
        # Graficamos 'seco' como 1 y 'húmedo' como 0
        valores.append(1 if estado == "seco" else 0)
    return tiempos, valores

# 3. Grafica los datos y guarda como imagen
def graficar(tiempos, valores):
    plt.figure(figsize=(10, 4))
    plt.step(tiempos, valores, where="post", label="Sensor")
    plt.yticks([0, 1], ["Húmedo", "Seco"])
    plt.xlabel("Tiempo")
    plt.ylabel("Estado del suelo")
    plt.title("Historial de lecturas de humedad del suelo")
    plt.legend()
    plt.tight_layout()
    plt.grid(True, axis='y', alpha=0.3)
    plt.savefig("historial_lecturas.png")
    print("¡Gráfico guardado como historial_lecturas.png!")
    # plt.show()  # No la uses si NO tienes entorno gráfico

if __name__ == "__main__":
    datos = obtener_lecturas()
    if not datos:
        print("No hay datos para graficar.")
    else:
        tiempos, valores = procesar_datos(datos)
        graficar(tiempos, valores)

