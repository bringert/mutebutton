## Adafruit Neokey Featherwing notes

https://www.adafruit.com/product/4979

* Switch A - Connects to the Feather pin to the left of SCL, on most Feathers this is pin D5
* Switch B - Connects to the Feather pin two pins to the left of SCL, on most Feathers this is pin D6
* NeoPixel Input - Connects to the Feather pin three pins to the left of SCL, on most Feathers this is pin D9

Looking at https://cdn-learn.adafruit.com/assets/assets/000/046/240/original/microcomputers_Adafruit_Feather_32u4_Basic_Proto_v2.3-1.png
Counting from bottom right, with key side up, text properly oriented:
* 3rd pin is NeoKey button A
* 4th pin is NeoKey button B
* 5th pin is NeoPixel Input
* GND seems to be bottom left pin, and 4th pin from top left
* Power pins:
  * 2nd from top left is 3.3V. Probably the one to use.
  * 3rd from top right is VBUS, I guess USB 5V.

* What does the RST switch do? It must connect GND to top right 1st pin RESET.
