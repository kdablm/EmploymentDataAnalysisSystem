from django.urls import path
from api import views
urlpatterns = [
    path('hello/', views.hello, name='hello-api'),
    path('test/',views.hello_post)
]
