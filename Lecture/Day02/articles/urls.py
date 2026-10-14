'''
# 기본 코드

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [

]
'''

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth, name='auth'),
]
