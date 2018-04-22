from maestro import Controller
from time import sleep

c0 = Controller()

RIGHT_SHOULDER_UD = 6
RIGHT_SHOULDER_LR = 7
RIGHT_ELBOW = 8
RIGHT_WRIST_UD = 9
RIGHT_WRIST_ROTATE = 10
RIGHT_HAND = 11

LEFT_SHOULDER_UD = 12
LEFT_SHOULDER_LR = 13
LEFT_ELBOW = 14
LEFT_WRIST_UD = 15
LEFT_WRIST_ROTATE = 16
LEFT_HAND = 17

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
