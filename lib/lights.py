from gpiozero import LED

_UPPERCASE_OFFSET = 41
_LOWERCASE_OFFSET = 97

lights = {}

for gpioID in range(1, 26):
    led = LED(gpioID)
    lights[chr(_UPPERCASE_OFFSET + gpioID)] = led
    lights[chr(_LOWERCASE_OFFSET + gpioID)] = led
