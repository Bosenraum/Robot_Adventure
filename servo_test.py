from maestro import Controller
from time import sleep

c0 = Controller()

RIGHT_SHOULDER_UD = 5
RIGHT_SHOULDER_LR = 6
RIGHT_ELBOW = 7
RIGHT_WRIST_UD = 8
RIGHT_WRIST_ROTATE = 9
RIGHT_HAND = 10

LEFT_SHOULDER_UD = 11
LEFT_SHOULDER_LR = 12
LEFT_ELBOW = 13
LEFT_WRIST_UD = 14
LEFT_WRIST_ROTATE = 15
LEFT_HAND = 16

MIN    = 3000
MID    = 6000
MAX    = 9000

c0.setTarget(RIGHT_SHOULDER_UD, MID)
time.sleep(2)
c0.setTarget(RIGHT_SHOULDER_LR, MID)
time.sleep(2)
c0.setTarget(RIGHT_ELBOW, MID)
time.sleep(2)
c0.setTarget(RIGHT_WRIST_UD, MID)
time.sleep(2)
c0.setTarget(RIGHT_WRIST_ROTATE, MID)
time.sleep(2)
c0.setTarget(RIGHT_HAND, MID)
time.sleep(2)
