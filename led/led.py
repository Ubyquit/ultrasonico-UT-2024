import serial
import time

# Configuración del puerto serial con Arduino
arduino_port = '/dev/cu.usbmodem1454301'  # Ajusta el puerto del Arduino
arduino_baudrate = 9600
arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

# Función para enviar la instrucción al Arduino
def enviar_instruccion(instruccion):
    arduino.write(instruccion.encode())

# Programa principal
if __name__ == "__main__":
    while True:
        try:
            # Leer el estado actual del LED desde la base de datos

            # 1. Implementar la lógica para conectarte a tu base de datos MySQL y obtener el estado del LED

            # Supongamos que obtienes el estado del LED como 0 (apagado) o 1 (encendido) desde la base de datos
            led_status = 0  # Cambia esto según el estado real del LED

            # Enviar la instrucción al Arduino según el estado del LED obtenido de la base de datos
            instruccion = '1' if led_status == 1 else '0'
            enviar_instruccion(instruccion)

            # Esperar un tiempo antes de volver a verificar el estado del LED en la base de datos
            time.sleep(1)
        except KeyboardInterrupt:
            print("Programa terminado por el usuario")
            break
