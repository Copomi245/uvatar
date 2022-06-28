from tokenize import String
from unicodedata import name
from bottle import get, post, run, request,template
import sys
import json
import random
import glob
from random import randint
"""este es el q funcion"""

def uvatarAleatorio():
    aleatorio = {"nombre" : "Aleatorio"}

    with open('./uvatar_recortes.json') as file:
        data = json.load(file)
        
    #i = random.randint(0, data["caras"].__len__()-1)
    #aleatorio["cara"] = data["caras"][i]
    i = randint(0, data["left_ears"].__len__()-1)
    aleatorio["orejaI"] = data["left_ears"][i]
    i = randint(0, data["right_ears"].__len__()-1)
    aleatorio["orejaD"] = data["right_ears"][i]
    i = randint(0, data["eyes"].__len__()-1)
    aleatorio["ojos"] = data["eyes"][i]
    i = randint(0, data["mouths"].__len__()-1)
    aleatorio["boca"] = data["mouths"][i]
    i = randint(0, data["noses"].__len__()-1)
    aleatorio["nariz"] = data["noses"][i]

    with open('Aleatorio.json', 'w') as file:
        json.dump(aleatorio, file, indent=4)
    return aleatorio

@get('/Aleatorio')
def Aleatorio():
    aleatorio = uvatarAleatorio()
    return aleatorio





@get('/Nombres')
def Nombres():
    nombres = {"Nombres" : []}

    
    with open('./pedrerol.json') as file:
        data = json.load(file)
        nombres["Nombres"].append(data["nombre"])
    with open('./juanma.json') as file:
        data = json.load(file)
        nombres["Nombres"].append(data["nombre"])
    with open('./dario.json') as file:
        data = json.load(file)
        nombres["Nombres"].append(data["nombre"])
    return nombres

#Yo
@get('/dario')
def dario():
    with open('./uvatar_recortes.json') as fp:
        
        data = json.load(fp)
        dario["ojos"]=data['eyes']['dario']
    return dario

@post('/dario')
def muestraDario():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/ojos')
def mostrarOjos():
    ojos = {"Ojos" : []}
    files = glob.glob("./recortes/ojos/*.json")
    for file in files:
        with open(file) as f:
            data = json.load(f)
            ojos["Ojos"].append(data["url"])
    
    return ojos 
   
@post('/ojos')
def postOjos():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body


@get('/bocas')
def mostrarBocas():
    bocas = {"Bocas" : []}
    files = glob.glob("./recortes/bocas/*.json")
    for file in files:
        with open(file) as f:
            data = json.load(f)
            bocas["Bocas"].append(data["url"])
    
    return bocas 
   
@post('/bocas')
def postBocas():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/narices')
def mostrarNarices():
    narices = {"Narices" : []}
    files = glob.glob("./recortes/narices/*.json")
    for file in files:
        with open(file) as f:
            data = json.load(f)
            narices["Narices"].append(data["url"])
    
    return narices 
   
@post('/narices')
def postNarices():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body


@get('/orejasI')
def mostrarOrejasI():
    orejas = {"Orejas" : []}
    files = glob.glob("./recortes/orejas/orejasI/*.json")
    for file in files:
        with open(file) as f:
            data = json.load(f)
            orejas["Orejas"].append(data["urlI"])

    
    return orejas 
   
@post('/orejasI')
def postOrejasI():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/orejasD')
def mostrarOrejasD():
    orejas = {"Orejas" : []}
    files = glob.glob("./recortes/orejas/orejasD/*.json")
    for file in files:
        with open(file) as f:
            data = json.load(f)
            orejas["Orejas"].append(data["urlD"])

    
    return orejas 
   
@post('/orejasD')
def postOrejasD():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/accesorios')
def mostrarAccesorios():
    accesorios = {"Accesorios" : []}
    files = glob.glob("./recortes/accesorios/*.json")
    for file in files:
        with open(file) as f:
            data = json.load(f)
            accesorios["Accesorios"].append(data["url"])

    
    return accesorios 
   
@post('/accesorios')
def postAccesorios():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

@get('/accesorios2')
def devolverAccesorio():

    accesorios = {"Accesorios" : []}
    files = glob.glob("./recortes/accesorios/*.json")
    print(files)
    for file in files:
        with open(file) as f:
            accesorio = json.load(f)
            accesorios["Accesorios"].append(accesorio)
    return accesorios

@post('/accesorios2')
def posteaDevuelveAccesorio():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body


print("chorizo")

################################################

run(host='localhost', port=8080, debug=True)