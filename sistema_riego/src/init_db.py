import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("sistema_riego.db")
cursor = conn.cursor()

# Crear tabla lecturas
cursor.execute("""
CREATE TABLE lecturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    estado_sensor TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Base de datos creada correctamente.")
