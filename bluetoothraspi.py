import bluetooth
from time import sleep
import socket

# Obtener el nombre del host de la Raspberry Pi
raspberry_pi_name = socket.gethostname()
print("Nombre de la Raspberry Pi:", raspberry_pi_name)

# Nombre del dispositivo ESP32
esp32_name = 'esp32_1'  # Reemplaza con el nombre real definido en el codigo de la esp32

# Encuentra la dirección MAC del ESP32
devices = bluetooth.discover_devices()
esp32_mac_address = None

for addr in devices:
    print(addr)
    print('buscando dispositivo...')
    if bluetooth.lookup_name(addr) == esp32_name:
        esp32_mac_address = addr
        print('dispositivo encontrado...')
        print(bluetooth.lookup_name(addr))
        break
    sleep(1)

if esp32_mac_address is None:
    print('No se encontró el dispositivo ESP32.')
    exit()

# Crea un socket RFCOMM para la comunicación Bluetooth
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Establece la conexión con el ESP32
socket.connect((esp32_mac_address, 1))  # El segundo argumento es el canal (puerto) Bluetooth
try:
 data = 'Hello ESP32!'
 socket.send(data)
 while(1):
  # Envía datos al ESP32
  text = input("ingrese texto a enviar.. " )
  socket.send(text)
  # Recibe datos del  ESP32
  received_data = socket.recv(1024)
  print('Recibido:', received_data.decode().strip())
except:
 # Cierra la conexión
 socket.close()
