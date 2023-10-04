#include <IRremote.h>

IRrecv receptor_ir(5);
decode_results ir;

void setup() {
  Serial.begin(9600);
  receptor_ir.enableIRIn();
}

void loop() {
  if (receptor_ir.decode(&ir)) {
    Serial.print(char(ir.value));
    receptor_ir.resume();
  }
}