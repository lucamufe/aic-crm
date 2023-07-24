from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('ver-datos', views.ver_datos, name='ver-datos'),
    path('detalle-datos/<int:pk>', views.detalle_datos, name='detalle-datos'),
    path('borrar-datos/<int:pk>', views.borrar_datos, name='borrar-datos'),
    path('insertar-datos', views.insertar_datos, name='insertar-datos'),
]