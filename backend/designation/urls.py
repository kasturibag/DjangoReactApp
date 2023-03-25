"""
URL mappings for the designation API.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from designation import views

router = DefaultRouter()
router.register('', views.DesignationViewSet, basename='designation')

app_name = 'designation'

urlpatterns = [
    path('', include(router.urls)),
]
