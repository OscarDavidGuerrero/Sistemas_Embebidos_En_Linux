from db_manager import DBManager
import csv
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from datetime import datetime

def exportar_a_csv(lecturas, nombre_archivo="lecturas.csv"):
    with open(nombre_archivo, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Timestamp", "Estado del Sensor"])
        writer.writerows(lecturas)
    print(f"✅ Lecturas exportadas a {nombre_archivo}")

def graficar_linea(lecturas):
    timestamps = [fila[1] for fila in lecturas]
    valores = [1 if fila[2] == "seco" else 0 for fila in lecturas]

    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, valores, marker='o', linestyle='-', label="Humedad")
    plt.xticks(rotation=45)
    plt.yticks([0, 1], labels=["húmedo", "seco"])
    plt.title("Histórico de Lecturas de Humedad (Línea)")
    plt.xlabel("Timestamp")
    plt.ylabel("Estado del Sensor")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.savefig("grafico_linea.png")
    plt.close()
    print("📈 Gráfico de línea guardado como grafico_linea.png")

def graficar_barras(lecturas):
    estados = [fila[2] for fila in lecturas]
    conteo = Counter(estados)

    plt.figure(figsize=(6, 4))
    plt.bar(conteo.keys(), conteo.values(), color=["skyblue", "salmon"])
    plt.title("Cantidad de lecturas por estado")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig("grafico_barras.png")
    plt.close()
    print("📊 Gráfico de barras guardado como grafico_barras.png")

def graficar_por_dia(lecturas):
    agrupado = defaultdict(lambda: {"seco": 0, "húmedo": 0})

    for _, timestamp, estado in lecturas:
        fecha = timestamp.split(" ")[0]
        agrupado[fecha][estado] += 1

    fechas = sorted(agrupado.keys())
    secos = [agrupado[fecha]["seco"] for fecha in fechas]
    humedos = [agrupado[fecha]["húmedo"] for fecha in fechas]

    plt.figure(figsize=(10, 5))
    plt.bar(fechas, secos, label="Seco", color="orange")
    plt.bar(fechas, humedos, bottom=secos, label="Húmedo", color="blue")
    plt.title("Lecturas agrupadas por día")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad de lecturas")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafico_por_dia.png")
    plt.close()
    print("📅 Gráfico por día guardado como grafico_por_dia.png")





def main():
    db = DBManager("sistema_riego.db")
    lecturas = db.consultar_lecturas(limite=100)

    print("Últimas lecturas registradas:")
    print("-" * 40)
    for lectura in lecturas:
        print(f"[{lectura[1]}] -> {lectura[2]}")

    exportar_a_csv(lecturas)
    graficar_linea(lecturas)
    graficar_barras(lecturas)
    graficar_por_dia(lecturas)

if __name__ == "__main__":
    main()
