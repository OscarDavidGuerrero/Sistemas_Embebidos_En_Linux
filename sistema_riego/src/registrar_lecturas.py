import time
from sensor_manager import SensorManager
from db_manager import DBManager

if __name__ == "__main__":
    sensor = SensorManager(pin=17)  # Cambia el pin si usas otro
    db = DBManager(db_path="../sistema_riego.db")
    print("Iniciando registro de lecturas de humedad cada 5 segundos.")
    print("Presiona Ctrl+C para detener.")
    try:
        while True:
            estado = sensor.leer_estado()
            db.insertar_lectura(estado)
            print(f"Lectura registrada: {estado}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Registro detenido por el usuario.")
    finally:
        sensor.limpiar()
        db.cerrar()
