from django.urls import path

from .views import api_view
app_name='api'
urlpatterns = [
    path('api',api_view,name='api_view')
]
