from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.listar_rod , name=""),
    path('tipo_rod/', include([
        path('agregar', views.agregar_tipo , name="agregar-tipo"),
        path('editar/<str:tipo_id>', views.editar_Tipo, name="editar-tipo"),
    ])),

    path('rod/', include([
        path('agregar', views.agregar_rod , name="agregar-rod"),
        path('editar/<int:rod_id>', views.editar_rod, name="editar-rod"),
        path('eliminar/<int:rod_id>', views.eliminar_rod, name="eliminar-rod"),
    ])),

    path('equiva/', include([
        path('agregar/<int:fk_rod>', views.agregar_equiv , name="agregar-equiva"),
        path('editar/<int:fk_rod>', views.editar_equiv, name="editar-equiva"),
    ])),
]