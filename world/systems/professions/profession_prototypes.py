PROFESSION_BARBARIAN = {
	"key": "barbarian",
	"hit_dice": 12,
	"proficiences": ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["rage"],
	"traits": ["unarmored defense"],
	"saving_throw": {'str': False, 'dex': False, 'con': False, 'int': False, 'wis': False, 'cha': False}
}

PROFESSION_BARD = {
	"key": "bard",
	"hit_dice": 8,
	"proficiences": ["light armor", "simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["bardic inspiration", "vicious mockery", "dancing lights", "cure wounds", "hideous laughter"],
	"traits": ["spellcasting"],
	"saving_throw": {'str': False, 'dex': True, 'con': False, 'int': False, 'wis': False, 'cha': True}
}

PROFESSION_CLERIC = {
	"key": "cleric",
	"hit_dice": 8,
	"proficiences": ["light armor", "medium armor", "shields", "simple weapons"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["cure wounds", "shield of faith", "guiding bolt", "spare the dying", "light", "guidance"],
	"traits": ["spellcasting"],
	"saving_throw": {'str': False, 'dex': False, 'con': False, 'int': False, 'wis': True, 'cha': True}
}

PROFESSION_DRUID = {
	"key": "druid",
	"hit_dice": 8,
	"proficiences": ["light armor", "medium armor", "shields", "clubs", "daggers", "darts", "javelins",
					 "maces", "quarlerstaffs", "scimitars", "sickles", "slings", "spears", "herbalism kit"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["cure wounds", "animal friendship", "poison spray", "produce flame"],
	"traits": ["druidic", "spellcasting"],
	"saving_throw": {'str': False, 'dex': False, 'con': False, 'int': True, 'wis': True, 'cha': False}
}

PROFESSION_FIGHTER = {
	"key": "fighter",
	"hit_dice": 10,
	"proficiences": ["light armor", "medium armor", "heavy armor", "shields", "simple weapons", "martial weapons"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["second wind"],
	"traits": [],
	"saving_throw": {'str': True, 'dex': False, 'con': True, 'int': False, 'wis': False, 'cha': False}
}

PROFESSION_PALADIN = {
	"key": "paladin",
	"hit_dice": 10,
	"proficiences": ["light armor", "medium armor", "heavy armor", "shields", "simple weapons", "martial weapons"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["divine sense", "lay on hands"],
	"traits": [],
	"saving_throw": {'str': False, 'dex': False, 'con': False, 'int': False, 'wis': True, 'cha': True}
}

PROFESSION_RANGER = {
	"key": "ranger",
	"hit_dice": 10,
	"proficiences": ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": [],
	"traits": [],
	"saving_throw": {'str': True, 'dex': True, 'con': False, 'int': False, 'wis': False, 'cha': False}
}

PROFESSION_ROGUE = {
	"key": "rogue",
	"hit_dice": 8,
	"proficiences": ["light armor", "simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords",
					 "thieves tools"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": [],
	"traits": ["sneak attack"],
	"saving_throw": {'str': False, 'dex': True, 'con': False, 'int': True, 'wis': False, 'cha': False}
}

PROFESSION_SORCERER = {
	"key": "sorcerer",
	"hit_dice": 6,
	"proficiences": ["simple weapons", "daggers", "darts", "slings", "quarterstaffs", "light crossbows"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["mage armor", "chaos bolt", "light", "thunderclap"],
	"traits": ["spellcasting"],
	"saving_throw": {'str': False, 'dex': False, 'con': True, 'int': False, 'wis': False, 'cha': True}
}

PROFESSION_WARLOCK = {
	"key": "warlock",
	"hit_dice": 8,
	"proficiences": ["light armor", "simple weapons"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["eldritch blast", "mage hand", "hellish rebuke", "protection from evil and good"],
	"traits": ["pact magic"],
	"saving_throw": {'str': False, 'dex': False, 'con': False, 'int': False, 'wis': True, 'cha': True}
}

PROFESSION_WIZARD = {
	"key": "wizard",
	"hit_dice": 6,
	"proficiences": ["simple weapons", "daggers", "darts", "slings", "quarterstaffs", "light crossbows"],
	"skills": {"acrobatics": [False, "dex"], "animal handling": [False, "wis"], "arcana": [False, "int"],
			   "athletics": [False, "str"], "deception": [False, "cha"], "history": [False, "int"],
			   "insight": [False, "wis"], "intimidation": [False, "cha"], "investigation": [False, "int"],
			   "medicine": [False, "wis"], "nature": [False, "int"], "perception": [False, "wis"],
			   "performance": [False, "cha"], "persuasion": [False, "cha"], "religion": [False, "int"],
			   "sleight of hand": [False, "dex"], "stealth": [False, "dex"], "survival": [False, "wis"]},
	"actions": ["light", "shocking grasp", "minor illusion", "mage armor", "magic missile"],
	"traits": ["spellcasting"],
	"saving_throw": {'str': False, 'dex': False, 'con': False, 'int': True, 'wis': True, 'cha': False}
}
