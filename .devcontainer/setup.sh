python -m pip install --user --upgrade pip
python -m pip install --user pip-tools
python -m piptools compile --upgrade -o requirements.txt requirements.in
python -m pip install --user -r requirements.txt
