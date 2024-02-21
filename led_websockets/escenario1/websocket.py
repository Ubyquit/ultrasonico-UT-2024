# pip install websockets pyserial
# Ejecutar con Python 3.7 o superior

import asyncio
import websockets
import serial
import time

# Configura el puerto serial según tu configuración de Arduino
arduino_serial = serial.Serial('/dev/cu.usbmodem1444301', 9600, timeout=1)

def get_current_led_state():
    arduino_serial.write(b'get_state\n')  # Solicita el estado actual
    time.sleep(0.1)  # Da tiempo al Arduino para responder
    if arduino_serial.inWaiting() > 0:
        state = arduino_serial.readline().decode().strip()
        return state
    return "0"  # Devuelve un estado predeterminado si no hay respuesta

async def handle_led(websocket, path):
    # Envía el estado actual del LED al cliente justo después de establecer la conexión
    current_state = get_current_led_state()
    await websocket.send(current_state)
    
    async for message in websocket:
        print(f"Recibido del cliente: {message}")
        if message in ["1", "0"]:
            print(f"Enviando a Arduino: {message}")
            arduino_serial.write(message.encode())

async def start_server():
    async with websockets.serve(handle_led, "localhost", 8765):
        await asyncio.Future()  # Ejecuta el servidor indefinidamente

if __name__ == "__main__":
    print("Iniciando servidor WebSocket...")
    asyncio.run(start_server())
