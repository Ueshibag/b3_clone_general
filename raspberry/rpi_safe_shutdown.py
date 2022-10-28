# --------------------------------------------------------
# rpi_safe_shutdown.py
#
# Safely reboot/shutdown the Raspberry PI by polling one of its
# GPIOs.
#    1.) If you press the button momentarily, the Pi will reboot.
#    2.) Holding down the button for about 3 seconds the Pi will shutdown.
#
import time
import RPi.GPIO as GPIO

# GPIO6 = pin 31 on the RPI header
reset_shutdown_pin = 6

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Use built-in internal pullup resistor
# When the ON/OFF switch is closed (ON), shutdown_pin = 0
# When the ON/OFF switch os open (OFF), shutdown_pin = 1
GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# modular function to restart Pi
def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
    
# modular function to shutdown Pi
def shut_down():
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

# Check button if we want to shutdown the Pi safely
while True:

    if GPIO.input(reset_shutdown_pin) == True:
        counter = 0

        while GPIO.input(reset_shutdown_pin) == False:
            counter += 1
            time.sleep(0.5)

            # if long button press
            if counter > 6:
                shut_down()

        # if short button press, restart!
        restart()
