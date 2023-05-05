from django.contrib import admin
from django.urls import path, include
from student import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
    title = "Student API",
    default_version = 'v 1.0.0',
    description = "Student API; To store and get student details",
    terms_of_service = "https://www.google.com/policies/terms/",
    contact = openapi.Contact(email="omotoso.rauf@plitsolutions.com"),
    license = openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include('student.urls')),

    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc'), name='schema-redoc'),
]
