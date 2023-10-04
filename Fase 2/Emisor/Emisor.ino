#include <IRremote.h>

IRsend emisor_ir;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String datos = Serial.readString();
    for (int i = 0; i < datos.length(); i++) {
      emisor_ir.sendSony(datos.charAt(i), 12);
      delay(20);
    }
    Serial.println("Enviado");
  }
}