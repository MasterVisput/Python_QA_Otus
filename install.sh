FILE=otusenv/

if [ -d "$FILE" ]; then
    source otusenv/bin/activate &&
    pip install -U pip &&
    pip install -Ur requirements.txt
else
    python3 -m venv otusenv &&
    source otusenv/bin/activate &&
    pip install -U pip &&
    pip install -Ur requirements.txt
fi