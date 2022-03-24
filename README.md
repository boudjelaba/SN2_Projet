# SN2_Projet

---

### Code Arduino

```cpp
void setup() {
  Serial.begin(9600);
  Serial.println("Initialisation");
  
  analogReference(DEFAULT);
  pinMode(7, OUTPUT);
}
 
void loop() {
  float tensionVide;
  float tensionCharge;
 
  digitalWrite(7, LOW);
  delay(500);
  tensionVide = analogRead(A0)*5.0/1023;
 
  digitalWrite(7, HIGH);
  delay(500);
  tensionCharge = analogRead(A0)*5.0/1023;
 
  Serial.print("Tension à vide = ");
  Serial.print(tensionVide);
  Serial.println("V");
  Serial.print("Tension en charge = ");
  Serial.print(tensionCharge);
  Serial.println("V");
  if (tensionCharge > 1.2) {
    Serial.println("Batterie bonne");
  } else if (tensionCharge > 1.0) {
    Serial.println("Batterie faible");
  } else {
    Serial.println("Batterie à remplacer");
  }
}
```


## ECG

https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4

https://tutorials-raspberrypi.com/build-raspberry-pi-gps-location-navigation-device/

https://www.instructables.com/Interfacing-GPS-Module-With-Raspberry-Pi/

---

## Email

https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails

---

## GPS

https://www.electronicwings.com/raspberry-pi/gps-module-interfacing-with-raspberry-pi

