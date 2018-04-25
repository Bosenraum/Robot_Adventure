from pygame import mixer
from Enumerations import *

mixer.init()

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
	twinkle = None
	sphinx = None
	coffee = None
	heal = None
	vanish = None
	best = None

	playing = None

	def __init__(self):
		pass

	@staticmethod
	def init():
		Sounds.theme		= mixer.Sound("audio/theme_wav.wav")
		Sounds.boss		 = mixer.Sound("audio/wizard_battle.wav")
		Sounds.weak_hit	 = mixer.Sound("audio/weak_hit.wav")
		Sounds.med_hit	  = mixer.Sound("audio/medium_hit.wav")
		Sounds.hard_hit	 = mixer.Sound("audio/hard_hit.wav")
		Sounds.lose		 = mixer.Sound("audio/game_over.wav")
		Sounds.wrong_answer = mixer.Sound("audio/wrong_answer.wav")
		Sounds.twinkle	  = mixer.Sound("audio/twinkle.wav")
		Sounds.win        = mixer.Sound("audio/win.wav")
		Sounds.sphinx     = mixer.Sound("audio/sphinx.wav")
		Sounds.coffee     = mixer.Sound("audio/coffee_shop.wav")
		Sounds.heal       = mixer.Sound("audio/heal.wav")
		Sounds.vanish     = mixer.Sound("audio/VOBD_Assassin_PL_Start_Action_Skill_23_1-i_vanish.wav")
		Sounds.best       = mixer.Sound("audio/NAR_Live_Claptrap_194-i_am_the_best_robot.wav")

	@staticmethod
	def getPlaying():
		return Sounds.playing

	@staticmethod
	def playSound(sound):
		if(sound == SoundEffect.THEME):
			Sounds.theme.play(loops=-1)
			Sounds.playing = SoundEffect.THEME
		elif(sound == SoundEffect.BOSS):
			Sounds.boss.play(loops=-1)
			Sounds.playing = SoundEffect.BOSS
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
			Sounds.win.play()
		elif(sound == SoundEffect.TWINKLE):
			Sounds.twinkle.play()
		elif(sound == SoundEffect.SPHINX):
			Sounds.sphinx.play(loops=-1)
			Sounds.playing = SoundEffect.SPHINX
		elif(sound == SoundEffect.COFFEE):
			Sounds.coffee.play(loops=-1)
			Sounds.playing = SoundEffect.COFFEE
		elif(sound == SoundEffect.HEAL):
			Sounds.heal.play()
		elif(sound == SoundEffect.VANISH):
			Sounds.vanish.play()
		elif(sound == SoundEffect.BEST):
			Sounds.best.play()


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
			Sounds.win.stop()
		elif(sound == SoundEffect.TWINKLE):
			Sounds.twinkle.stop()
		elif(sound == SoundEffect.SPHINX):
			Sounds.sphinx.stop()
		elif(sound == SoundEffect.COFFEE):
			Sounds.coffee.stop()
		elif(sound == SoundEffect.HEAL):
			Sounds.heal.stop()
		elif(sound == SoundEffect.VANISH):
			Sounds.vanish.stop()
		elif(sound == SoundEffect.BEST):
			Sounds.best.stop()

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
			Sounds.win.fadeout(1000)
		elif(sound == SoundEffect.SPHINX):
			Sounds.sphinx.fadeout(3000)
		elif(sound == SoundEffect.COFFEE):
			Sounds.coffee.fadeout(1000)
		elif(sound == SoundEffect.VANISH):
			Sounds.vanish.fadeout(1000)
		elif(sound == SoundEffect.BEST):
			Sounds.best.fadeout(1000)
