import board
import busio
import digitalio
import time
import adafruit_rfm9x


# lora radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D9)
reset = digitalio.DigitalInOut(board.D10)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

# led
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:

    p1=1.
    p2=2.
    p3=3.

    send_str=str(p1)+","+str(p2)+","+str(p3)

    print(send_str)

    rfm9x.send(send_str)

    led.value=True
    time.sleep(.1)
    led.value=False
    time.sleep(.1)


    time.sleep(1)