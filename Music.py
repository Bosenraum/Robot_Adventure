from pygame import mixer
from enum import Enum

mixer.init()

class SoundEffect(Enum):
    THEME  = 1
    BOSS   = 2
    WEAK   = 3
    MEDIUM = 4
    HARD   = 5
    LOSE   = 6
    WIN    = 7
    WRONG  = 8

class Sounds:
    # create static class variables for necessary sounds
    theme = None
    boss = None
    weak_hit = None
    med_hit = None
    hard_hit = None
    lose = None
    win = None
    wrong_answer = None

    def __init__(self):
        pass

    @staticmethod
    def init():
        Sounds.theme        = mixer.Sound("audio/theme_wav.wav")
        Sounds.boss         = mixer.Sound("audio/wizard_battle.wav")
        Sounds.weak_hit     = mixer.Sound("audio/weak_hit.wav")
        Sounds.med_hit      = mixer.Sound("audio/medium_hit.wav")
        Sounds.hard_hit     = mixer.Sound("audio/hard_hit.wav")
        Sounds.lose         = mixer.Sound("audio/game_over.wav")
        Sounds.wrong_answer = mixer.Sound("audio/wrong_answer.wav")

    @staticmethod
    def playSound(sound):
        if(sound == SoundEffect.THEME):
            Sounds.theme.play(loops=-1)
        elif(sound == SoundEffect.BOSS):
            Sounds.boss.play(loops=-1)
        elif(sound == SoundEffect.WEAK):
            Sounds.weak_hit.play()
        elif(sound == SoundEffect.MEDIUM):
            Sounds.med_hit.play()
        elif(sound == SoundEffect.HARD):
            Sounds.hard_hit.play()
        elif(sound == SoundEffect.LOSE):
            Sounds.lose.play()
        elif(sound == SoundEffect.WRONG):
            Sounds.wrong_answer.play()
        elif(sound == SoundEffect.WIN):
            #Sounds.win.play()
            pass

    @staticmethod
    def stopSound(sound):
        if(sound == SoundEffect.THEME):
            Sounds.theme.stop()
        elif(sound == SoundEffect.BOSS):
            Sounds.boss.stop()
        elif(sound == SoundEffect.WEAK):
            Sounds.weak_hit.stop()
        elif(sound == SoundEffect.MEDIUM):
            Sounds.med_hit.stop()
        elif(sound == SoundEffect.HARD):
            Sounds.hard_hit.stop()
        elif(sound == SoundEffect.LOSE):
            Sounds.lose.stop()
        elif(sound == SoundEffect.WRONG):
            Sounds.wrong_answer.stop()
        elif(sound == SoundEffect.WIN):
            #Sounds.win.stop()
            pass

    @staticmethod
    def fadeSound(sound):
        if(sound == SoundEffect.THEME):
            Sounds.theme.fadeout(1000)
        elif(sound == SoundEffect.BOSS):
            Sounds.boss.fadeout(1000)
        elif(sound == SoundEffect.WEAK):
            Sounds.weak_hit.fadeout(1000)
        elif(sound == SoundEffect.MEDIUM):
            Sounds.med_hit.fadeout(1000)
        elif(sound == SoundEffect.HARD):
            Sounds.hard_hit.fadeout(1000)
        elif(sound == SoundEffect.LOSE):
            Sounds.lose.fadeout(1000)
        elif(sound == SoundEffect.WRONG):
            Sounds.wrong_answer.fadeout(1000)
        elif(sound == SoundEffect.WIN):
            #Sounds.win.fadeout(1000)
            pass
