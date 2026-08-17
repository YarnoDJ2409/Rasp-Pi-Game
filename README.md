Simple incremental game for raspberry pi

## Hardware requirements

**Raspberry Pi**
- [Pi 4 (2GB)](https://www.kiwi-electronics.com/nl/raspberry-pi-boards-behuizingen-uitbreidingen-en-accessoires-59/raspberry-pi-4-model-b-2gb-4267)

**Display**
- [4,3 inch display - 800x480 DSI LCD](https://www.kiwi-electronics.com/nl/raspberry-pi-boards-behuizingen-uitbreidingen-en-accessoires-59/beeldschermen-monitoren-voor-de-raspberry-pi-413/4-3-inch-dsi-touch-display-voor-raspberry-pi-800x480-10259)
- [Installation Manual](https://www.waveshare.com/wiki/4.3inch_DSI_LCD)

**Buttons**
- [Main button](https://www.kiwi-electronics.com/nl/drukknop-12mm-10-stuks-403?search=button&page=2) (for selection)
- Arrow buttons or [joystick](https://www.kiwi-electronics.com/nl/analoge-2-assige-joystick-met-selectieknop--breakout-board-1839?search=thumb%20joystick)

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
Locate the *config.txt* on your MicroSD after the Raspberry Pi OS has been succesfully written. Add the following lines at the end of the text file:
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

## Connecting the hardware

[Raspberry pi pinout](https://pinout.xyz/)
