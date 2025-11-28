#!/usr/bin/python3

import asyncio
import random
import signal
import RPi.GPIO as GPIO

# time in seconds
ONTIME = 6
OFFTIME = 0.3

# Random range in the led on/off times (between 0 and 1)
PLUSORMINUS = 0.5

# The time that a given twinkle power is set, in msec
TWINKLEUPDATEPERIOD = 100
# The Twinkle PWM period, in msec
TWINKLEPWMPERIOD = 20


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


async def main():
    loop = asyncio.get_running_loop()
    maintask = asyncio.current_task()

    def do_sigterm():
        maintask.cancel()

    loop.add_signal_handler(signal.SIGTERM, do_sigterm)

    # create a Task for each led.
    # gpio 2 is the yellow star - 4-27 are the other tree lights
    tasks = [loop.create_task(blink_led(x)) for x in range(2, 28) if x != 3]

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        [task.cancel() for task in tasks]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
