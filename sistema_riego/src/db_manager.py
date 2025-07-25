import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_path="../sistema_riego.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lecturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                estado_sensor TEXT NOT NULL
            )
        """)
        self.conn.commit()
    
    def insertar_lectura(self, estado_sensor):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO lecturas (timestamp, estado_sensor) VALUES (?, ?)", (timestamp, estado_sensor))
        self.conn.commit()
    
    def consultar_lecturas(self, limite=10):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM lecturas ORDER BY timestamp DESC LIMIT ?", (limite,))
        return cursor.fetchall()
    
    def cerrar(self):
        self.conn.close()

# Prueba rápida
if __name__ == "__main__":
    db = DBManager()
    db.insertar_lectura("húmedo")
    db.insertar_lectura("seco")
    print("Lecturas recientes:")
    for row in db.consultar_lecturas():
        print(row)
    db.cerrar()
