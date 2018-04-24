from maestro import Controller
import time, threading

c0 = Controller()

BODY            = 0
FORWARD_BACK    = 1
LEFT_RIGHT      = 2
HEAD_TURN       = 3
HEAD_TILT       = 4

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

# Enumerate positions
MIN    = 3000
MID    = 6000
MAX    = 9000

c0.setTarget(BODY, MID)

# Setting restrictions for all servos
c0.setRange(HEAD_TILT, MIN, MAX)
c0.setRange(HEAD_TURN, MIN, MAX)
c0.setRange(BODY, MIN, MAX)
c0.setRange(FORWARD_BACK, MIN, MAX)
c0.setRange(LEFT_RIGHT, MIN, MAX)

# Setting speeds for all servos
# Setting accelerations for all servos
for i in range(18):
    c0.setSpeed(i, 60)
    c0.setAccel(i, 30)
# c0.setSpeed(HEAD_TILT, 60)
# c0.setSpeed(HEAD_TURN, 60)
# c0.setSpeed(LEFT_RIGHT, 60)
# c0.setSpeed(FORWARD_BACK, 60)
# c0.setSpeed(BODY, 60)



# c0.setAccel(HEAD_TILT, 30)
# c0.setAccel(HEAD_TURN, 30)
# c0.setAccel(BODY, 30)
# c0.setAccel(FORWARD_BACK, 30)
# c0.setAccel(LEFT_RIGHT, 30)

class Motor:
    def __init__(self, forward_back=0, left_right=0, delay=0, forward_back_target=0, left_right_target=0):
        self.delay = delay
        self.forward_back_target = forward_back_target
        self.left_right_target = left_right_target
        self.forward_back = forward_back
        self.left_right = left_right

    def execute(self):
        c0.setTarget(FORWARD_BACK, 6000 + (self.forward_back * self.forward_back_target))
        c0.setTarget(LEFT_RIGHT, 6000 + (self.left_right * self.left_right_target))
        print("Executing Motor Movement")
        time.sleep(self.delay)

        c0.setTarget(FORWARD_BACK, 6000)
        c0.setTarget(LEFT_RIGHT, 6000)

class Body:
    def __init__(self, left_right=0, left_right_target=0):
        self.left_right = left_right
        self.left_right_target = left_right_target

    def execute(self):
        c0.setTarget(BODY, 6000 + (self.left_right * self.left_right_target))
        # print("Executing Body Movement")

class Head: #lol
    def __init__(self, up_down=0, left_right=0, up_down_target=0, left_right_target=0):
        self.up_down_target = up_down_target
        self.left_right_target = left_right_target
        self.left_right = left_right
        self.up_down = up_down


    def execute(self):
        c0.setTarget(HEAD_TURN, 6000 + (self.left_right * self.left_right_target))
        c0.setTarget(HEAD_TILT, 6000 + (self.up_down * self.up_down_target))
        # print("Executing Head Movement" + str(self.up_down_target))


class Wait:
    def __init__(self, delay=0):
        self.delay = delay

    def execute(self):
        print("Executing Wait" + str(self.delay))
        time.sleep(self.delay)

turnRight = Motor(forward_back=0, left_right=-1, delay=1, forward_back_target=0, left_right_target=1100)
turnLeft = Motor(forward_back=0, left_right=1, delay=1, forward_back_target=0, left_right_target=1100)
forward = Motor(forward_back=-1, left_right=0, delay=1, forward_back_target=1100, left_right_target=0)
turnAround = Motor(forward_back=0, left_right=-1, delay=2, forward_back_target=0, left_right_target=1100)

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


def robot_flee():
    runThread = threading.Thread(target=run_away)
    runThread.start()
    turnAround.execute()
    wrist_center()
    lower_arm()
    straighten_arm()
