import world.systems.languages.language_lookups as lang

CHARACTER_BACKGROUNDS = {
	"acolyte":
		{"skills": {"insight": [True, "wis"], "religion": [True, "int"]},
		 "equiptment": [],
		 "proficiences": [],
		 "traits": [],
		 "languages": [2, lang.LANGUAGES['standard'] + lang.LANGUAGES['exotic']],
		 "belt_pouch": 1500,
		 "special": {},
		 "personality trait": {1: "I idolize a parlicular hero of my faith, and constantlly "
								  "refer to that person's deeds and example.",
							   2: "I can find common ground between the fiercest enemies, empathizing with them and "
								  "always working toward peace.",
							   3: "I see omens in every event and action. The gods try to speak to us, we just need"
								  "to listen.",
							   4: "Nothing can shake my optimistic attitude.",
							   5: "I quote (or misquote) sacred texts and proverbs in almost every situation.",
							   6: "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship "
								  "of other gods.",
							   7: "I've enjoyed fine food, drink, and high society among my temple's elite. "
								  "Rough living grates on me.",
							   8: "I've spent so long in the temple that I have little practical experience dealing "
								  "with people in the outside world."},
		 "ideal": {1: "Tradition. The ancient traditions of worship and sacrifice must be preserved "
					  "and upheld. (Lawful)",
				   2: "Charity. I always try to help those in need, no matter what the personal cost. (Good)",
				   3: "Change. We must help bring about the changes the gods are constantly working in the "
					  "world. (Chaotic)",
				   4: "Power. I hope to one day rise to the top of my faith's religious hierarchy. (Lawful)",
				   5: "Faith. I trust that my deity will guide my actions. I have faith that if I work hard, "
					  "things will go well. (Lawful)",
				   6: "Aspiration. I seek to prove myself worthy of my god's favor by matching my actions against his "
					  "or her teachings. (Any)"},
		 "bond": {1: "I would die to recover an ancient relic of my faith that was lost long ago.",
				  2: "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
				  3: "I owe my life to the priest who took me in when my parents died.",
				  4: "Everything I do is for the common people.",
				  5: "I will do anything to protect the temple where I served.",
				  6: "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy."},
		 "flaw": {1: "I judge others harshly, and myself even more severely.",
				  2: "I put too much trust in those who wield power within my temple's hierarchy.",
				  3: "My piety sometimes leads me to blindly trust those that profess faith in my god.",
				  4: "I am inflexible in my thinking.",
				  5: "I am suspicious of strangers and expect the worst of them.",
				  6: "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."}},

	"criminal":
		{"skills": {"deception": [True, "cha"], "stealth": [True, "dex"]},
		 "equiptment": [],
		 "languages": [],
		 "proficiences": [1, ["gaming set", "thieves tools"]],
		 "traits": ["criminal contact"],
		 "belt_pouch": 1500,
		 "special": {"name": "criminal specialty",
					 1: "Blackmailer",
					 2: "Burglar",
					 3: "Enforcer",
					 4: "Fence",
					 5: "Highway Robber",
					 6: "Hired Killer",
					 7: "Pickpocket",
					 8: "Smuggler"},
		 "personality trait": {1: "I always have a plan for when things go wrong.",
							   2: "I am always calm, no matter what the situation. I never raise my voice or let my "
								  "emotions control me.",
							   3: "The first thing I do in a new place is note the locations of everything "
								  "valuable-or where such things could be hidden.",
							   4: "I would rather make a new friend than a new enemy.",
							   5: "I am incredibly slow to trust. Those who seem the fairest often "
								  "have the most to hide.",
							   6: "I don't pay attention to the risks in a situation. Never tell me the odds.",
							   7: "The best way to get me to do something is to tell me I can't do it.",
							   8: "I blow up at the slightest insult."},
		 "ideal": {1: "Honor. I don't steal from others in the trade.",
				   2: "Freedom. Chains are meant to be broken, as are those who would forge them.",
				   3: "Charity. I steal from the wealthy so that I can help people in need.",
				   4: "Greed. I will do whatever it takes to become wealthy.",
				   5: "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the "
					  "Styx for all I care.",
				   6: "Redemption. There's a spark of good in everyone."},
		 "bond": {1: "I'm trying to pay off an old debt I owe to a generous benefactor.",
				  2: "My ill-gotten gains go to support my family",
				  3: "Something important was taken from me, and I aim to steal it back.",
				  4: "I will become the greatest thief that ever lived.",
				  5: "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
				  6: "Someone I loved died because of I mistake I made. That will never happen again."},
		 "flaw": {1: "When I see something valuable, I can't think about anything but how to steal it.",
				  2: "When faced with a choice between money and my friends, I usually choose the money.",
				  3: "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
				  4: "I have a 'tell' that reveals when I'm lying.",
				  5: "I turn tail and run when things look bad.",
				  6: "An innocent person is in prison for a crime that I committed. I'm okay with that."}},

	"folk hero":
		{"skills": {"animal handling": [True, "wis"], "survival": [True, "wis"]},
		 "equiptment": [],
		 "languages": [],
		 "proficiences": [1, ["artisans tools", "vehicles (land)"]],
		 "traits": ["rustic hospitality"],
		 "belt_pouch": 1000,
		 "special": {"name": "defining event",
					 1: "I stood up to a tyrant's agents",
					 2: "I saved people during a natural disaster.",
					 3: "I stood alone against a terrible monster.",
					 4: "I stole from a corrupt merchant to help the poor.",
					 5: "I led a militia to fight off an invading army.",
					 6: "I broke into a tyrant's castle and stole weapons to arm the people.",
					 7: "I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.",
					 8: "A lord rescinded an unpopular decree after I led a symbolic act of protect against it.",
					 9: "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
					 10: "Recruited into a lord's army, I rose to leadership and was commended for my heroism."},
		 "personality trait": {1: "I judge people by their actions, not their words.",
							   2: "If someone is in trouble, I'm always ready to lend help.",
							   3: "When I set my mind to something, I follow through no matter what gets in my way.",
							   4: "I have a strong sense of fair play and always try to find the most equitable "
								  "solution to arguments.",
							   5: "I'm confident in my own abilities and do what I can to instill confidence in others.",
							   6: "Thinking is for other people. I prefer action.",
							   7: "I misuse long words in an attempt to sound smarter.",
							   8: "I get bored easily. When am I going to get on with my destiny?"},
		 "ideal": {1: "Respect. People deserve to be treated with dignity and respect.",
				   2: "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
				   3: "Freedom. Tyrants must not be allowed to oppress the people.",
				   4: "Might. If I become strong, I can take what I want – what I deserve",
				   5: "Sincerity. There's no good in pretending to be something I'm not.",
				   6: "Destiny. Nothing and no one can steer me away from my higher calling."},
		 "bond": {1: "I have a family, but I have no idea where they are. One day, I hope to see them again.",
				  2: "I worked the land, I love the land, and I will protect the land.",
				  3: "A proud noble once gave me a horrible beating, and I will take my revenge on any bully "
					 "I encounter.",
				  4: "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
				  5: "I protect those who cannot protect themselves.",
				  6: "I wish my childhood sweetheart had come with me to pursue my destiny."},
		 "flaw": {1: "The tyrant who rules my land will stop at nothing to see me killed.",
				  2: "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk "
					 "of failure.",
				  3: "The people who knew me when I was young know my shameful secret, so I can never go home again.",
				  4: "I have a weakness for the vices of the city, especially hard drink.",
				  5: "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
				  6: "I have trouble trusting in my allies."}},

	"entertainer":
		{"skills": {"acrobatics": [True, "dex"], "performance": [True, "cha"]},
		 "equiptment": [],
		 "languages": [],
		 "proficiences": [1, ["bagpipes", "drum", "flute", "lute", "lyre", "horn", "pan flute", "shawm", "viol"]],
		 "traits": ["by popular demand"],
		 "belt_pouch": 1500,
		 "special": {"name": "entertainer routine",
					 1: "Actor",
					 2: "Dancer",
					 3: "Fire-eater",
					 4: "Jester",
					 5: "Juggler",
					 6: "Instrumentalist",
					 7: "Poet",
					 8: "Singer",
					 9: "Storyteller",
					 10: "Tumbler"},
		 "personality trait": {1: "I know a story relevant to almost every situation.",
							   2: "Whenever I come to a new place, I collect local rumors and spread gossip.",
							   3: "I'm a hopeless romantic, always searching for that 'special someone.'",
							   4: "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
							   5: "I love a good insult, even one directed at me.",
							   6: "I get bitter if I'm not the center of attention.",
							   7: "I'll settle for nothing less than perfection.",
							   8: "I change my mood or my mind as quickly as I change key in a song."},
		 "ideal": {1: "Beauty. When I perform, I make the world better than it was.",
				   2: "Tradition. The stories, legends, and songs of the past must never be forgotten, "
					  "for they teach us who we are.",
				   3: "Creativity. The world is in need of new ideas and bold action.",
				   4: "Greed. I'm only in it for the money and fame. (Evil)",
				   5: "People. I like seeing the smiles on people's faces when I perform. That's all that matters.",
				   6: "Honesty. Art should reflect the soul; it should come from within and reveal who we really are."},
		 "bond": {1: "My instrument is my most treasured possession, and it reminds me of someone I love.",
				  2: "Someone stole my precious instrument, and someday I'll get it back.",
				  3: "I want to be famous, whatever it takes.",
				  4: "I idolize a hero of the old tales and measure my deeds against that person's.",
				  5: "I will do anything to prove myself superior to my hated rival.",
				  6: "I would do anything for the other members of my old troupe."},
		 "flaw": {1: "I'll do anything to win fame and renown.",
				  2: "I'm a sucker for a pretty face.",
				  3: "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
				  4: "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
				  5: "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
				  6: "Despite my best efforts, I am unreliable to my friends."}},

	"folk hero":
		{"skills": {"animal handling": [True, "wis"], "survival": [True, "wis"]},
		 "equiptment": [],
		 "languages": [],
		 "proficiences": [1, ["artisans tools", "vehicles (land)"]],
		 "traits": ["rustic hospitality"],
		 "belt_pouch": 1000,
		 "special": {"name": "defining event",
					 1: "I stood up to a tyrant's agents",
					 2: "I saved people during a natural disaster.",
					 3: "I stood alone against a terrible monster.",
					 4: "I stole from a corrupt merchant to help the poor.",
					 5: "I led a militia to fight off an invading army.",
					 6: "I broke into a tyrant's castle and stole weapons to arm the people.",
					 7: "I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.",
					 8: "A lord rescinded an unpopular decree after I led a symbolic act of protect against it.",
					 9: "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
					 10: "Recruited into a lord's army, I rose to leadership and was commended for my heroism."},
		 "personality trait": {1: "I judge people by their actions, not their words.",
							   2: "If someone is in trouble, I'm always ready to lend help.",
							   3: "When I set my mind to something, I follow through no matter what gets in my way.",
							   4: "I have a strong sense of fair play and always try to find the most equitable "
								  "solution to arguments.",
							   5: "I'm confident in my own abilities and do what I can to instill confidence in others.",
							   6: "Thinking is for other people. I prefer action.",
							   7: "I misuse long words in an attempt to sound smarter.",
							   8: "I get bored easily. When am I going to get on with my destiny?"},
		 "ideal": {1: "Respect. People deserve to be treated with dignity and respect.",
				   2: "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
				   3: "Freedom. Tyrants must not be allowed to oppress the people.",
				   4: "Might. If I become strong, I can take what I want – what I deserve",
				   5: "Sincerity. There's no good in pretending to be something I'm not.",
				   6: "Destiny. Nothing and no one can steer me away from my higher calling."},
		 "bond": {1: "I have a family, but I have no idea where they are. One day, I hope to see them again.",
				  2: "I worked the land, I love the land, and I will protect the land.",
				  3: "A proud noble once gave me a horrible beating, and I will take my revenge on any bully "
					 "I encounter.",
				  4: "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
				  5: "I protect those who cannot protect themselves.",
				  6: "I wish my childhood sweetheart had come with me to pursue my destiny."},
		 "flaw": {1: "The tyrant who rules my land will stop at nothing to see me killed.",
				  2: "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk "
					 "of failure.",
				  3: "The people who knew me when I was young know my shameful secret, so I can never go home again.",
				  4: "I have a weakness for the vices of the city, especially hard drink.",
				  5: "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
				  6: "I have trouble trusting in my allies."}},

	"guild artisan":
		{"skills": {"persuasion": [True, "cha"], "insight": [True, "wis"]},
		 "equiptment": [],
		 "languages": [],
		 "proficiences": [1, ["tinkers tools", "masons tools", "jewelers tools", "brewers supplies",
							  "alchemists supplies", "smiths tools", "carpenters tools", "leatherworkers tools",
							  "cook’s utensils"]],
		 "traits": ["guild membership"],
		 "belt_pouch": 1500,
		 "special": {"name": "guild business",
					 1: "Alchemists and apothecaries",
					 2: "Armorers, locksmiths, and finesmiths",
					 3: "Brewers, distillers, and vintners",
					 4: "Carpenters, roofers, and plasterers",
					 5: "Cooks and bakers",
					 6: "Jewelers and gemcutters",
					 7: "Leatherworkers, skinners, and tanners",
					 8: "Masons and stonecutters",
					 9: "Smiths and metal-forgers",
					 10: "Tinkers, pewterers, and casters"},
		 "personality trait": {1: "I believe that anything worth doing is worth doing right. "
								  "I can't help it - I'm a perfectionist.",
							   2: "I'm a snob who looks down on those who can't appreciate fine art.",
							   3: "I always want to know how things work and what makes people tick.",
							   4: "I'm full of witty aphorisms and have a proverb for every occasion.",
							   5: "I'm rude to people who lack my commitment to hard work and fair play.",
							   6: "I like to talk at length about my profession.",
							   7: "I don't part with my money easily and will haggle tirelessly to "
								  "get the best deal possible.",
							   8: "I'm well known for my work, and I want to make sure everyone appreciates it. "
								  "I'm always taken aback when people haven't heard of me."},
		 "ideal": {1: "Community. It is the duty of all civilized people to strengthen the bonds of community "
					  "and the security of civilization.",
				   2: "Tradition. The stories, legends, and songs of the past must never be forgotten, "
					  "for they teach us who we are.",
				   3: "Creativity. The world is in need of new ideas and bold action.",
				   4: "Greed. I'm only in it for the money and fame. (Evil)",
				   5: "People. I like seeing the smiles on people's faces when I perform. That's all that matters.",
				   6: "Honesty. Art should reflect the soul; it should come from within and reveal who we really are."},
		 "bond": {1: "My instrument is my most treasured possession, and it reminds me of someone I love.",
				  2: "Someone stole my precious instrument, and someday I'll get it back.",
				  3: "I want to be famous, whatever it takes.",
				  4: "I idolize a hero of the old tales and measure my deeds against that person's.",
				  5: "I will do anything to prove myself superior to my hated rival.",
				  6: "I would do anything for the other members of my old troupe."},
		 "flaw": {1: "I'll do anything to win fame and renown.",
				  2: "I'm a sucker for a pretty face.",
				  3: "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
				  4: "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
				  5: "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
				  6: "Despite my best efforts, I am unreliable to my friends."}},
}
