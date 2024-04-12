import RPi.GPIO as GPIO
import time

# Define GPIO pins for the A4988 connections
STEP_PIN = 17
DIR_PIN = 27
ENABLE_PIN = 22

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Function to move the stepper motor
def move_stepper(steps, direction, delay):
    # Set the direction
    GPIO.output(DIR_PIN, direction)
    
    # Enable the motor
    GPIO.output(ENABLE_PIN, GPIO.LOW)
    
    # Step the motor
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)
    
    # Disable the motor
    GPIO.output(ENABLE_PIN, GPIO.HIGH)

try:
    # Move the stepper motor 200 steps clockwise with a delay of 0.005 seconds
    move_stepper(200, GPIO.HIGH, 0.005)
    
    # Pause for 1 second
    time.sleep(1)
    
    # Move the stepper motor 200 steps counterclockwise with a delay of 0.005 seconds
    move_stepper(200, GPIO.LOW, 0.005)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
