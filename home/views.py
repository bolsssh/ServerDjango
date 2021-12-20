import sys

from django.http import JsonResponse
import json
from .utils import *
from subprocess import Popen
from signal import SIGINT

# start the process

def Ping(request):
    return JsonResponse({}, status=200)


def PostInputData(request):
    DataBase.Input = json.loads(request.body)
    return JsonResponse({}, status=200)


def GetAnswer(request):
    input = DataBase.Input
    return JsonResponse(convertObject(input), status=200)


def Stop(request):
    sys.exit(0)


class DataBase:
    Input = {}
