# Medlughati
NYUAD Hackathon 2018 - Healthcare


## How to run 

### Only the first time

- configure the env
- install the env

```bash
python3.6 -m venv env # could also be python3.5 if python3.6 is not available
```


Now ask the team for configs and paste them at the end of file at `env/bin/activate` and save.

Ask the team for a testing db (should be called `db.sqlite3`) and paste it in this root.

```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

### Ever after

```bash
source env/bin/activate # no need to do this if you just run the installation for the first time
```

```bash
python manage.py runserver 0.0.0.0:8000
```

Web should be available at [http://localhost:8000/](http://localhost:8000/)
