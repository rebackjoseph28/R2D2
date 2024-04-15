import RPi.GPIO as GPIO
import time

class Motor:
    # Define GPIO pins for the A4988 connections
    STEP_PIN = 21
    DIR_PIN = 20
    ENABLE_PIN = 16

    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO pins
    GPIO.setup(STEP_PIN, GPIO.OUT)
    GPIO.setup(DIR_PIN, GPIO.OUT)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)

    # Function to move the stepper motor
    def move_stepper(steps, direction, delay):
        # Set the direction
        if direction == 1:    
            GPIO.output(Motor.DIR_PIN, GPIO.HIGH)
        elif direction == 0:
            GPIO.output(Motor.DIR_PIN, GPIO.LOW)
        
        # Enable the motor
        GPIO.output(Motor.ENABLE_PIN, GPIO.LOW)
        
        # Step the motor
        for _ in range(steps):
            GPIO.output(Motor.STEP_PIN, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(Motor.STEP_PIN, GPIO.LOW)
            time.sleep(delay)
        
        # Disable the motor
    def disable_motor():
        GPIO.output(Motor.ENABLE_PIN, GPIO.HIGH)

    def cleanup():
        GPIO.cleanup()
