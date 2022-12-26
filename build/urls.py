from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('layanan',views.layanan),
    path('pendaftaran',views.pendaftaran),
    path('artikel',views.artikel),
    path('periksahamil',views.periksahamil),
    path('suntiktt',views.suntiktt),
    path('tandamelahirkan',views.tandamelahirkan),
    path('bahayabayi',views.bahayabayi),
    path('kontrollahiran',views.kontrollahiran),
    path('kb',views.kb),
    path('imunisasi',views.imunisasi),
    path('gizi',views.gizi),
    path('promil',views.promil)
]