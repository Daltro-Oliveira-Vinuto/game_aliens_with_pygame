
all: test lint mypy

lint: source/aliens.py source/ships.py
	pylint source/aliens.py
	pylint source/ships.py
	pylint source/library.py

test:
	pytest -v 

mypy: source/ships.py source/aliens.py
	mypy source/ships.py
	mypy source/aliens.py
	mypy source/library.py

run:
	python source/aliens.py


