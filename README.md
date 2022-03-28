# SN2_Projet

---

### Code QT

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```

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

