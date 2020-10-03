import re

import world.systems.chargen.util as util
import world.systems.professions.profession_prototypes as pr
import world.systems.races.race_prototypes as ra
import world.systems.backgrounds.background_lookups as bl
from evennia import ansi
from evennia.utils import evtable
from random import randint


def node_choose_race(caller):
	text = \
	"""
The following races are available:

|wDwarf|n - Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.
|wElf|n - Elves are a magical people of otherworldly grace, living in the world but not entirely part of it.
|wGnome|n - A gnome's energy and enthusiasm for living shines through every inch of his or her tiny body.
|wHalf-Elf|n - Half-elves combine what some say are the best qualities of their elf and human parents.
|wHalfling|n - The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense.
|wHalf-Orc|n - Half-orcs' grayish pigmentation, sloping foreheads, jutting jaws, prominent teeth, and towering builds make their orcish heritage plain for all to see.
|wHuman|n - Humans are the most adaptable and ambitious people among the common races.
|wTiefling|n - To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye.
|wGoblin|n - Goblins occupy an uneasy place in a dangerous world, and they react by lashing out at any creatures they believe they can bully.
|wKobold|n - Kobolds are typically timid and shy away from conflict, but they are dangerous and vicious if cornered.
|wCentaur|n - Both half human (torso) and half horse (body), they make amazing warriors that can both scout and tank.
|wMinotaur|n - Strong in body, dedication, and courage, Minotaurs are at home on the battlefield with their mighty horns and beast-like brute.

(|wNote|n: You can type '|whelp <race>|n' to see additional info about the race.)

What race will you choose?
	"""
	options = ({'key': '_default',
				"goto": _set_race})

	return text, options


def help_race(caller, race):
	races = {'dwarf': ra.RACE_DWARF,
			 'elf': ra.RACE_ELF,
			 'half-elf': ra.RACE_HALF_ELF,
			 'halfling': ra.RACE_HALFLING,
			 'half-orc': ra.RACE_HALF_ORC,
			 'human': ra.RACE_HUMAN,
			 'tiefling': ra.RACE_TIEFLING,
			 'goblin': ra.RACE_GOBLIN,
			 'kobold': ra.RACE_KOBOLD,
			 'centaur': ra.RACE_CENTAUR,
			 'minotaur': ra.RACE_MINOTAUR}

	caller.msg("\n")
	for key, value in races[race].items():

		if key == 'ability_score':
			key = 'Attribute Bonuses'

		text = "|w%s|n: %s" % (key.title(), value)
		caller.msg(text)
	caller.msg("\n")
	return


