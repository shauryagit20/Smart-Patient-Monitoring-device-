#include <SoftwareSerial.h>

String inputByte="z";
SoftwareSerial bt(10,11);

void setup(){
Serial.begin(9600);
pinMode(13,OUTPUT);
}



void loop() {

while(Serial.available() > 0){
  String inputByte= Serial.readString();
  Serial.println(inputByte);
  
  
}
}
