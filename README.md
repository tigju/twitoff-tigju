# twitoff-tigju

# Installation

```sh
git clone https://github.com/tigju/twitoff-tigju.git
cd twitoff-tigju/
```

# Setup 

```sh
pipenv install
```
Migrate the database:

```sh
flask db init
flask db migrate
flask db update
```

# Usage 

```sh
# Mac:
FLASK_APP=app  flask run

# Windows:
export FLASK_APP=app # one-time thing, to set the env var
flask run
```