def _set_race(caller, raw_string, **kwargs):
	if not caller.nattributes.has('charactersheet'):
		caller.ndb.charactersheet = {}

	races = ['dwarf', 'elf', 'half-elf', 'halfling', 'half-orc', 'human', 'tiefling',
			 'goblin', 'kobold', 'centaur', 'minotaur', 'gnome']

	raw_string = raw_string.lower().strip()

	if len(raw_string.split(' ')) == 2 and raw_string.split(' ')[0] == 'help':
		if raw_string.split(' ')[1] in races:
			help_race(caller, raw_string.split(' ')[1])
			return "node_choose_race"
		else:
			caller.msg("We could not find a help topic for that race choice.")
			return "node_choose_race"

	if raw_string in races:
		caller.ndb.charactersheet['race'] = raw_string

		if raw_string == 'dwarf':
			caller.ndb.charactersheet['traits'] = ra.RACE_DWARF['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_DWARF['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_DWARF['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_DWARF['ability_score']
		elif raw_string == 'elf':
			caller.ndb.charactersheet['traits'] = ra.RACE_ELF['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_ELF['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_ELF['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_ELF['ability_score']
		elif raw_string == 'half-elf':
			caller.ndb.charactersheet['traits'] = ra.RACE_HALF_ELF['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_HALF_ELF['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_HALF_ELF['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_HALF_ELF['ability_score']
		elif raw_string == 'halfling':
			caller.ndb.charactersheet['traits'] = ra.RACE_HALFLING['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_HALFLING['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_HALFLING['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_HALFLING['ability_score']
		elif raw_string == 'half-orc':
			caller.ndb.charactersheet['traits'] = ra.RACE_HALF_ORC['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_HALF_ORC['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_HALF_ORC['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_HALF_ORC['ability_score']
		elif raw_string == 'human':
			caller.ndb.charactersheet['traits'] = ra.RACE_HUMAN['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_HUMAN['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_HUMAN['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_HUMAN['ability_score']
		elif raw_string == 'tiefling':
			caller.ndb.charactersheet['traits'] = ra.RACE_TIEFLING['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_TIEFLING['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_TIEFLING['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_TIEFLING['ability_score']
		elif raw_string == 'goblin':
			caller.ndb.charactersheet['traits'] = ra.RACE_GOBLIN['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_GOBLIN['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_GOBLIN['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_GOBLIN['ability_score']
		elif raw_string == 'kobold':
			caller.ndb.charactersheet['traits'] = ra.RACE_KOBOLD['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_KOBOLD['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_KOBOLD['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_KOBOLD['ability_score']
		elif raw_string == 'centaur':
			caller.ndb.charactersheet['traits'] = ra.RACE_CENTAUR['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_CENTAUR['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_CENTAUR['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_CENTAUR['ability_score']
		elif raw_string == 'minotaur':
			caller.ndb.charactersheet['traits'] = ra.RACE_MINOTAUR['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_MINOTAUR['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_MINOTAUR['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_MINOTAUR['ability_score']
		elif raw_string == 'gnome':
			caller.ndb.charactersheet['traits'] = ra.RACE_GNOME['traits']
			caller.ndb.charactersheet['size'] = ra.RACE_GNOME['size']
			caller.ndb.charactersheet['languages'] = ra.RACE_GNOME['languages']
			caller.ndb.charactersheet['ability_score'] = ra.RACE_GNOME['ability_score']

		# Get attributes ready
		if not caller.nattributes.has('rolled_attributes'):
			caller.ndb.rolled_attributes = util.roll_all_attributes()
			caller.ndb.rolled = 2

		return "node_choose_profession"
	else:
		caller.msg("That is not a valid race. Please pick again.")
		return "node_choose_race"


def node_choose_attributes(caller):
	text = \
"""
You rolled the following attributes. Choose one attribute name and a value or type '|wreroll|n' to reroll all attributes.

	Example: dex 13

The following attributes are available to your race: str, dex, con, int, wis, cha.
Available rerolls: %d
Your attribute roll is the following: %s
""" % (caller.ndb.rolled, caller.ndb.rolled_attributes)

	if caller.nattributes.has('attributes'):
		text = text + ("Your current assigned attributes are: %s" % caller.ndb.attributes)

	options = ({'key': '_default',
				"goto": _set_attribute})

	return text, options


def _set_attribute(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()
	raw_string = raw_string.split(' ')

	if raw_string[0] == 'reroll':
		if caller.ndb.rolled >= 1:
			caller.ndb.rolled = caller.ndb.rolled - 1
			caller.ndb.rolled_attributes = util.roll_all_attributes()
			return "node_choose_attributes"

	if len(raw_string) != 2:
		caller.msg("This is not a valid choice. Please type <attribute name> <rolled valud> with 1 space in between.")
		return "node_choose_attributes"

	if raw_string[0] not in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
		caller.msg("This is not a valid choice. Please type <attribute name> <rolled valud> with 1 space in between.")
		return "node_choose_attributes"

	if not raw_string[1].isnumeric():
		caller.msg("The chosen roll is not a valid integer. Please ensure you type the number correctly.")
		return "node_choose_attributes"

	if int(raw_string[1]) in caller.ndb.rolled_attributes:
		# Check to see if the attributes list exists
		if not caller.nattributes.has('attributes'):
			caller.ndb.attributes = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}

		# Re-assigning attributes in the event the player assigns an attribute that already has been assigned
		if caller.ndb.attributes[raw_string[0]] > 0:
			# Putting the already assigned attribute back in the roll
			caller.ndb.rolled_attributes.append(caller.ndb.attributes[raw_string[0]])
			# Removing the already assigned attribute from the attributes
			caller.ndb.attributes[raw_string[0]] = 0
			caller.msg("Re-assigning %s with %d." % (raw_string[0], int(raw_string[1])))
			caller.ndb.attributes[raw_string[0]] = int(raw_string[1])
			# Removing the newly assigned attribute from the roll
			caller.ndb.rolled_attributes.remove(int(raw_string[1]))
			return "node_choose_attributes"
		else:
			caller.ndb.attributes[raw_string[0]] = int(raw_string[1])
			caller.ndb.rolled_attributes.remove(int(raw_string[1]))

			# Check to see if any more attributes are left in the roll
			if not caller.ndb.rolled_attributes:
				return "node_choose_background"
			else:
				return "node_choose_attributes"
	else:
		caller.msg("The roll value you chose is not available.")
		return "node_choose_attributes"


def node_choose_background(caller):
	text = "The following backgrounds are available:"
	option_list = []

	for key, value in bl.CHARACTER_BACKGROUNDS.items():
		option_list.append({'key': key.title(), 'goto': (_set_background, {"background": (key, value)})})

	options = tuple(option_list)

	return text, options


def _set_background(caller, raw_string, **kwargs):
	background_name, background_value = kwargs.get("background")

	caller.ndb.charactersheet['background'] = background_name
	caller.ndb.charactersheet['background_skills'] = background_value['skills']
	caller.ndb.charactersheet['coin_purse'] = background_value['belt_pouch']

	if background_name == 'entertainer':
		caller.ndb.charactersheet['proficiences'].append("disguise tools")

	for key, value in background_value['skills'].items():
		if key in caller.ndb.skills_available:
			caller.ndb.skills_available[key][0] = True
		else:
			caller.ndb.skills_available.update({key: value})

	if background_value['special']:
		caller.ndb.charactersheet['special_name'] = background_value['special']['name'].title()
		return "node_choose_background_special"

	if background_value['traits']:
		caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + background_value['traits']
	return "node_choose_background_personality"


def node_choose_background_special(caller):
	name = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['special']['name']
	text = "Choose one of the following for your %s:" % name
	option_list = []

	for key, value in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['special'].items():
		if key != 'name':
			option_list.append({'key': value, 'goto': _set_backgroup_special})

	option_list.append({'key': 'Randomize', 'goto': _set_backgroup_special})

	options = tuple(option_list)

	return text, options


def _set_backgroup_special(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string == 'randomize':
		roll = randint(1, len(bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['special']) - 1)
		randomize = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['special'][roll]
		caller.ndb.charactersheet['special'] = randomize.title()
		return "node_choose_background_personality"
	else:
		caller.ndb.charactersheet['special'] = raw_string.title()
		return "node_choose_background_personality"


def node_choose_background_personality(caller):
	text = "Choose one of the following for your personality trait:"
	option_list = []

	for key, value in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['personality trait'].items():
		option_list.append({'key': value, 'goto': _set_backgroup_personality})
	option_list.append({'key': 'Randomize', 'goto': _set_backgroup_personality})

	options = tuple(option_list)

	return text, options


def _set_backgroup_personality(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string == 'randomize':
		roll = randint(1, len(bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['personality trait']))
		randomize = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['personality trait'][roll]
		caller.ndb.charactersheet['personality trait'] = randomize.title()
		caller.msg(caller.ndb.charactersheet['personality trait'])
		return "node_choose_background_ideal"
	else:
		caller.ndb.charactersheet['personality trait'] = raw_string.title()
		return "node_choose_background_ideal"


def node_choose_background_ideal(caller):
	text = "Choose one of the following for your ideal:"
	option_list = []

	for key, value in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['ideal'].items():
		option_list.append({'key': value, 'goto': _set_backgroup_ideal})
	option_list.append({'key': 'Randomize', 'goto': _set_backgroup_ideal})

	options = tuple(option_list)

	return text, options


def _set_backgroup_ideal(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string == 'randomize':
		roll = randint(1, len(bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['ideal']))
		randomize = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['ideal'][roll]
		caller.ndb.charactersheet['ideal'] = randomize.title()
		caller.msg(caller.ndb.charactersheet['ideal'])
		return "node_choose_background_bond"
	else:
		caller.ndb.charactersheet['ideal'] = raw_string.title()
		return "node_choose_background_bond"


def node_choose_background_bond(caller):
	text = "Choose one of the following for your bond:"
	option_list = []

	for key, value in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['bond'].items():
		option_list.append({'key': value, 'goto': _set_backgroup_bond})
	option_list.append({'key': 'Randomize', 'goto': _set_backgroup_bond})

	options = tuple(option_list)

	return text, options


def _set_backgroup_bond(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string == 'randomize':
		roll = randint(1, len(bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['bond']))
		randomize = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['bond'][roll]
		caller.ndb.charactersheet['bond'] = randomize.title()
		caller.msg(caller.ndb.charactersheet['bond'])
		return "node_choose_background_flaw"
	else:
		caller.ndb.charactersheet['bond'] = raw_string.title()
		return "node_choose_background_flaw"


def node_choose_background_flaw(caller):
	text = "Choose one of the following for your flaw:"
	option_list = []

	for key, value in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['flaw'].items():
		option_list.append({'key': value, 'goto': _set_backgroup_flaw})
	option_list.append({'key': 'Randomize', 'goto': _set_backgroup_flaw})

	options = tuple(option_list)

	return text, options


def _set_backgroup_flaw(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string == 'randomize':
		roll = randint(1, len(bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['flaw']))
		randomize = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['flaw'][roll]
		caller.ndb.charactersheet['flaw'] = randomize.title()
		caller.msg(caller.ndb.charactersheet['flaw'])
	else:
		caller.ndb.charactersheet['flaw'] = raw_string.title()

	if bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['languages']:
		caller.ndb.language_picks = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['languages'][0]
		return "node_choose_background_languages"
	elif bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['proficiences']:
		caller.ndb.proficiences_picks = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['proficiences'][0]
		return "node_choose_background_proficiences"


def node_choose_background_languages(caller):
	text = "Your background grants you additional languages to learn. Choose one of the following languages:"
	option_list = []

	for language in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['languages'][1]:
		option_list.append({'key': language, 'goto': _set_backgroup_languages})

	options = tuple(option_list)

	return text, options


def _set_backgroup_languages(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string in caller.ndb.charactersheet['languages']:
		caller.msg("\nYou already know that language. Choose another.\n")
		return "node_choose_background_languages"

	caller.ndb.charactersheet['languages'].append(raw_string)
	bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['languages'][1].remove(raw_string)
	caller.ndb.language_picks = caller.ndb.language_picks - 1

	if caller.ndb.language_picks >= 1:
		return "node_choose_background_languages"
	else:
		if bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['proficiences']:
			caller.ndb.proficiences_picks = bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['proficiences'][0]
			return "node_choose_background_proficiences"
		return "node_choose_background_personality"


def node_choose_background_proficiences(caller):
	text = "Your background grants you additional proficiences. Choose one of the following proficiences:"
	option_list = []

	for proficiency in bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['proficiences'][1]:
		option_list.append({'key': proficiency, 'goto': _set_backgroup_proficiences})

	options = tuple(option_list)

	return text, options


def _set_backgroup_proficiences(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string in caller.ndb.charactersheet['proficiences']:
		caller.msg("\nYou already know that proficiency. Choose another.\n")
		return "node_choose_background_proficiences"

	caller.ndb.charactersheet['proficiences'].append(raw_string)
	bl.CHARACTER_BACKGROUNDS[caller.ndb.charactersheet['background']]['proficiences'][1].remove(raw_string)
	caller.ndb.proficiences_picks = caller.ndb.proficiences_picks - 1

	if caller.ndb.proficiences_picks >= 1:
		return "node_choose_background_proficiences"
	else:
		return "node_choose_skills"


def node_choose_profession(caller):
	text = \
	"""
The following classes are available:

Barbarian - A fierce warrior of primitive background who can enter a battle rage.
Bard - An inspiring magician whoes power echoes the music of creation.
Cleric - A priestly champion who wields divine magic in service of a higher power.
Druid - A priest of the old faith, wielding the powers of nature and adopting animal form.
Fighter - A master of martial combat, skilled with a variety of weapons and armor.
Paladin - A holy warrior bond to a sacred oath.
Ranger - A warrior who combats threats on the edge of civilization.
Rogue - A scoundrel who uses stealth and trickery to overcome obstacles and enemies.
Sorcerer - A spellcaster who draws on inherent magic from a gift or bloodline.
Warlock - A wielder of magic that is derived from a bargain with an extraplanar entity.
Wizard - A scholarly magic-user capable of manipulating the structures of reality.

What class will you choose?
	"""
	options = ({'key': '_default',
				"goto": _set_profession})

	return text, options


def _set_profession(caller, raw_string, **kwargs):
	classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk',
			   'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']

	raw_string = raw_string.lower().strip()

	if raw_string in classes:
		caller.ndb.charactersheet['profession'] = raw_string
		caller.msg("You set your class to |w{}|n!\n".format(raw_string.title()))
		caller.msg("Your current race is |w%s|n and your current class is |w%s|n.\n" %
				   (caller.ndb.charactersheet['race'], caller.ndb.charactersheet['profession']))

		# Let's preload some variables so when we re-edit selection of skills, we don't reset the skills to zero
		if not caller.nattributes.has('skills_available'):
			caller.ndb.skills_available = []

		if not caller.nattributes.has('skill_count'):
			caller.ndb.skill_count = 0

		# Now let's do the selection of skills. Each class has it's own set of skills and how many they can pick
		if raw_string == 'barbarian':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"animal handling": [False, "wis"], "athletics": [False, "str"],
										   "intimidation": [False, "cha"], "nature": [False, "int"],
										   "perception": [False, "wis"], "survival": [False, "wis"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_BARBARIAN['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_BARBARIAN['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_BARBARIAN['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_BARBARIAN['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_BARBARIAN['saving_throw']
		elif raw_string == 'bard':
			caller.ndb.skill_count = 3
			caller.ndb.skills_available = {"acrobatics": [False, "dex"], "animal handling": [False, "wis"],
										   "arcana": [False, "int"],
										   "athletics": [False, "str"], "deception": [False, "cha"],
										   "history": [False, "int"],
										   "insight": [False, "wis"], "intimidation": [False, "cha"],
										   "investigation": [False, "int"],
										   "medicine": [False, "wis"], "nature": [False, "int"],
										   "perception": [False, "wis"], "persuasion": [False, "cha"],
										   "performance": [False, "cha"], "religion": [False, "int"],
										   "sleight of hand": [False, "dex"],
										   "stealth": [False, "dex"], "survival": [False, "wis"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_BARD['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_BARD['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_BARD['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_BARD['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_BARD['saving_throw']
		elif raw_string == 'cleric':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"history": [False, "int"], "insight": [False, "wis"], "medicine": [False, "wis"],
										   "persuasion": [False, "cha"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_CLERIC['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_CLERIC['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_CLERIC['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_CLERIC['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_CLERIC['saving_throw']
		elif raw_string == 'druid':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"animal handling": [False, "wis"], "arcana": [False, "int"],
										   "insight": [False, "wis"], "medicine": [False, "wis"],
										   "nature": [False, "int"], "perception": [False, "wis"],
										   "religion": [False, "int"], "survival": [False, "wis"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_DRUID['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_DRUID['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_DRUID['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_DRUID['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_DRUID['saving_throw']
		elif raw_string == 'fighter':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"acrobatics": [False, "dex"], "animal handling": [False, "wis"],
										   "athletics": [False, "str"], "history": [False, "int"],
										   "insight": [False, "wis"], "intimidation": [False, "cha"],
										   "perception": [False, "wis"], "survival": [False, "wis"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_FIGHTER['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_FIGHTER['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_FIGHTER['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_FIGHTER['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_FIGHTER['saving_throw']

			# Fighters get to choose a fighting style.
			caller.ndb.feature_list = [['archery', 'trait'],
									   ['defense', 'trait'],
									   ['dueling', 'trait'],
									   ['great weapon fighting', 'trait'],
									   ['protection', 'trait'],
									   ['two-weapon fighting', 'trait']]

			caller.ndb.feature_text = \
"""
Fighters get the feature '|wFighting Style|n' that allows them to choose one of the following styles.

	|wArchery|n: +2 towards archery attack rolls.
	|wDefense|n: +1 towards AC while wearing armor.
	|wDueling|n: +2 towards damage while wielding only one weapon.
	|wGreat Weapon Fighting|n: Reroll attack rolls that result in a 1 or 2.
	|wProtection|n: Give an attacker disadvantage on their attack roll if you protect a creature within 5 feet of you.
	|wTwo-Weapon Fighting|n: Add your ability modifier to damage with all two-weapon fighting.

What is your choice?	
"""
			caller.ndb.feature_picks = 1
			caller.ndb.next_node = "node_choose_attributes"
			return "node_choose_feature"
		elif raw_string == 'paladin':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"medicine": [False, "wis"], "persuasion": [False, "cha"],
										   "athletics": [False, "str"], "religion": [False, "int"],
										   "insight": [False, "wis"], "intimidation": [False, "cha"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_PALADIN['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_PALADIN['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_PALADIN['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_PALADIN['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_PALADIN['saving_throw']
		elif raw_string == 'ranger':
			caller.ndb.skill_count = 3
			caller.ndb.skills_available = {"animal handling": [False, "wis"], "athletics": [False, "str"],
										   "insight": [False, "wis"], "investigation": [False, "int"],
										   "nature": [False, "int"], "perception": [False, "wis"],
										   "stealth": [False, "dex"], "survival": [False, "wis"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_RANGER['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_RANGER['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_RANGER['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_RANGER['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_RANGER['saving_throw']

			# Fighters get to choose a fighting style.
			caller.ndb.feature_list = [['aberrations', 'trait'],
									   ['beasts', 'trait'],
									   ['celestiais', 'trait'],
									   ['constructs', 'trait'],
									   ['dragons', 'trait'],
									   ['elementals', 'trait'],
									   ['fey', 'trait'],
									   ['fiends', 'trait'],
									   ['giants', 'trait'],
									   ['humanoid', 'trait'],
									   ['monstrosities', 'trait'],
									   ['oozes', 'trait'],
									   ['plants', 'trait'],
									   ['undead', 'trait']]

			caller.ndb.feature_text = \
"""
Rangers get the feature '|wFavored Enemy|n' that gives you have significant experience 
studying, tracking, hunting, and even talking to a certain type of enemy. Choosing a favored enemy
will add the enemy to your traits and also add the associated language to your languages.

What is your choice?	
"""
			caller.ndb.feature_picks = 1
			caller.ndb.next_node = "node_choose_attributes"
			return "node_choose_feature"
		elif raw_string == 'rogue':
			caller.ndb.skill_count = 4
			caller.ndb.skills_available = {"acrobatics": [False, "dex"], "athletics": [False, "str"],
										   "deception": [False, "cha"], "investigation": [False, "int"],
										   "insight": [False, "wis"], "intimidation": [False, "cha"],
										   "perception": [False, "wis"], "persuasion": [False, "cha"],
										   "performance": [False, "cha"], "sleight of hand": [False, "dex"],
										   "stealth": [False, "dex"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_ROGUE['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_ROGUE['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_ROGUE['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_ROGUE['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_ROGUE['saving_throw']
		elif raw_string == 'sorcerer':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"arcana": [False, "int"], "deception": [False, "cha"],
										   "insight": [False, "wis"], "intimidation": [False, "cha"],
										   "persuasion": [False, "cha"], "religion": [False, "int"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_SORCERER['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_SORCERER['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_SORCERER['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_SORCERER['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_SORCERER['saving_throw']
		elif raw_string == 'warlock':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"arcana": [False, "int"], "deception": [False, "cha"],
										   "history": [False, "int"], "intimidation": [False, "cha"],
										   "investigation": [False, "int"], "religion": [False, "int"],
										   "nature": [False, "int"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_WARLOCK['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_WARLOCK['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_WARLOCK['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_WARLOCK['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_WARLOCK['saving_throw']
		elif raw_string == 'wizard':
			caller.ndb.skill_count = 2
			caller.ndb.skills_available = {"arcana": [False, "int"], "history": [False, "int"],
										   "insight": [False, "wis"], "investigation": [False, "int"],
										   "medicine": [False, "wis"], "religion": [False, "int"]}
			caller.ndb.charactersheet['hit_dice'] = pr.PROFESSION_WIZARD['hit_dice']
			caller.ndb.charactersheet['proficiences'] = pr.PROFESSION_WIZARD['proficiences']
			caller.ndb.charactersheet['actions'] = pr.PROFESSION_WIZARD['actions']
			caller.ndb.charactersheet['traits'] = caller.ndb.charactersheet['traits'] + pr.PROFESSION_WIZARD['traits']
			caller.ndb.charactersheet['saving_throw'] = pr.PROFESSION_WIZARD['saving_throw']

		return "node_choose_attributes"
	else:
		caller.msg("That is not a valid profession. Please pick again.")
		return "node_chose_profession"


def node_choose_feature(caller):
	""" Choose Feature Node

	Some features require a choice to be made such as Fighting Style for Fighters. The feature has a number
	of different fighting styles to choose from that a player must choose. This node helps receive a list
	of those options from the feature along with the name of the option and whether or not it's an action
	or trait to the character profile.

	:var feature_list: [['archery', 'trait'], ['defense', 'trait'],...]
	:var text: string of text to display to caller when choosing feature.
	:return: text, options to select by caller
	"""
	option_list = []
	feature_list = caller.ndb.feature_list
	text = caller.ndb.feature_text

	# {"fighting style": ["archery", "action"]}
	for feature in feature_list:
		option_list.append({'key': feature[0].title(), 'goto': (_set_feature, {"feature": (feature[0], feature[1])})})

	options = tuple(option_list)

	return text, options


def _set_feature(caller, raw_string, **kwargs):
	feature_name, feature_value = kwargs.get("feature", (None, None))

	if [feature_name, feature_value] not in caller.ndb.feature_list:
		caller.msg("Sorry, we could not find that option.")
		return node_choose_feature

	if feature_value == 'action':
		caller.ndb.charactersheet['actions'].append(feature_name)
		caller.ndb.feature_picks = caller.ndb.feature_picks - 1
	elif feature_value == 'expertise':
		caller.ndb.charactersheet['expertise'].append(feature_name)
		caller.ndb.feature_picks = caller.ndb.feature_picks - 1
	elif feature_value == 'trait':
		caller.ndb.charactersheet['traits'].append(feature_name)
		caller.ndb.feature_picks = caller.ndb.feature_picks - 1

	# Remove our selected feature from our list in the event you can pick more than one
	for feature in caller.ndb.feature_list:
		if feature == [feature_name, feature_value]:
			del caller.ndb.feature_list[caller.ndb.feature_list.index(feature)]

	# Repeat if picks not done, else move onto next node
	if caller.ndb.feature_picks >= 1:
		return "node_choose_feature"
	else:
		return caller.ndb.next_node


def node_choose_skills(caller):
	text = \
"""
You can select %d skill(s) from the skill list below for your %s.
""" % (caller.ndb.skill_count, caller.ndb.charactersheet['profession'].title())

	option_list = []
	chosen_skills = []

	for skill in caller.ndb.skills_available:
		if not caller.ndb.skills_available[skill][0]:
			option_list.append({'key': skill.title(), 'goto': _set_skill})
		else:
			chosen_skills.append(skill)

	if chosen_skills:
		text = text + '\n\nYou have chosen the following skills: ' + ', '.join(chosen_skills)

	options = tuple(option_list)

	return text, options


def _set_skill(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	# Reset skill back to false if they select the skill again so they can repick the skill
	if caller.ndb.skills_available[raw_string][0]:
		caller.msg("You have chosen to deselect |w%s|n as a chosen skill." % raw_string)
		caller.ndb.skills_available[raw_string][0] = False
		caller.ndb.skill_count = caller.ndb.skill_count + 1
		return "node_choose_skills"

	# If the skill is false already, then let's pick the skill and update our skill_count
	caller.ndb.skills_available[raw_string][0] = True
	caller.ndb.skill_count = caller.ndb.skill_count - 1

	# When the skill_count reaches 0, we are done picking skills and should move on
	if caller.ndb.skill_count == 0:
		caller.ndb.charactersheet['skills'] = {"acrobatics": [False, "dex"], "animal handling": [False, "wis"],
											   "arcana": [False, "int"],
											   "athletics": [False, "str"], "deception": [False, "cha"],
											   "history": [False, "int"],
											   "insight": [False, "wis"], "intimidation": [False, "cha"],
											   "investigation": [False, "int"],
											   "medicine": [False, "wis"], "nature": [False, "int"],
											   "perception": [False, "wis"],
											   "performance": [False, "cha"], "persuasion": [False, "cha"],
											   "religion": [False, "int"],
											   "sleight of hand": [False, "dex"], "stealth": [False, "dex"],
											   "survival": [False, "wis"]}

		# Set our skill proficiences
		for skill in caller.ndb.skills_available:
			if caller.ndb.skills_available[skill][0]:
				caller.ndb.charactersheet['skills'][skill][0] = caller.ndb.skills_available[skill][0]

		# Rogues get to set Expertise in skills or tools that they are proficient in
		if caller.ndb.charactersheet['profession'] == 'rogue':
			caller.ndb.feature_list = []
			caller.ndb.feature_picks = 2
			caller.ndb.charactersheet['expertise'] = []
			caller.ndb.feature_text = \
"""
Rogues get the feature '|wExpertise|n' where your existing proficiency bonus is doubled for any ability check you 
make that uses either of the chosen proficiencies. This applies for skill proficiencies you chosen as well tools
like Thieves' Tools.

You can pick two. What is your choice?	
"""

			# Append our skills that we are proficient in
			for key, value in caller.ndb.charactersheet['skills'].items():
				# If proficient in the skill
				if value[0]:
					caller.ndb.feature_list.append([key, 'expertise'])

			# Append our additional proficiences
			if caller.ndb.charactersheet['proficiences']:
				for feature in caller.ndb.charactersheet['proficiences']:
					caller.ndb.feature_list.append([feature, 'expertise'])

			caller.ndb.next_node = "node_choose_age"
			return "node_choose_feature"
		return "node_choose_age"
	else:
		return "node_choose_skills"


def node_choose_age(caller):
	text = """How old are you? Pick between ages 13 and 90 years old."""

	options = ({'key': '_default',
				"goto": _set_age})

	return text, options


def _set_age(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	if raw_string.isnumeric():
		if 13 <= int(raw_string) <= 90:
			caller.ndb.charactersheet['age'] = int(raw_string)
			return "node_choose_sex"
		else:
			caller.msg("That is not a valid age between 13 and 90 years of age.")
			return "node_choose_age"
	else:
		caller.msg("That is not a valid number.")
		return "node_choose_age"


def node_choose_sex(caller):
	text = """What is your sex?"""

	options = ({'key': 'Male',
				"goto": _set_sex},
			   {'key': 'Female',
				"goto": _set_sex},
			   {'key': 'Neutral',
				"goto": _set_sex})

	return text, options


def _set_sex(caller, raw_string, **kwargs):
	raw_string = raw_string.lower().strip()

	caller.ndb.charactersheet['sex'] = raw_string
	return "node_choose_short_description"


def node_choose_short_description(caller):
	text = \
"""
Please select a short description for your character. This is the name of which other players you meet on your
journey will see you as until you introduce yourself. Keep this description short and descriptive about your character.
Try not to lead the looker on with things like ugly, pretty, attractive, etc. Try not to also describe feelings like
happy, sad, depressed, and so on. Keep to the facts of your character like short, tall, blonde, blind-eye, etc. You
can always change this later if you are not happy with the results or if your character appearance changes.

	Example: a short petite fellow, a tall tanned elf, a short green goblin
"""

	options = ({'key': '_default',
				"goto": _set_short_description})

	return text, options


def _set_short_description(caller, raw_string, **kwargs):
	_RE_FLAGS = re.MULTILINE + re.IGNORECASE + re.UNICODE
	_RE_CHAREND = re.compile(r"\W+$", _RE_FLAGS)
	raw_string = _RE_CHAREND.sub("", raw_string)
	cleaned_sdesc = ansi.strip_ansi(raw_string)

	if not cleaned_sdesc:
		caller.msg("Short description cannot be empty.")
		return "node_choose_short_description"

	if len(cleaned_sdesc) > 60:
		caller.msg("Short description too long. Keep it under 60 characters.")
		return "node_choose_short_description"

	caller.ndb.charactersheet['sdec'] = cleaned_sdesc
	return "node_choose_first_name"


def node_choose_first_name(caller):
	text = \
"""
Please select a first name. This will not be showed to players until you introduce yourself to them. Keep names
under 20 characters long.
"""

	options = ({'key': '_default',
				"goto": _set_first_name})

	return text, options


def _set_first_name(caller, raw_string, **kwargs):
	_RE_FLAGS = re.MULTILINE + re.IGNORECASE + re.UNICODE
	_RE_CHAREND = re.compile(r"\W+$", _RE_FLAGS)
	raw_string = _RE_CHAREND.sub("", raw_string)
	cleaned_first_name = ansi.strip_ansi(raw_string)

	if not cleaned_first_name:
		caller.msg("First name cannot be empty.")
		return "node_choose_first_name"

	if len(cleaned_first_name) > 20:
		caller.msg("First name too long. Keep it under 60 characters.")
		return "node_choose_first_name"

	caller.ndb.charactersheet['first_name'] = cleaned_first_name
	return "node_choose_last_name"


def node_choose_last_name(caller):
	text = \
"""
Please select a last name. If you do not want a last name, simply type, '|wNone|n'.
"""

	options = ({'key': '_default',
				"goto": _set_last_name})

	return text, options


def _set_last_name(caller, raw_string, **kwargs):
	_RE_FLAGS = re.MULTILINE + re.IGNORECASE + re.UNICODE
	_RE_CHAREND = re.compile(r"\W+$", _RE_FLAGS)
	raw_string = _RE_CHAREND.sub("", raw_string)
	cleaned_last_name = ansi.strip_ansi(raw_string)

	if cleaned_last_name == 'none':
		caller.msg("Ignoring last name.")
		caller.ndb.charactersheet['last_name'] = None
		return

	if not cleaned_last_name:
		caller.msg("Last name cannot be empty.")
		return "node_choose_last_name"

	if len(cleaned_last_name) > 20:
		caller.msg("Last name too long. Keep it under 60 characters.")
		return "node_choose_last_name"

	caller.ndb.charactersheet['last_name'] = cleaned_last_name
	return "node_character_overview"


def node_character_overview(caller):
	caller.ndb.charactersheet['attributes'] = caller.ndb.attributes

	# Combine our attribute bonuses to our attributes
	if caller.ndb.charactersheet['ability_score']:
		for bonus in caller.ndb.charactersheet['ability_score']:
			caller.ndb.charactersheet['attributes'][bonus] = caller.ndb.charactersheet['attributes'][bonus] + \
															 caller.ndb.charactersheet['ability_score'][bonus]

	# Calculate passive perception with proficiency
	if caller.ndb.charactersheet['skills']['perception'][0]:
		passive_perception = util.calculate_attribute_bonus(caller.ndb.charactersheet['attributes']['wis']) + \
							 util.calculate_proficiency_bonus(caller.db.level) + 10
	else:
		passive_perception = util.calculate_attribute_bonus(caller.ndb.charactersheet['attributes']['wis']) + 10

	# Factor in expertise in perception
	if caller.ndb.charactersheet['profession'] == 'rogue' and 'perception' in caller.ndb.charactersheet['expertise']:
		passive_perception = passive_perception + util.calculate_proficiency_bonus(caller.db.level)

	table = evtable.EvTable("|wStat|n", "|wValue|n", border=None)
	table.add_row("|wFirst|n:", caller.ndb.charactersheet['first_name'].title())
	table.add_row("|wLast|n:", caller.ndb.charactersheet['last_name'].title())
	table.add_row("|wAge|n:", caller.ndb.charactersheet['age'])
	table.add_row("|wSex|n:", caller.ndb.charactersheet['sex'].title())
	table.add_row("|wSize|n:", caller.ndb.charactersheet['size'].title())
	table.add_row("|wRace|n:", caller.ndb.charactersheet['race'].title())
	table.add_row("|wClass|n:", caller.ndb.charactersheet['profession'].title())
	table.add_row("|wHit Die|n:", caller.ndb.charactersheet['hit_dice'])
	table.add_row("|wInitiative |n:", util.calculate_attribute_bonus(caller.ndb.charactersheet['attributes']['dex']))
	table.add_row("|wPassive Perception|n:", passive_perception)
	table.add_row("|wLanguages|n:", ', '.join(caller.ndb.charactersheet['languages']).title())

	text = str(table) + "\n"

	# Attribute Block
	table = evtable.EvTable("|wAttributes|n", "|wValue|n", "|wMod|n", "|wSaves|n", border=None)
	attr_names = {"str": "|wStrength|n:", "dex": "|wDexterity|n:", "con": "|wConstitution|n:",
				  "int": "|wIntelligence|n:", "wis": "|wWisdom|n:", "cha": "|wCharisma|n:"}

	for stat, value in caller.ndb.charactersheet['attributes'].items():
		mod = util.calculate_attribute_bonus(value)
		saves = caller.ndb.charactersheet['saving_throw'][stat]
		table.add_row(attr_names[stat], value, mod, saves)

	text = text + "\n" + str(table) + "\n"

	# Skill Block
	table = evtable.EvTable("|wSkill|n", "|wModifier|n", "|wProficiency|n", border=None)

	for key, value in caller.ndb.charactersheet['skills'].items():
		stat = value[1]
		mod = util.calculate_attribute_bonus(caller.ndb.charactersheet['attributes'][stat])
		bonus = util.calculate_proficiency_bonus(caller.db.level)

		# Add proficiency bonus
		if value[0]:
			mod = mod + bonus

		# Add expertise bonus
		if caller.ndb.charactersheet['profession'] == 'rogue':
			if key in caller.ndb.charactersheet['expertise']:
				mod = mod + bonus

		table.add_row('|w' + key.title() + '|n:', mod, value[0])

	text = text + "\n" + str(table) + "\n"
	text = text + '\n |wActions |n(|wAbilities|n): ' + ', '.join(caller.ndb.charactersheet['actions']).title()
	text = text + '\n |wTraits |n(|wpassive perks|n): ' + ', '.join(caller.ndb.charactersheet['traits']).title()
	text = text + '\n |wProficiences |n(|warmor, weapons, tools|n): ' + ', '.join(caller.ndb.charactersheet['proficiences']).title()
	try:
		text = text + '\n |wExpertise |n(|warmor, weapons, tools|n): ' + ', '.join(caller.ndb.charactersheet['expertise']).title()
	except:
		pass

	# Skill Block
	table = evtable.EvTable("|wBackground|n", "|wValue|n", border=None)
	try:
		table.add_row("|w%s" % caller.ndb.charactersheet['special_name'] + "|n:",
					  caller.ndb.charactersheet['special'])
	except:
		pass
	table.add_row("|wPersonality|n:", caller.ndb.charactersheet['personality trait'])
	table.add_row("|wIdeal|n:", caller.ndb.charactersheet['ideal'])
	table.add_row("|wBond|n:", caller.ndb.charactersheet['bond'])
	table.add_row("|wFlaw|n:", caller.ndb.charactersheet['flaw'])
	text = text + "\n\n" + str(table) + "\n"

	options = ({'key': 'Confirm',
				"goto": _set_last_name},
			   {'key': 'Start Over',
				"goto": "node_choose_race"},
			   {'key': 'Change First Name',
				"goto": "node_choose_first_name"},
			   {'key': 'Change Last Name',
				"goto": "node_choose_last_name"},
			   {'key': 'Change Age',
				"goto": "node_choose_age"},
			   {'key': 'Change Sex',
				"goto": "node_choose_sex"},
			   {'key': 'Change Short Description',
				"goto": "node_choose_short_description"})

	return text, options
