from django.urls import include
from django.urls import path

urlpatterns = [
    path('tipo-de-parte/', include('catalogo.tipoparte.urls')),
    path('tipo-de-color/', include('catalogo.tipocolor.urls')),
    path('tipo-de-material/', include('catalogo.tipomaterial.urls')),
    ]