import sqlite3
from datetime import datetime

# 1. Conectar (o crear si no existe) la base de datos
conn = sqlite3.connect('sistema_riego.db')
cursor = conn.cursor()

# 2. Crear tablas (solo la primera vez)
cursor.execute('''
CREATE TABLE IF NOT EXISTS lecturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    sensor TEXT NOT NULL,
    valor REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    evento TEXT NOT NULL,
    descripcion TEXT
)
''')

# 3. Insertar datos simulados en lecturas
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute('''
INSERT INTO lecturas (fecha, sensor, valor) VALUES (?, ?, ?)
''', (now, 'humedad', 47.8))
cursor.execute('''
INSERT INTO lecturas (fecha, sensor, valor) VALUES (?, ?, ?)
''', (now, 'temperatura', 23.5))

# 4. Insertar evento simulado
cursor.execute('''
INSERT INTO eventos (fecha, evento, descripcion) VALUES (?, ?, ?)
''', (now, 'riego', 'Riego activado por humedad baja'))

# 5. Guardar cambios
conn.commit()

# 6. Consultar y mostrar las lecturas
print("\n--- Lecturas registradas ---")
for row in cursor.execute('SELECT * FROM lecturas'):
    print(row)

print("\n--- Eventos registrados ---")
for row in cursor.execute('SELECT * FROM eventos'):
    print(row)

# 7. Cerrar la conexión
conn.close()
