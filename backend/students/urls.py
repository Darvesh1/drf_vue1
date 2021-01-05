from  django.urls import path

from rest_framework import routers
# from  .views import index

from  .views import *

router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

# urlpatterns = [
#     path('students/', index)
# ]

urlpatterns = router.urls