from tokenize import String
from unicodedata import name
from bottle import get, post, run, request,template
import sys
import json
import random
import glob
from random import randint

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
