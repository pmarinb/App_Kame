from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.listar_rod , name="buscador"),
    path('tipo_rod/', include([
        path('buscar', views.listar_tipo, name="buscar-tipo"),
        path('agregar', views.agregar_tipo , name="agregar-tipo"),
        path('editar/<str:tipo_id>', views.editar_Tipo, name="editar-tipo"),
        path('eliminar/<str:tipo_id>', views.eliminar_tipo, name="eliminar-tipo"),
    ])),

    path('rod/', include([
        path('agregar', views.agregar_rod , name="agregar-rod"),
        path('editar/<int:rod_id>', views.editar_rod, name="editar-rod"),
        path('eliminar/<int:rod_id>', views.eliminar_rod, name="eliminar-rod"),
    ])),

    path('equiva/', include([
        path('buscar', views.listar_equiv, name="buscar-equiv"),
        path('agregar/<int:fk_rod>', views.agregar_equiv , name="agregar-equiva"),
        path('editar/<int:equiv_id>', views.editar_equiv, name="editar-equiva"),
        path('eliminar/<int:equiv_id>', views.eliminar_equiv, name="eliminar-equiva"),
    ])),
]