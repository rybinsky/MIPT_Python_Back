PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS := venv/bin/pytest -v ./test_controllers.py

clear:
	rm -rf venv

venv:
	python3 -m venv venv

requirements:
	${PIP} install -r requirements.txt

setup:
	make clear
	make venv
	make requirements

run:
	${PYTHON3} server.py

test:
	${TESTS}

.PHONY: clear venv requirements setup run test