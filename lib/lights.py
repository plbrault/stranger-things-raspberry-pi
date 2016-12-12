from copy import copy
from gpiozero import LED

lights = {
    'a': LED(2),
    'b': LED(3),
    'c': LED(4),
    'd': LED(17),
    'e': LED(27),
    'f': LED(22),
    'g': LED(10),
    'h': LED(9),
    'i': LED(11),
    'j': LED(5),
    'k': LED(6),
    'l': LED(13),
    'm': LED(19),
    'n': LED(26),
    'o': LED(14),
    'p': LED(15),
    'q': LED(18),
    'r': LED(23),
    's': LED(24),
    't': LED(25),
    'u': LED(8),
    'v': LED(7),
    'w': LED(12),
    'x': LED(16),
    'y': LED(20),
    'z': LED(21)
}

for key in copy(lights):
    lights[key.upper()] = lights[key]
