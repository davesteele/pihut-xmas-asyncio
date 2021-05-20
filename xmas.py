#!/usr/bin/python3

import asyncio
import random
import signal
import RPi.GPIO as GPIO

# time in seconds
ONTIME = 1.5
OFFTIME = 0.3

# Random range in the times (between 0 and 1)
PLUSORMINUS = 0.3

GPIO.setmode(GPIO.BCM)


def calcplusorminus(val, var):
    """return random number in the range val +/- (var*100)%"""
    factor = (1.0 - var) + (random.random() * 2 * var)
    return factor * val


async def blink_led(ledno):
    """The led blinking coroutine for one led."""
    ontime = calcplusorminus(ONTIME, PLUSORMINUS)
    offtime = calcplusorminus(OFFTIME, PLUSORMINUS)

    GPIO.setup(ledno, GPIO.OUT)

    try:
        while True:
            GPIO.output(ledno, GPIO.HIGH)
            await asyncio.sleep(ontime)

            GPIO.output(ledno, GPIO.LOW)
            await asyncio.sleep(offtime)
    except asyncio.CancelledError:
        GPIO.setup(ledno, GPIO.IN)


async def amain():
    # create a Task for each led.
    # gpio 2 is the yellow star - 4-27 are the other tree lights
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(blink_led(x)) for x in range(2, 28) if x != 3]

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        [task.cancel() for task in tasks]
        await asyncio.gather(*tasks)


def do_sigterm():
    """SIGTERM triggers the KeyboardInterrupt handler."""
    raise KeyboardInterrupt


def main():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGTERM, do_sigterm)

    task = loop.create_task(amain())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        task.cancel()
        loop.run_until_complete(task)


if __name__ == "__main__":
    main()
