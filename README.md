# Introduction
Hello everyone, this project is a fully custom built TKL keyboard. Soul purpose behind this project was to learn some new things while replacing the old rusty keyboard on my desk. So let's take a look inside the project

# Project overview
## PCB
For any electronics project, pcb is the very first thing to design, since it is the brain of the project. I used easyeda for designing my pcb. There are quite a few limitations with easyeda, but I somehow got things to work. It's a two layer pcb containing necessery things for the project. Main things would be microcontroller, switch, display, etc etc.

![PCB_IMAGE](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/PCB_image2.png)


## CAD
What I did after designing the pcb was building a case around it. The case looks simple, but there went a lot of research behind it.
![CAD_IMAGE](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/CAD_image.png)

There is a magnetic wrist rest extension to the main case. The wrist rest also has an oled screen in the center. This oled screen will be connected to the pcb via a pogo pin. I'll demonstrate the thing below.
![POGO_IMAGE](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/POGO_image.png)

The display will be hand wired to the pogo pins like below!
![POGO_CONNECTION](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/OLED_WIRING_image.png)

## Firmware
The firmware is mostly ai written, I just have instructed the ai tool what to do with each component and I got the firmware. It's still not tested and only a proof of concept though. I'll update the readme when I get an actual working firmware!
[Firmware]()

## BOM

|Name                          |Quantity|Price(BDT)|Delivery(BDT)|Total(BDT)|Total(USD)|Product link                                                                                                                               |
|------------------------------|--------|----------|-------------|----------|----------|-------------------------------------------------------------------------------------------------------------------------------------------|
|Raspberry Pi Pico             |1       |930       |             |930       |7.626     |https://store.roboticsbd.com/raspberry-pi/1599-raspberry-pi-pico-robotics-bangladesh.html                                                  |
|74AHCT125                     |1       |40        |             |40        |0.328     |https://store.roboticsbd.com/digital-ics/3383-74hct125-4-ch-buffer-with-3-state-outputs-robotics-bangladesh.html                           |
|DISPLAY-OLED-128X32           |1       |300       |             |300       |2.46      |https://store.roboticsbd.com/display/1634-091-inch-128x32-blue-oled-display-module-with-i2ciic-serial-interface-robotics-bangladesh.html   |
|1N4148 Diode                  |90      |270       |             |270       |2.214     |https://store.roboticsbd.com/components/1355-1n4148-diode-robotics-bangladesh.html                                                         |
|Pogo pin set                  |1       |220       |             |220       |1.804     |https://store.roboticsbd.com/connector/3147-4-pin-2a-dc-magnetic-pogo-pin-connector-254mm-spacing-robotics-bangladesh.html                 |
|DisPLAY-OLED-2.42”            |1       |1690      |             |1690      |13.858    |https://store.roboticsbd.com/arduino-shield/2922-242-inch-oled-screen-lcd-display-module-128x64-iic-i2c-4pin-white-robotics-bangladesh.html|
|Deliver charge for above parts|-       |          |119          |119       |0.9758    |                                                                                                                                           |
|Akko Dracula switches         |(45+45) |3300      |             |3300      |27.06     |https://vibegaming.com.bd/product/akko-dracula-switch-lubed-45-pcs/                                                                        |
|SK6812MINI-E                  |100     |880       |             |880       |7.216     |https://www.aliexpress.com/item/1005006463785578.html                                                                                      |
|Kailh hot swap sockets        |100     |818       |389          |1207      |9.8974    |https://www.aliexpress.com/item/1005009594313632.html                                                                                      |
|Shipments for 3d prints       |-       |-         |-            |2443.6    |20        |                                                                                                                                           |
|PCB                           |5       |          |             |          |34        |https://jlcpcb.com                                                                                                                                 |
|Neodemyum magnets(8mm*3mm)    |4       |85        |143          |228       |1.8696    |https://www.daraz.com.bd/products/powerfull-disc-neodymium-magnets-10mm2mm-10mm15mm-8mm3mm-4pcs-i546832185-s2574219327.html?               |
|Ribbon(peripheral)            |1       |1000      |             |1000      |8.2       |https://www.aliexpress.com/item/1005008283113666.html                                                                                      |
|                              |        |          |             |          |          |                                                                                                                                           |
|                              |        |          |             |Total(USD)|137.5088  |                                                                                                                                           |

Please note that the website called roboticsbd.com does not accept card payment. They accept a mobile financial service provider called "Bkash". I don't know if it's possible to pay from the grant card through bkash or not. If not, the total costing may vary(most likely increase) provided that I have to order from aliexpress!