from django.urls import path
from basic_app import views

# TEMPLATE TAGGING (set variable name of app_name)
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]