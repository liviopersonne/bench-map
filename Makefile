PYTHON := python3

create-venv:
	${PYTHON} -m venv venv
	source venv/bin/activate && pip install -r requirements.txt