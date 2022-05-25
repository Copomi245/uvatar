from bottle import get, post, run, request
import sys
import json
import random


def uvatarAleatorio():
    aleatorio = {"nombre" : "Aleatorio"}

    with open('./uvatar_recortes.json') as file:
        data = json.load(file)
        
    #i = random.randint(0, data["caras"].__len__()-1)
    #aleatorio["cara"] = data["caras"][i]
    i = random.randint(0, data["left_ears"].__len__()-1)
    aleatorio["orejaI"] = data["left_ears"][i]
    i = random.randint(0, data["right_ears"].__len__()-1)
    aleatorio["orejaD"] = data["right_ears"][i]
    i = random.randint(0, data["eyes"].__len__()-1)
    aleatorio["ojos"] = data["eyes"][i]
    i = random.randint(0, data["mouths"].__len__()-1)
    aleatorio["boca"] = data["mouths"][i]
    i = random.randint(0, data["noses"].__len__()-1)
    aleatorio["nariz"] = data["noses"][i]

    with open('Aleatorio.json', 'w') as file:
        json.dump(aleatorio, file, indent=4)
    return aleatorio

@get('/Aleatorio')
def Aleatorio():
    aleatorio = uvatarAleatorio()
    return aleatorio

@post('/Aleatorio')
def post1():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

run(host='localhost', port=8080, debug=True)