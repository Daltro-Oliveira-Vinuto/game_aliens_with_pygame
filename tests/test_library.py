import pytest
import sys
import os

real_path = os.path.realpath(__file__)
current_directory = os.path.dirname(real_path)
parent_directory = os.path.dirname(current_directory)

sys.path.append(parent_directory+"/source")

from library import Position, Directions, Keyboard

def test_class_position():
	p1 = Position(3,4)
	assert p1.pos_x == 3
	assert p1.pos_y == 4

	p1.pos_x = 10
	p1.pos_y = 20
	assert p1.pos_x == 10
	assert p1.pos_y == 20

	assert p1.__str__() == "(10, 20)"


def test_class_direction():
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

	assert d1.__str__() == "(left=False, right=False, up=True, down=True)"

def test_class_keyboard():
	d0 = Directions(False,False,False,False)
	k0 = Keyboard(d0)
	assert k0.state == False
	assert k0.get_real_state() == False
	k0.state = True
	assert k0.state == True
	assert k0.get_real_state() == True
	assert k0.__str__() == d0.__str__()+", state=True"


	d_list = [Directions(True, False, False, False),
			Directions(False, True, False, False),
			Directions(False, False, True, False),
			Directions(False, False, False, True)]
	for i in range(0,4,1):
		k1 = None
		k1 = Keyboard(d_list[i])
		assert k1.get_real_state() == True
		assert k1.state == True
		k1.state = False
		assert k1.state == False
		assert k1.get_real_state() == True



