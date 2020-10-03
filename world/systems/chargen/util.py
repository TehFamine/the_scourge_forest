import os
import subprocess
from random import randint
from math import floor, ceil


def roll_attribute():
	# 4d6 simulation where we drop the lowest value
	roll = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
	roll.remove(min(roll))
	return sum(roll)


def roll_all_attributes():
	attr = []

	for n in range(6):
		roll = roll_attribute()
		while roll < 9:
			roll = roll_attribute()
		attr.append(roll)
	return attr


def calculate_attribute_bonus(attribute):
	return floor((attribute-10) / 2)


def calculate_proficiency_bonus(level):
	return ceil(1 + (0.25 * level))
