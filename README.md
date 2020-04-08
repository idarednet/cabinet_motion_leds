# Under-the-Cabinet Motion Activated LEDs Project
Harware Used:
- Adafruit Trinket M0 - https://www.adafruit.com/product/3500
- Grove PIR Motion Sensor - http://wiki.seeedstudio.com/Grove-PIR_Motion_Sensor/
- External 5VDC Power Supply

# Connections:
 - Trinket M0
     - Gnd   <-> Negative side of 5VDC power source
     - Bat   <-> Positive side of 5VDC power source
     - PIN 4 <-> DIN on 5050 LED Strip
     - PIN 3 <-> D1 on PIR
 - 5050 LED Strip
     - GND   <-> Negative side of 5VDC power source
     - DIN   <-> PIN 4 Trinket M0
     - +5V   <-> Positive side of 5VDC power source
 - PIR
     - GND   <-> Negative side of 5VDC power source
     - VCC   <-> Postivie side of 5VDC power source
     - D1    <-> PIN 3 Trinket M0
 
