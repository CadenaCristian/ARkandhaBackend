import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .query import listPlots, listPlotById, insertPlots, updatePlots, deletePlots, listPlotsType, listAllOwners
from ..common.functions import executyQuery, valMessage


@csrf_exempt
def list(request):
    if request.method == 'GET':
        data = executyQuery('r', listPlots)
        message = valMessage('retorna', 'data', 1 if data != 1 else 0)
        print("message: ", message)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def getPlotById(request, id):
    if request.method == 'GET':
        var = listPlotById.format(id)
        data = executyQuery('r', var)
        message = valMessage('retorna', 'data', 1 if data != 1 else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def listAllPlotsType(request):
    if request.method == 'GET':
        data = executyQuery('r', listPlotsType)
        message = valMessage('retorna', 'data', 1 if data != 1 else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)


@csrf_exempt
def listOwners(request):
    if request.method == 'GET':
        data = executyQuery('r', listAllOwners)
        message = valMessage('retorna', 'data', 1 if data != 1 else 0)
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
        newinsertPlots = insertPlots.format(body["catastral_id"], body["plost_type"],
                                            body["addres_name"], body["realtor_name"], body["owner_data"])
        data = executyQuery('i', newinsertPlots)
        message = valMessage('inserta', 'data', 1 if data != 0 else 0)
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
        newupdatePlots = updatePlots.format(body["catastral_id"], body["plost_type"],
                                            body["addres_name"], body["realtor_name"], body["owner_data"], body["id"])
        data = executyQuery('i', newupdatePlots)
        print("data: ", data)
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
        newdeletePlots = deletePlots.format(body["id"])
        data = executyQuery('i', newdeletePlots)
        print("data: ", data)
        message = valMessage('elimina', 'data', 1 if data != 0 else 0)
        peticionResponse = {
            "error": message["error"],
            "message": message["message"],
            "data": data
        }
        return JsonResponse(peticionResponse, safe=False)
