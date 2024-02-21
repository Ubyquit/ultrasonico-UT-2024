import mysql.connector
import serial
import time

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'sm52_arduino'
}

# Configuración del puerto serial con Arduino
arduino_port = '/dev/cu.usbmodem1444301'  # Ajusta el puerto del Arduino
arduino_baudrate = 9600
arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

def obtener_estado_led():
    try:
        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Consultar el estado actual del LED
        cursor.execute("SELECT led_status FROM estado_led WHERE id_estado_led = 1")
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            return None
    except mysql.connector.Error as e:
        print(f"Error al consultar el estado del LED: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def enviar_instruccion(instruccion):
    arduino.write(instruccion.encode())

if __name__ == "__main__":
    while True:
        try:
            # Leer el estado actual del LED desde la base de datos
            led_status = obtener_estado_led()

            if led_status is not None:
                # Enviar la instrucción al Arduino según el estado del LED
                instruccion = '1' if led_status == 1 else '0'
                enviar_instruccion(instruccion)
                print(f"Estado del LED enviado al Arduino: {'Encendido' if led_status == 1 else 'Apagado'}")

            # Esperar un tiempo antes de volver a verificar el estado del LED en la base de datos
            time.sleep(1)
        except KeyboardInterrupt:
            print("Programa terminado por el usuario")
            arduino.close()  # Asegúrate de cerrar la conexión serial
            break
