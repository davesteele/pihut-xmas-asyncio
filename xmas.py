#!/usr/bin/python3

import asyncio
import random
import RPi.GPIO as GPIO

# time in seconds
ONTIME = 1.5
OFFTIME = .3

# Random range in the times (between 0 and 1)
PLUSORMINUS = .3

GPIO.setmode(GPIO.BCM)


def calcplusorminus(val, var):
    """return random number in the range val +/- (var*100)%"""
    factor = (1.0 - var) + (random.random() * 2 * var)
    return factor * val


async def blink_led(ledno):
    ontime = calcplusorminus(ONTIME, PLUSORMINUS)
    offtime = calcplusorminus(OFFTIME, PLUSORMINUS)

    GPIO.setup(ledno, GPIO.OUT)

    while True:
        GPIO.output(ledno, GPIO.HIGH)
        await asyncio.sleep(ontime)

        GPIO.output(ledno, GPIO.LOW)
        await asyncio.sleep(offtime)

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(blink_led(x)) for x in range(2, 27)]
loop.run_forever()

loop.close()
