# Local Security Lab Setup

## Requirements
- Python 3.11 or newer
- pip
- GitHub account

## Installation

1. Download or clone this repository.
2. Open the project folder.
3. Create a virtual environment:

python -m venv .venv

4. Activate the environment.

Windows:
.venv\Scripts\activate

Linux/macOS:
source .venv/bin/activate

5. Install dependencies:

pip install -r requirements.txt

## Run Application

python -m flask --app app run --host 127.0.0.1 --port 5000

Open:
http://127.0.0.1:5000

## Run Tests

pytest -q

## Safety
Run this educational lab locally only.
Do not test public websites without written permission.
