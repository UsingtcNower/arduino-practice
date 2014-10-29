#include <DHT.h>

#define DHT_PIN A0
#define VCC_PIN 13

DHT dht(A0, DHT11);

void setup() {
  pinMode(VCC_PIN, OUTPUT);
  digitalWrite(VCC_PIN, HIGH);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  
  Serial.print("Humidity = ");
  Serial.print(dht.readHumidity());
  Serial.print(", Temperature = ");
  Serial.println(dht.readTemperature());
  delay(1000);
}
