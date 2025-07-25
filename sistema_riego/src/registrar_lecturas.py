import time
from sensor_manager import SensorManager
from db_manager import DBManager

sensor = SensorManager(pin=17)
db = DBManager("sistema_riego.db")

print("Iniciando registro de lecturas de humedad cada 5 segundos.")
print("Presiona Ctrl+C para detener.")

try:
    while True:
        estado = sensor.leer_estado()
        db.insertar_lectura(estado)

        if estado == "seco":
            print("🌱 Estado: seco → 💧 DEBE regar.")
        else:
            print("🌿 Estado: húmedo → ✅ No necesita riego.")

        time.sleep(5)

except KeyboardInterrupt:
    print("Registro detenido por el usuario.")
finally:
    sensor.limpiar()

