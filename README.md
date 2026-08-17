Simple incremental game for raspberry pi

## Hardware requirements

**Raspberry Pi**
- [Pi 4 (2GB)](https://www.kiwi-electronics.com/nl/raspberry-pi-boards-behuizingen-uitbreidingen-en-accessoires-59/raspberry-pi-4-model-b-2gb-4267)

**Display**
- [4,3 inch display - 800x480 DSI LCD](https://www.kiwi-electronics.com/nl/raspberry-pi-boards-behuizingen-uitbreidingen-en-accessoires-59/beeldschermen-monitoren-voor-de-raspberry-pi-413/4-3-inch-dsi-touch-display-voor-raspberry-pi-800x480-10259)

**Buttons**
- [Main button](https://www.kiwi-electronics.com/nl/drukknop-12mm-10-stuks-403?search=button&page=2) (for selection)
- [Joystick](https://www.kiwi-electronics.com/nl/analoge-2-assige-joystick-met-selectieknop--breakout-board-1839?search=thumb%20joystick)

**MicroSD**
- 32 or 64 GB

**Power Supply**
- [5V 3A power supply](https://www.kiwi-electronics.com/nl/raspberry-pi-boards-behuizingen-uitbreidingen-en-accessoires-59/raspberry-pi-4-usb-c-voeding-zwart-eu-4270) or PiSugar battery

**Extras**
- [Cables](https://www.kiwi-electronics.com/nl/premium-jumperwires-op-strip-40-stuks-f-f-20cm-590?search=F%2FF)
- [MCP3008](https://www.kiwi-electronics.com/nl/mcp3008-8-kanaals-10-bit-adc-met-spi-interface-622?search=MCP) (This part is needed to translate voltages from the analog joystick into bitstrings. The bitstrings are then sent to the pi and read out bit-by-bit)
- [Heatsink](https://www.kiwi-electronics.com/nl/aluminium-heatsink-case-voor-raspberry-pi-4-zwart-4340?search=heatsink) ([alternative link](https://www.123-3d.nl/123-3D-Aluminium-Heatsink-Case-voor-Raspberry-Pi-4-Zwart-i5035.html?utm_source=google&utm_medium=cpc&utm_campaign=PPC-SEA-NL-Google-Shopping-B-Parts-Balanced-Growth-Profit&gad_source=1&gad_campaignid=23928548585&gbraid=0AAAAAC164-Qz2h5X7qTJoYMIPs6CrfSMB&gclid=Cj0KCQjw-frTBhCvARIsADv4XY5e41ozE8pYZuAZ44DwuynKOmwkRwwc2BNEAPkA77jWCG0n48k6TOAaAmFLEALw_wcB))
- [Male headers (90 degree bend)](https://www.kiwi-electronics.com/nl/40-pin-header-strip-90-hoek-2-54mm-pitch-20216?search=header&page=2) (if the joystick lacks headers)

**Optional**
- [Breadboard](https://www.kiwi-electronics.com/nl/400-punt-breadboard-wit-283) (for testing)


## Setting up the software (MicroSD Card)

**Raspberry Pi OS (Operating System)**

Connect the MicroSD to any computer using an adapter. Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/), run it and follow the instructions to write an OS image to your MicroSD. (Setup Raspberry Pi Connect during this process for easy controll of the Raspberry Pi latere down the line.)

**LCD Display**

Locate the *config.txt* on your MicroSD after the Raspberry Pi OS has been succesfully written to the MicroSD card. Add the following lines at the end of the text file:
```
dtoverlay=vc4-kms-v3d
#DSI1 Use
dtoverlay=vc4-kms-dsi-7inch
#DSI0 Use
#dtoverlay=vc4-kms-dsi-7inch,dsi0
```
Run the following lines to update the OS if needed:
```
sudo apt-get update
sudo apt-get full-upgrade -y
```
[Click here](https://www.waveshare.com/wiki/4.3inch_DSI_LCD) for instructions on editing features of the LCD display (such as backlight brightness or display rotation).

## Connecting the hardware

**Raspberry Pi**

- Insert the MicroSD at the underside of the Raspberry Pi
- Insert the power cable (USB-C) to turn on the Raspberry Pi **Do not insert the power cable while connecting any hardware**

**LCD Display**

- Use an FFC (Flexible Flat Cable) to connect the DSI (Display Serial Interface) on the LCD display to the 15PIN DSI interface on the Raspberry Pi board, as shown in the image:
  
  <img width="482" height="364" alt="image" src="https://github.com/user-attachments/assets/8f55070f-7794-48a0-9150-0db3c7ee0db0" />
- For convenience, you can fix the Raspberry Pi on the backside of the LCD display with screws and the copper columns.

**Main Button**

- Connect one pin on the button to a GND (Ground) pin on the Raspberry Pi board (for example pin 9) (see [Raspberry pi pinout](https://pinout.xyz/) for a description of each pin on the Raspberry Pi).
- Connect the pin on the button **diagonal to the one you chose in the previous step** to any GPIO pin on the Raspberry Pi board (for example pin 11).

**Joystick**

 - The joystick must be connected to both the Raspberry Pi board and an MCP3008 converter chip.
 - If no headers are present on the chip of the joystick, solder some male headers with a 90 degree bend onto the chip (with the long heads sticking out sideways, solder the short ends at the bottom of the chip).
 - Below is a table with all connections between the joystick, MCP3008 and Raspberry Pi board (the GND and 3.3V connections are bunched together to the same pin on the Raspberry Pi boar, either by twisting the cables together or using wire nuts):

| Joystick Pin | MCP3008 Pin | Raspberry Pi Pin |
| :---:| :---: | :---: |
| GND | Pin 9 (DGND) & Pin 14 (AGND) | Pin 6 (GND) |
| VCC (3.3V) | Pin 16 (VDD) & Pin 15 (VREF) | Pin 1 (3.3V Power) |
| VRx | Pin 1 (CH0) | - |
| VRy | Pin 2 (CH1) | - |
| SW | - | Pin 22 (GPIO 25) |
| - | Pin 10 (CS/SHDN) | Pin 24 (GPIO 8 / SPI CE0) |
| - | Pin 11 (DIN) | Pin 19 (GPIO 10 / SPI MOSI) |
| - | Pin 12 (DOUT) | Pin 21 (GPIO 9 / SPI MISO) |
| - | Pin 13 (CLK) | Pin 23 (GPIO 11 / SPI SCLK) |

Pinout of the MCP3008:

<img width="300" height="250" alt="image" src="https://github.com/user-attachments/assets/30b33f96-74f7-4bee-8255-c15eaef9c476" />

 - [Click here](https://www.raspberrypi-spy.co.uk/2014/04/using-a-joystick-on-the-raspberry-pi-using-an-mcp3008/) for an example of the joystick connection using an MCP3008.
