import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .query import listOwners, listOwnerType, getTypeOwner, listById, insertOwners, updateOwners, deleteOwners
from ..common.functions import executyQuery, valMessage


@csrf_exempt
def list(request):
    if request.method == 'GET':
        data = executyQuery('r', listOwners)
        message = valMessage('retorna', 'data', 1 if data != None else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def listTypeOwner(request):
    if request.method == 'GET':
        data = executyQuery('r', listOwnerType)
        message = valMessage('retorna', 'data', 1 if data != None else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def getById(request, id):
    if request.method == 'GET':
        queryId = listById.format(str(id))
        data = executyQuery('r', queryId)
        message = valMessage('retorna', 'data', 1 if data != None else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def insert(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        query = listById.format(str(body["identification"]))
        userExist = executyQuery('r', query)
        print("userExit: ", userExist)
        if len(userExist) == 0:
            newinsertPlots = insertOwners.format(
                body["type_owner"], body["identification"], body["name_owner"])
            data = executyQuery('i', newinsertPlots)
            message = valMessage('inserta', 'data', 1 if data != 0 else 0)
        else:
            data = []
            message = {"error": True, "message": "El usuario ya existe"}
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def update(request):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print("lom", len(body))
        if len(body) > 4:
            type = body["type_owner"]
            print("existe")
        else:
            retu = executyQuery(
                'r', getTypeOwner.format(body["id"]))
            type = retu[0]["type_owner"]
            print("no existe")
        newupdatePlots = updateOwners.format(
            type, body["identification"], body["name_owner"], body["id"])
        print("newupdatePlots: ", newupdatePlots)
        data = executyQuery('i', newupdatePlots)
        message = valMessage('actualiza', 'data', 1 if data != 0 else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        newdeletePlots = deleteOwners.format(body["id"])
        print("newdeletePlots: ", newdeletePlots)
        data = executyQuery('i', newdeletePlots)
        message = valMessage('elimina', 'data', 1 if data != 0 else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)
