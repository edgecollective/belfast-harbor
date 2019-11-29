# belfast-harbor

Reference:

https://github.com/DaveSprague/Belfast-Harbor-Tide-Project

## OS Upgrade

Requires CircuitPython 4+, which you can download for various boards [here](https://circuitpython.org/downloads).

To upgrade CircuitPython, double-press the RESET button; this will bring up the BOOT drive; drag-drop the relevant UF2 file to the BOOT drive. Board will reset automatically.

## Gateway Firmware 

- Copy the entire 'lib' folder to the CIRCUITPYTHON drive. 
- Copy gateway.py to 'main.py' and copy it to the CIRCUITPYTHON drive 
- Rename 'dummy_secrets.py' to 'secrets.py' and add your WiFi credentials, along with your farmos public_key and private_key; then copy 'secrets.py' to the CIRCUITPYTHON drive.

## Wiring

### M4, ESP2

USB, VIN

GND, GND

MISO, MISO

MOSI, MOSI

SCK, SCK

D10, CS

D11, RESET

D9, BUSY

## M4, LoRA

3V, VIN

GND, GND

MISO, MISO

MOSI, MOSI

SCK, SCK

A5, CS

A4, RST



