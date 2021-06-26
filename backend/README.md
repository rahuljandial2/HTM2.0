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
### auth(on new terminal)
#### signup
```sh
http http://127.0.0.1:8000/api/user-register/ username=<username> email=<something@email.com> password=<password123>
#response
{
    "token": "<token>"
}

```
#### login
```sh
http http://127.0.0.1:8000/api/auth-token/ username=<username> password=<password123>
#response
{
    "token": "<token>"
}

```
