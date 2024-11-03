default: requirements.txt
	python3.10 -m venv venv
	chmod u+x venv/bin/activate
	source venv/bin/activate && python -m pip install -r requirements.txt
