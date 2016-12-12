from lib.lights import lights
from time import sleep

def spell(message):
    for character in message:
        if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
            lights[character].blink(1, 0.5, 1, False)
        elif character == ' ':
            sleep(0.5)
