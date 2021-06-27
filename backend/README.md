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
### CRUD EXAMPLES
`Authorization:  Token <token>` added in `headers`
`name, \[etc\]` added in `data`

#### Create Task
```sh
http http://127.0.0.1:8000/api/task/ 'Authorization: Token <token>' name=<name> [Other Params, check api/models.py] 
#response example
    {
        "completed_at": [null],
        "duration": [null],
        "ends_at": [null],
        "id":<id>,
        "is_completed": false,
        "name": <name>,
        "parent_task": [null],
        "remarks": [null],
        "starts_at": [null],
        "user": <user>
    }

```

#### List All Tasks
```sh
http http://127.0.0.1:8000/api/task/ 'Authorization: Token <token>' 
#response

    [
        {
            Task OBJ SEE above
        }
    ]


```

#### List Task
```sh
http http://127.0.0.1:8000/api/task/<id> 'Authorization: Token <token>' 
#response
    {
        Task OBJ SEE above
    }

```

#### Update Task
```sh
http PUT http://127.0.0.1:8000/api/task/<id> 'Authorization: Token <token>' {TASK}
#response
    {
        UPSATED Task OBJ SEE above
    }

```

#### DELETE Task
```sh
http DELETEhttp://127.0.0.1:8000/api/task/<id> 'Authorization: Token <token>' 
#response
    CODE:204

```
