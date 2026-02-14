# Introduction
Hello everyone, this project is a fully custom built TKL keyboard. Soul purpose behind this project was to learn some new things while replacing the old rusty keyboard on my desk. So let's take a look inside the project

# Project overview
## PCB
For any electronics project, pcb is the very first thing to design, since it is the brain of the project. I used easyeda for designing my pcb. There are quite a few limitations with easyeda, but I somehow got things to work. It's a two layer pcb containing necessery things for the project. Main things would be microcontroller, switch, display, etc etc.

[PCB_IMAGE](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/PCB_image.png)


## CAD
What I did after designing the pcb was building a case around it. The case looks simple, but there went a lot of research behind it.
![CAD_IMAGE](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/CAD_image.png)

There is a magnetic wrist rest extension to the main case. The wrist rest also has an oled screen in the center. This oled screen will be connected to the pcb via a pogo pin. I'll demonstrate the thing below.
![POGO_IMAGE](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/POGO_image.png)

The display will be hand wired to the pogo pins like below!
![POGO_CONNECTION](https://github.com/Nishan-wisdomadventure/TKL_Keyboard/blob/main/Images/OLED_WIRING_image.png)

## Firmware
The firmware is mostly ai written, I just have instructed the ai tool what to do with each component and I got the firmware. It's still not tested and only a proof of concept though. I'll update the readme when I get an actual working firmware!
