from gpiozero import Button
from signal import pause

button_a_pin = 17 #GPIO number
button_b_pin = 27 #GPIO number

# Assign the two main buttons to their corresponding GPIO pins on the RPi board
button_a = Button(button_a_pin)
button_b = Button(button_b_pin)

def main_button_press(button):
    print(f"Button on GPIO {button.pin.number} has been pressed!")

button_a.when_pressed = main_button_press
button_b.when_pressed = main_button_press

pause()