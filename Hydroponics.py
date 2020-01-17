# Import required modules
from datetime import date, time, datetime
import time
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


# Define current, ON, and OFF times
now = datetime.now()
on_time = now.replace(hour=8, minute=00, second=00)
off_time = now.replace(hour=18, minute=00, second=00)

# Loop to control GPIO output
while True:
    if (now > on_time and now < off_time):
        GPIO.output(8, GPIO.HIGH)
        sleep(30)
    else:
        GPIO.output(8, GPIO.LOW)


