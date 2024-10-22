import pyfirmata
from pyfirmata import SERVO

comport = 'COM6' # Replace with your port

board = pyfirmata.Arduino(comport)

servos = [board.get_pin(f'd:{i}:s') for i in range(8, 13)]

for servo in servos:
    servo.mode = SERVO

def move_servo(fingerUp):
    for i, finger in enumerate(fingerUp):
        angle = 90 if finger == 1 else 0
        servos[i].write(angle)

  """
  ***OR YOU CAN HARDCODE LIKE THIS***
  
  import pyfirmata
from pyfirmata import SERVO

comport = 'COM6'

board = pyfirmata.Arduino(comport)

# Attach servos to digital pins 8 to 12
servo_1 = board.get_pin('d:8:s')
servo_2 = board.get_pin('d:9:s')
servo_3 = board.get_pin('d:10:s')
servo_4 = board.get_pin('d:11:s')
servo_5 = board.get_pin('d:12:s')

# Set servos to servo mode
servo_1.mode = SERVO
servo_2.mode = SERVO
servo_3.mode = SERVO
servo_4.mode = SERVO
servo_5.mode = SERVO

def move_servo(fingerUp):
    if fingerUp == [0, 0, 0, 0, 0]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [1, 0, 0, 0, 0]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 1, 0, 0, 0]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 0, 1, 0, 0]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 0, 0, 1, 0]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(90)
        servo_5.write(0)

    if fingerUp == [0, 0, 0, 0, 1]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [1, 1, 0, 0, 0]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 1, 1, 0, 0]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 0, 1, 1, 0]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(0)

    if fingerUp == [0, 0, 0, 1, 1]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(90)
        servo_5.write(90)

    if fingerUp == [1, 0, 0, 1, 0]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(90)
        servo_5.write(0)

    if fingerUp == [1, 0, 0, 0, 1]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [1, 0, 1, 0, 0]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 1, 0, 0, 1]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [0, 1, 0, 1, 0]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(0)
        servo_4.write(90)
        servo_5.write(0)

    if fingerUp == [0, 0, 1, 0, 1]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [1, 1, 1, 0, 0]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(0)

    if fingerUp == [0, 1, 1, 1, 0]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(0)

    if fingerUp == [0, 0, 1, 1, 1]:
        servo_1.write(0)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(90)

    if fingerUp == [1, 0, 1, 0, 1]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [1, 1, 0, 0, 1]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(0)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [0, 1, 1, 0, 1]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [1, 0, 0, 1, 1]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(0)
        servo_4.write(90)
        servo_5.write(90)

    if fingerUp == [1, 1, 1, 1, 0]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(0)

    if fingerUp == [0, 1, 1, 1, 1]:
        servo_1.write(0)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(90)

    if fingerUp == [1, 0, 1, 1, 1]:
        servo_1.write(90)
        servo_2.write(0)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(90)

    if fingerUp == [1, 1, 0, 1, 1]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(0)
        servo_4.write(90)
        servo_5.write(90)

    if fingerUp == [1, 1, 1, 0, 1]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(0)
        servo_5.write(90)

    if fingerUp == [1, 1, 1, 1, 1]:
        servo_1.write(90)
        servo_2.write(90)
        servo_3.write(90)
        servo_4.write(90)
        servo_5.write(90)

    #Add all other finger combinations here
  """
