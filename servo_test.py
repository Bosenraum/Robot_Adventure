from maestro import Controller
import time

c0 = Controller()

for i in range(18):
    c0.setSpeed(i, 60)
    c0.setAccel(i, 30)

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

def open_close(n):
    for i in range(n):
        c0.setTarget(RIGHT_HAND, MIN)
        time.sleep(1)
        c0.setTarget(RIGHT_HAND, MID)
        time.sleep(1)

def raise_arm():
    c0.setTarget(RIGHT_SHOULDER_UD, MAX)

def lower_arm():
    c0.setTarget(RIGHT_SHOULDER_UD, MIN)

def straighten_arm():
    c0.setTarget(RIGHT_SHOULDER_LR, 6500)
    c0.setTarget(RIGHT_ELBOW, MID)
    c0.setTarget(RIGHT_WRIST_UD, MID)
    c0.setTarget(RIGHT_WRIST_ROTATE, MID)

def bend_arm():
    # c0.setTarget(RIGHT_SHOULDER_UD, MID)
    c0.setTarget(RIGHT_ELBOW, 8000)

def rest_arm():
    c0.setTarget(RIGHT_SHOULDER_UD, MID)

def wrist_up():
    c0.setTarget(RIGHT_WRIST_UD, 8500)

def wrist_rest():
    c0.setTarget(RIGHT_WRIST_UD, MID)

def wrist_down():
    c0.setTarget(RIGHT_WRIST_UD, 3500)

def wrist_right():
    c0.setTarget(RIGHT_WRIST_ROTATE, 400)

def wrist_center():
    c0.setTarget(RIGHT_WRIST_ROTATE, MID)

def wrist_left():
    c0.setTarget(RIGHT_WRIST_ROTATE, 8000)

def wave():
    raise_arm()
    wrist_up()
    time.sleep(1)
    for i in range(3):
        c0.setTarget(RIGHT_SHOULDER_LR, 5000)
        wrist_left()
        time.sleep(.75)
        c0.setTarget(RIGHT_SHOULDER_LR, 7000)
        wrist_right()
        time.sleep(.75)
    wrist_center()
    straighten_arm()
    lower_arm()

def arm_attack():
    raise_arm()
    bend_arm()
    wrist_up()
    wrist_right()
    c0.setTarget(RIGHT_SHOULDER_LR, 8000)
    time.sleep(2)
    wrist_center()
    wrist_rest()
    rest_arm()
    straighten_arm()

def run_away():
    raise_arm()
    # time.sleep(1)
    bend_arm()
    time.sleep(.5)
    for i in range(3):
        wrist_left()
        time.sleep(.5)
        wrist_right()
        time.sleep(.5)
    wrist_center()
    lower_arm()
    straighten_arm()

# run_away()
# time.sleep(3)
arm_attack()
time.sleep(1)
lower_arm()

# rest_arm()
# straighten_arm()
# wave()
# straighten_arm()
# rest_arm()
# bend_arm()
# open_close(3)


# wrist_right()
# time.sleep(1)
# wrist_center()
# time.sleep(1)
# wrist_left()
# time.sleep(1)
# wrist_center()


# raise_arm()
# straighten_arm()
# time.sleep(2)
# open_close(1)
# rest_arm()
# time.sleep(2)
# bend_arm()
# time.sleep(2)
# open_close(1)


# c0.setTarget(RIGHT_SHOULDER_UD, MID)
# time.sleep(2)
# c0.setTarget(RIGHT_SHOULDER_LR, MID)
# time.sleep(2)
# c0.setTarget(RIGHT_ELBOW, MID)
# time.sleep(2)
# c0.setTarget(RIGHT_WRIST_UD, MID)
# time.sleep(2)
# c0.setTarget(RIGHT_WRIST_ROTATE, MID)
# time.sleep(2)
# c0.setTarget(RIGHT_HAND, MID)
# time.sleep(2)
