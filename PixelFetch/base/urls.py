from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('request', views.req_wall, name='Requested Wallpaper'),
    path('about',views.about,name='About Page'),
    path('detail',views.detail,name='Detail Page of Wallpaper'),
    path('download',views.download,name="Download Image"),
    path('scan/', views.scan_barcode, name='scan'),
]