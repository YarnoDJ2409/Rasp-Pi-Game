from gpiozero import MCP3008
from time import sleep

x_axis = MCP3008(channel=0)
y_axis = MCP3008(channel=1)

CENTER = 0.5
DEADZONE = 0.1
DELAY = 0.5

while True:

    x = x_axis.value
    y = y_axis.value

    horizontal = ""
    vertical = ""

    # X axis
    if x < CENTER - DEADZONE:
        horizontal = "LEFT"
    elif x > CENTER + DEADZONE:
        horizontal = "RIGHT"

    # Y axis
    if y < CENTER - DEADZONE:
        vertical = "DOWN"
    elif y > CENTER + DEADZONE:
        vertical = "UP"

    # Combine them
    if vertical and horizontal:
        direction = vertical + "-" + horizontal
    elif vertical:
        direction = vertical
    elif horizontal:
        direction = horizontal
    else:
        direction = "CENTER"

    print(f"X={x:.2f} Y={y:.2f} -> {direction}")

    sleep(DELAY)