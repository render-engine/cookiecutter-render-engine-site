python -m pip install --user --upgrade pip
python -m venv .venv
source .venv/bin/activate
python -m pip install pip-tools
python -m piptools compile --upgrade -o requirements.txt requirements.in
python -m pip install -r requirements-dev.txt
