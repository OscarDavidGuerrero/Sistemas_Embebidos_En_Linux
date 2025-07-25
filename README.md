# Sistema de Riego Inteligente con Raspberry Pi

Proyecto: Monitoreo de humedad del suelo, registro en base de datos y visualización de datos usando Raspberry Pi y sensor de humedad resistivo LM393 (salida digital).

---

## Descripción general

- Lee periódicamente el sensor de humedad (cada 5 segundos).
- Registra cada lectura en una base de datos SQLite (`sistema_riego.db`).
- Permite graficar el historial de lecturas.
- El código es modular y preparado para agregar actuadores en el futuro.

---

## Estructura básica del proyecto
 ```
Sistemas_Embebidos_En_Linux/
│
├── sistema_riego/
│ ├── src/
│ │ ├── sensor_manager.py
│ │ ├── db_manager.py
│ │ ├── registrar_lecturas.py
│ │ └── graficar_historial.py
│ ├── venv/
│ └── requirements.txt
│
├── sistema_riego.db
├── README.md
└── ...
 ```
---

## Requisitos

- Raspberry Pi con Python 3
- Sensor de humedad LM393 (salida digital)
- (Opcional) Entorno virtual Python
- Paquetes Python: RPi.GPIO, matplotlib

---

## Instalación de dependencias

Si usas entorno virtual:

    cd ~/Sistemas_Embebidos_En_Linux/sistema_riego
    source venv/bin/activate
    pip install matplotlib

---

## Ejecución de scripts principales

1. **Registrar lecturas automáticamente**

        cd ~/Sistemas_Embebidos_En_Linux/sistema_riego
        python src/registrar_lecturas.py

    - El script lee el sensor cada 5 segundos y guarda la lectura en la base de datos.
    - Detén la ejecución con Ctrl+C.

2. **Consultar la base de datos **
    - Para ver las últimas lecturas, exportarlas a CSV y generar gráficos
    - Esto genera:

       - lecturas.csv con el historial reciente
       - grafico_linea.png: gráfico de línea de estado del sensor
       - grafico_barras.png: cantidad de lecturas por estado
       - grafico_por_dia.png: lecturas agrupadas por fecha

         cd ~/Sistemas_Embebidos_En_Linux/sistema_riego
	 python src/ver_lecturas.py
---

## ¿Cómo funciona el sistema?

- `sensor_manager.py`: Gestiona la lectura del sensor digital (GPIO), devuelve "húmedo" o "seco".
- `db_manager.py`: Maneja la base de datos SQLite, crea la tabla y permite insertar/consultar lecturas.
- `registrar_lecturas.py`: Integra ambos módulos, registra automáticamente las lecturas reales del sensor en la base de datos.
- `graficar_historial.py`: Lee la base de datos y genera un gráfico con el historial de lecturas.

---

## Tareas pendientes para la versión completa

- Integrar actuador físico (relé/electroválvula) y módulo de control de riego.
- Registrar eventos de riego en la base de datos.
- Desarrollar una interfaz de usuario avanzada (TUI o dashboard web).
- Escalar el sistema a múltiples sensores y zonas de riego.
- Mejorar el manejo de errores y la robustez.

---

## Autores

- Omar Andres Rodriguez Quiceno (OMANROQUI)
- Oscar David Guerrero Hernandez (OscarDavidGuerrero)

---

## Notas finales

Este proyecto muestra la integración entre hardware, adquisición de datos, almacenamiento y visualización en sistemas embebidos.  
Está preparado para ampliarse con actuadores y lógica de riego automática en futuras versiones.

---
