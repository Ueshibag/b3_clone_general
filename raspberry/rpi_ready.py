# rpi_ready.py
#
# ----------------------------------------------------------------------------
#          Raspberry Pi signals to Drawbars Control board it is ready
# ----------------------------------------------------------------------------
#
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from time import sleep

# GPIO5 in BCM mode
rpi_ready = 5

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(rpi_ready, GPIO.OUT, initial=GPIO.LOW)

sleep(10)

# when the Drawbars Control board sees 'rpi_ready' high, it sends drawbars
# positions to setBfree
GPIO.output(rpi_ready, GPIO.HIGH)


