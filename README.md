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
flask db upgrade
```
if adding new table or db afer removal of existing:
```sh
flask db revision --rev-id 30dc7f6b846a # your revision id
flask db migrate
flask db upgrade
```
# Usage 

```sh
# Mac:
FLASK_APP=app  flask run

# Windows:
set FLASK_APP=app # one-time thing, to set the env var
flask run
```