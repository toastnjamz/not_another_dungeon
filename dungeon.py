from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [
	    "You died. You kinda suck at this.",
	    "Wow, you really outdid yourself there.",
	    "Lamesauce.",
	    "Oh snap! You dead!"
    ]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class Cell(Scene):

	def enter(self):
		print "You wake up in a cell in what looks like a dungeon after a night of dwarven debauchery."
		print "How did this happen? One minute you were drinking mead with your clanmates..."
		print "...The next you woke up in here! Your head is pounding (mead hangovers are the worst)."
		print "You have to get out of here. You could really use a vitality drink and a shower."
		print "You take a look around. You see a guard with his back to you posted outside. What do you do?"

		action = raw_input("> ")

		if action == "talk to guard":
			print "The guard grunts, but doesn't bother turning around."
			print "Seems like talking to him won't get you anywhere."
			return 'cell'

		elif action == "wait" or "nothing":
			print "You're so hungover, you die of dehydration."
			return 'death'

		elif action == "search cell":
			print "You search your cell and find a small stick. You're pretty good at lockpicking."
			print "You use it to quickly pick the lock. The cell door creaks open."
			return 'central cordior'

		else:
			print "This game is pretty limited. Try again."
			return 'cell'


class CentralCorridor(Scene):

	def enter(self):
		print "The guard slowly turns when he hears the door creaking. He sees you're trying to escape."
		print "He starts to run toward you, cursing."
		print "You only have a split second to decide what to do! Do you:"
		print "1. Stand your ground and fight him mono e mono"
		print "2. Try to run between his legs (you're pretty short, being a dwarf and all)"
		print "3. Give up. You're too hungover for this shite"

		action = raw_input("> ")

		if action == "1":
		    print "The guard sees that you're attempting to fight and cuts you down with his sword."
		    print "You have no armor or weapons to defend yourself and the blade cuts right through your mead-stained tunic."
		    print "You bleed to death on the dungeon floor."
		    return ('death')

		if action == "2":
		    print "Your're quick on your feet. You dodge the guard's blows and run between his legs, narrowly escaping!"
		    return ('armory')

		if action == "3":
		    print "The guard knocks you prone and throws you back in your cell."
		    print "Way to go, tough guy."
		    return ('cell')

class Armory(Scene):

	def enter(self):
		print "You run down the corridor and into the first room you see."
		print "Embers of Ragnaros! You've stumbled into the armory!"
		print "The room's piled with weapons. Which do you choose?"
		print "1. A mace. Mmm... spikey."
		print "2. A battleaxe. Nothing like a familiar weapon to help you break out of prison!"
		print "3. A parisol. What's this even doing in here?!"

		action = raw_input("> ")

		if action == "1":
		    print "The guard rounds the corner into the armory and sees that you're attempting to fight." 
		    print "He swings his sword at you. You fumble with the mace."
		    print "It's just not what you're used to (spikey end towards the enemy, right?) Damn hangover!"
		    print "He hits you and you go down. You bleed to death on the armory floor."
		    return ('death')

		if action == "2":
		    print "The guard rounds the corner and you have just enough time to take him out with a surprise attack."
		    print "Baruk Khazad! He hits the floor, unconsious."
		    print "You peep around the corner and see main exit flanked by two more guards."
		    print "You steel yourself and round the corner, gripping your battle axe. You charge the guards."
		    return ('main exit')

		if action == "3":
		    print "The guard runs around the corner and you try to distract him with your pretty parisol."
		    print "He's not having it, but he snickers. He knocks you out and you wake up back in you cell."
		    return ('cell')
        

class MainExit(Scene):

	def enter(self):
		print "It's time for the final showdown! You swing your trusty axe at the first guard, cutting him down."
		print "The second guard is a bit tougher and parries your blows, but he leaves himself open after a deflection."
		print "You swing your axe and cut him in the side. He cries out and crumples to the floor."
		print "No time to waste! Time to open the gates to freedom!"
		print "You sure could use a drink after this (hair o' the warg?)"
		print "What's this? Another lock? It's a combo lock! Who even does that? And on a dungeon door!"
		print "You have to guess the combo to escape before more guards appear."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[combo]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "Incorrect!"
			guesses += 1
			guess = raw_input("[combo]> ")

		
		if int(guess) != code:
    	    print "You fumble with the lock one more time before more guards rush you and knock you down."
	    	print "The last thing you see, looking up at the ceiling, is five guards crowding around you and laughing."
	    	print "They curse and spit at you before bringing the axe you stole down on your neck."
	    	return "death"

	    else:
	        print "The lock clicks open and falls to the floor."
			print "You push the heavy doors open and feel a cool breeze on your face. Freedom!"
			print "You look around to try to gauge your location. You don't recognize this place."
			print "Wait, you see a banner waving in the breeze. But... how?! The Ronar Provice is over 600 miles away!"
			
			
			return "finished"
		

class Map(object):

	scenes = [
	    'cell': Cell(),
	    'central_corridor': CentralCorridor(),
	    'armory': Armory(),
	    'main_exit': MainExit()

	    ]

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('cell')
a_game = Engine(a_map)
a_game.play()
