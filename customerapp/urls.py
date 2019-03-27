from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "customerapp"

router = routers.DefaultRouter()
router.register('users', views.UserView, 'user')

urlpatterns =[
    path('api/', include(router.urls)),
]
