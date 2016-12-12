# Stranger Things Christmas Lights API - Powered by Raspberry Pi

This project allows to reproduce the Christmas Lights scene from the `Stranger Things` TV Show using a Raspberry Pi.
It provides a REST API for spelling messages by flashing LEDs assigned to alphabet letters.

It was tested with the Raspberry Pi 3 Model B.


## Prerequisites

* A Raspberry Pi 3 Model B
* Python 3 installed on the Raspberry Pi with the following librairies:
    * gpiozero
    * flask
* 26 LED Lights
* Cables
* Resistors


## Hardware Setup

Refer to the following pin mapping:

![Raspberry Pi 3 Pinout](https://gpiozero.readthedocs.io/en/v1.3.1/_images/pin_layout.svg)

Each LED should have its anode connected to a GPIO pin, and its cathode connected to a Ground pin, **with a limiting resistor** connected on either side of the LED.

Every letter of the alphabet is mapped to a specific GPIO pin:

```
a => GPIO2
b => GPIO3
c => GPIO4
d => GPIO17
e => GPIO27
f => GPIO22
g => GPIO10
h => GPIO9
i => GPIO11
j => GPIO5
k => GPIO6
l => GPIO13
m => GPIO19
n => GPIO26
o => GPIO14
p => GPIO15
q => GPIO18
r => GPIO23
s => GPIO24
t => GPIO25
u => GPIO8
v => GPIO7
w => GPIO12
x => GPIO16
y => GPIO20
z => GPIO21
```


## Software Setup

1. Clone this repository to your Raspberry Pi
2. `cd stranger-things-pi`
3. `python3 main.py`


## Usage

The API runs on port 8080. To spell a message, send a POST request to `/send` with the message as plain text in the request body.


## License

Copyright (c) 2016 Pier-Luc Brault <plbrault@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
