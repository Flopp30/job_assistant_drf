"""Module docstring?"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from userapp.views import CustomUserModelViewSet
from resumeapp.views import ResumeModelViewSet
from vacancyapp.views import VacancyModelViewSet

router = DefaultRouter()
router.register('users', viewset=CustomUserModelViewSet, basename='users')
router.register('resume', viewset=ResumeModelViewSet, basename='resume')
router.register('vacancys', viewset=VacancyModelViewSet, basename='vacancys')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
