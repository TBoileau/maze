freeze:
	./venv/Scripts/python -m pip freeze > requirements.txt

test:
	./venv/Scripts/python -m pytest

coding-style:
	./venv/Scripts/python -m flake8 ./src ./tests
	./venv/Scripts/python -m pydocstyle ./src
