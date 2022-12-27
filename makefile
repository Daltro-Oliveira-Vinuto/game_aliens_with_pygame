
all: test lint mypy

lint:
	pylint source/aliens.py
	pylint source/ships.py
	pylint source/library.py

test:
	pytest -v 

mypy:
	mypy source/ships.py
	mypy source/aliens.py
	mypy source/library.py

run:
	python source/aliens.py


debug:
	python -m pdb source/aliens.py

