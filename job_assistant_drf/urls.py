"""Module docstring?"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from userapp.views import CustomUserModelViewSet
from resumeapp.views import ResumeModelViewSet
from vacancyapp.views import VacancyModelViewSet

router = DefaultRouter()
router.register('users', viewset=CustomUserModelViewSet, basename='users')
router.register('resume', viewset=ResumeModelViewSet, basename='resume')
router.register('vacancies', viewset=VacancyModelViewSet, basename='vacancies')

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    # auth
    path('api-auth-token/', views.obtain_auth_token),

    # swagger / redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
