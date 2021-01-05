from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    students = []
    return JsonResponse(students, safe=False)
