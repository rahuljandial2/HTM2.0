# APP's API


### Initialization
```sh
virtualenv venv --python=python3.8
source venv/bin/activate

pip install -r ../requirements.txt

python manage.py makemigrations
python manage.py migrate

```
### Run
```sh
python manage.py runserver
```
### Signup(on new terminal)
```sh
http http://127.0.0.1:8000/api/user-register/ username=<username> email=<something@email.com> password=<password123>
```

