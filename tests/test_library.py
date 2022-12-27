import pytest
import sys
import os

real_path = os.path.realpath(__file__)
current_directory = os.path.dirname(real_path)
parent_directory = os.path.dirname(current_directory)

sys.path.append(parent_directory+"/source")

from library import Position, Directions, Keyboard

def test_position_class_setters_and_getters():
	p1 = Position(3,4)
	assert p1.pos_x == 3
	assert p1.pos_y == 4

	p1.pos_x = 10
	p1.pos_y = 20
	assert p1.pos_x == 10
	assert p1.pos_y == 20


def test_directions_class_setters_and_getters():
	d1 = Directions(left=True,right=True,upp=False,down=False)

	assert d1.left == True
	assert d1.right == True
	assert d1.upp == False
	assert d1.down == False

	d1.left = False
	d1.right = False
	d1.upp = True
	d1.down = True

	assert d1.left == False
	assert d1.right == False
	assert d1.upp == True
	assert d1.down == True

