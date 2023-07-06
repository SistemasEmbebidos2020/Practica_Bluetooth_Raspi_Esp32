#include <Arduino.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;
bool emparejado = false;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("esp32_1"); // Nombre del dispositivo Bluetooth del master
  SerialBT.connect("raspberrypi");    // Nombre del dispositivo Bluetooth del esclavo
 
  Serial.println("ESP32 esclavo iniciado");
}

void loop()
{
  while (!emparejado)
  {
    if (!SerialBT.connected())
    {
      Serial.println("Esperando emparejamiento...");
      delay(1000);
    }
    else
    {
      Serial.println("Emparejado con el esclavo");
      emparejado = true;
    }
  }

  if (SerialBT.available())
  {
    Serial.print("Recibido: ");
    Serial.println(SerialBT.readString());
  }

  if (Serial.available())
  {
    Serial.print("Enviado: ");
    SerialBT.println(Serial.readString());
  }
}
