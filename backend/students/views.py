# from django.http import JsonResponse
# from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# def index(request):
#     # students = Student.objects.all()
#     students = []
#
#     for student in Student.objects.all():
#         students.append({
#             'name': student.name,
#             'course': student.course,
#             'rating': student.rating,
#         })

    # return JsonResponse(students, safe=False)
