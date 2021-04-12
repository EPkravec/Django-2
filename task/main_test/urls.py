from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='general'),
    path('deal', views.deal, name='deal'),
    path('deal_load_csv', views.deal_load_csv, name='deal_load_csv'),

]