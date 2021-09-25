from fastapi import FastAPI
from typing import List
from config import routes

app = FastAPI()

names       = []
paths       = []
payloads    = []
tags        = []

for i in routes:
    path        = routes[i]['path']
    payload     = routes[i]['payload']
    tag         = routes[i]['tag']
    names.append(i)
    paths.append(path)
    payloads.append(payload)
    tags.append(tag)

def generator(name:List, path:List, payload:List, tag:List):
    counter = 0
    for i  in name:
        i = f'''@app.get("{path[counter]}", tags={tag[counter]}) 
        \nasync def {i}(): 
        \n    return {payload[counter]}\n'''
        code=compile(i, 'generator', 'exec')
        exec(code)
        counter += 1

generator(name=names, path=paths, payload=payloads, tag=tags)

