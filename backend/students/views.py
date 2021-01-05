from django.http import JsonResponse
from django.shortcuts import render

from .models import Student

def index(request):
    # students = Student.objects.all()
    students = []

    for student in Student.objects.all():
        students.append({
            'name': student.name,
            'course': student.course,
            'rating': student.rating,
        })

    return JsonResponse(students, safe=False)
