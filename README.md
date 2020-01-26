# pihut-xmas-asyncio

Demonstration driving the Raspberry Pi PiHut 3D Xmas tree using Python Asyncio


![The tree in blinky action](https://github.com/davesteele/pihut-xmas-asyncio/raw/master/images/Blinky.gif)

[The Pi Hut](https://thepihut.com/) is selling a
[3D Xmas Tree](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi)
that plugs into the Raspberry Pi
[GPIO header](https://www.raspberrypi.org/documentation/usage/gpio/).

Raspbian includes a Python [GPIO Module](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/) that facilitates working with PI I/O.

Recent versions of Python include [Asyncio](https://medium.freecodecamp.org/a-guide-to-asynchronous-programming-in-python-with-asyncio-232e2afa44f6), which provides tools to allow multiple I/O-bound functions to work cooperatively in a single-threaded event loop.

## How to Use It

The script requires the rpi.gpio, which may not be installed by default


    sudo apt-get update
    sudo apt-get install rpi.gpio


Run '*./xmas.py*' to see the lights blink.

Change the constants in the script to change the blink parameters.

run '*sudo ./install.sh*' to have the blink program
come up automatically on boot.

The asyncio syntax used here requires Python 3.5 or newer. It will not run on stock Raspbian Jessie.

## How it Works, in Brief

In [xmas.py](https://github.com/davesteele/pihut-xmas-asyncio/blob/master/xmas.py), the *async* keyword turns a function into a *coroutine*, which is a cousin to a generator function.

Instead of *yield*-ing, the coroutine returns control to the calling function when it passes control to another coroutine, flagged with the *await* keyword.

The *ensure_future()* function submits coroutines to the main event loop, which is then called to kick things off.
