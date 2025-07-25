import RPi.GPIO as GPIO
import time

class SensorManager:
    def __init__(self, pin=17):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
    
    def leer_estado(self):
        estado = GPIO.input(self.pin)
        if estado == GPIO.HIGH:
            return "seco"
        else:
            return "húmedo"
    
    def limpiar(self):
        GPIO.cleanup()

if __name__ == "__main__":
    sensor = SensorManager(pin=17)
    try:
        while True:
            estado = sensor.leer_estado()
            if estado == "seco":
                mensaje = "Suelo seco - debería regar"
            else:
                mensaje = "Suelo húmedo - no necesita riego"
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Lectura detenida por el usuario.")
    finally:
        sensor.limpiar()
