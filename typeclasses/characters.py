"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        self.db.flags = {'is_created': False}
        self.db.level = 1
        self.db.profession = 'Newbie'
        self.db.race = 'Clay'
        self.db.languages = []
        self.db.armor = 0
        self.db.saving_throws = {}
        self.db.damage_immunities = []
        self.db.damage_resistances = []
        self.db.condition_immunities = []
        self.db.condition_resistances = []
        self.db.experience = 0
        self.db.coin_purse = 0
        self.db.stats = {'hit_points': 0, 'max_hit_points': 0,
                         'mana_points': 0, 'max_mana_points': 0,
                         'move_points': 0, 'max_move_points': 0}
        self.db.attributes = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        # Tiny (2by2), Small (5by5), Medium (5by5), Large (10by10), Huge (15by15), Gargantuan (20by20)
        self.db.size = 'Tiny'
        self.db.skills = {}
        self.db.traits = []
        self.db.actions = {}
        self.db.legendary_actions = {}
        self.db.minions = []
    pass
