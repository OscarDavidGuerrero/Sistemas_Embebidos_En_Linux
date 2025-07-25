import RPi.GPIO as GPIO
import time

SENSOR_PIN = 17  # Cambia por el pin que estés usando

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

print("Iniciando lectura del sensor de humedad...")
print("Presiona Ctrl+C para detener.")

try:
    while True:
        estado = GPIO.input(SENSOR_PIN)
        if estado == GPIO.HIGH:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Suelo seco - debería regar")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Suelo húmedo - no necesita riego")
        time.sleep(5)
except KeyboardInterrupt:
    print("Lectura detenida por el usuario.")
finally:
    GPIO.cleanup()
