from django.urls import path
from.import views

urlpatterns = [
    path('main/',views.main, name="main"),
    path('main/clients/', views.clients, name='clients'),
    path('main/clients/add/', views.add, name='add'),
    path('main/clients/delete/<int:id>', views.delete, name='delete'),
    path('main/clients/edid', views.edit, name='edid'),
    path('main/clients/update/<int:id>', views.update, name='update'),
    path('main/history/', views.history, name='history'),
    path('filter/', views.filter, name='filter'),
    ]
