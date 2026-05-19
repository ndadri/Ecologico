# Variables para apuntar al entorno virtual en Windows
PYTHON = venv\Scripts\python.exe
PIP = venv\Scripts\pip.exe

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) app.py

clean-uploads:
	del /q app\static\uploads\*

freeze:
	$(PIP) freeze > requirements.txt