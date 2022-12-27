import pytest
import sys
import os

real_path = os.path.realpath(__file__)
current_directory = os.path.dirname(real_path)
parent_directory = os.path.dirname(current_directory)

sys.path.append(parent_directory+"/source")

from library import Position

def test_position_class():
	p1 = Position(3,4)
	assert p1.pos_x == 3
	assert p1.pos_y == 4

	p1.pos_x = 10
	p1.pos_y = 20
	assert p1.pos_x == 10
	assert p1.pos_y == 20