# fake-api

# Instrucciones

Modificar o agregar nuevas rutas en el archivo `config.py` siguiendo la misma estructura

Ejemplo:

```py
routes= {
    'userdata':{
        'path':'/user',
        'tag': ['userdata','user'],
        'payload':{
            'id':1,
            'username':'jhondoe',
            'email':'jhondoe@gmail.com'
            }
        }
       ,
 ```

`Nota:` No repetir el path ya q solo se veria el ultimo del mismo nombre

# Instalar

```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn main:app --reload --port 8001
```

[Documantacion interativa](http://localhost:8001/docs)
