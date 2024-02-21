# pip install websockets mysql-connector-python
# Ejecutar con Python 3.7 o superior

import asyncio
import websockets
import mysql.connector
import serial

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'sm52_arduino'
}

# Configura el puerto serial según tu configuración de Arduino
arduino_serial = serial.Serial('/dev/cu.usbmodem1444301', 9600, timeout=1)

def update_led_status_in_db(status):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("UPDATE estado_led SET led_status = %s WHERE id_estado_led = 1", (status,))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error de base de datos: {e}")
    finally:
        cursor.close()
        conn.close()

def get_led_status_from_db():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT led_status FROM estado_led WHERE id_estado_led = 1")
        status = cursor.fetchone()[0]
        return status
    except mysql.connector.Error as e:
        print(f"Error de base de datos: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

async def handle_led(websocket, path):
    status = get_led_status_from_db()
    await websocket.send(str(status))  # Enviar estado actual al cliente al conectarse
    async for message in websocket:
        if message in ["1", "0"]:
            update_led_status_in_db(message)
            arduino_serial.write(message.encode())
            await websocket.send(message)  # Opcional: Confirmar el cambio al cliente

async def start_server():
    async with websockets.serve(handle_led, "localhost", 8765):
        await asyncio.Future()  # Ejecuta el servidor indefinidamente

if __name__ == "__main__":
    asyncio.run(start_server())
