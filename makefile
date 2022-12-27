
all: test lint mypy

test:
	pytest -v 

lint:
	pylint source/aliens.py
	pylint source/ships.py
	pylint source/library.py

mypy:
	mypy source/ships.py
	mypy source/aliens.py
	mypy source/library.py


debug:
	python -m pdb source/aliens.py


run:
	python source/aliens.py