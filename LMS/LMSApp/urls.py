from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='index'),
        path('c/',views.c),
        path('java/',views.java),
        path('network/',views.network),
        path('ds/',views.ds),
        path('cloud/',views.cloud),
        path('os/',views.os),
        path('python/',views.python),
        path('ethical/',views.ethical),

]
