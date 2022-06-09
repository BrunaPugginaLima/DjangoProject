from django.urls import path
from . import views

app_name = 'ipam'
urlpatterns = [
    path('', views.index, name = 'index'),
    #VLANS
    path('vlan/', views.VlanList.as_view(), name='vlan-list'), 
    path('vlan/<int:pk>/', views.VlanDetail.as_view(), name='vlan-detail'),
    path('vlan/new/', views.VlanCreate.as_view(), name='vlan-create'),
    path('vlan/<int:pk>/update/', views.VlanUpdate.as_view(), name='vlan-update'),
    path('vlan/<int:pk>/delete/', views.VlanDelete.as_view(), name='vlan-delete'),
    #SUBNETS
    path('subnet/', views.SubnetList.as_view(), name='subnet-list'), #ok, só falta ver certinho o que tem que aparecer
    path('subnet/<int:pk>/', views.SubnetDetail.as_view(), name='subnet-detail'), #ok, só falta ver certinho o que tem que aparecer
    path('subnet/new/', views.SubnetCreate.as_view(), name='subnet-create'), 
    path('subnet/<int:pk>/update/', views.SubnetUpdate.as_view(), name='subnet-update'),
    path('subnet/<int:pk>/delete/', views.SubnetDelete.as_view(), name='subnet-delete'), 
]