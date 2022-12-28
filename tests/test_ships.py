
import os
import sys

real_path = os.path.realpath(__file__)
current_directory = os.path.dirname(real_path)
parent_directory = os.path.dirname(current_directory)

sys.path.append(parent_directory+"/source")

import ships
import library
from ships import Projectile, Ship
from library import Position

def test_class_projectiles(): # don't test draw() function because it need self.surface
	pos_x = 30
	pos_y = 40
	test_speed = 20
	test_image_path = "/"
	position0 = Position(pos_x, pos_y)
	p0 = Projectile(position0,None,test_image_path,speed=test_speed)
	assert p0.speed == test_speed
	assert p0.image_path == test_image_path

	assert p0.get_pos() == (pos_x, pos_y)
	assert p0.get_pos_x() == pos_x
	assert p0.get_pos_y() == pos_y

	p0.update_pos(Position(100,200))
	assert p0.get_pos() == (100,200)

	p0.speed = 1

	p0.update_pos(Position(0,0))
	p0.move_up()
	assert p0.get_pos() == (0,-1)

	p0.update_pos(Position(0,0))
	p0.move_down()
	assert p0.get_pos() == (0,1)

	p0.update_pos(Position(0,0))
	p0.move_right()
	assert p0.get_pos() == (1,0)

	p0.update_pos(Position(0,0))
	p0.move_left()
	assert p0.get_pos() == (-1,0)


def test_class_ships(): # don't test fire function because it need self.surface
	pos_x = 30
	pos_y = 40
	position0 = Position(pos_x, pos_y)
	test_speed = 100
	test_image_path = "abc"
	test_image_bullet_path = "zzz"
	s0 = Ship(position0, None, image_path=test_image_path,\
	 image_bullet_path=test_image_bullet_path, speed = test_speed)

	assert s0.get_pos() == (pos_x, pos_y)
	assert s0.speed == test_speed
	assert s0.image_path == test_image_path
	assert s0.image_bullet_path == test_image_bullet_path

	assert s0.bullets_fired == []

	# can't test fire() function because it need self.surface
	"""
	s0.fire()
	assert len(s0.bullets_fired) == 1
	assert type(s0.bullets_fired[0]) == Projectile
	"""
