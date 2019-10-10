import time
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name=bucket, bucket_key=bucket, access_key=access_key)

streamer.log("My Messages", "Stream Starting")

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

streamer.log("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
streamer.log("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

streamer.log("Distance:",distance,"cm")

GPIO.cleanup()


streamer.log("My Messages", "Stream Done")

streamer.close()
