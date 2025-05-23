from django.urls import path

from .vw import views, CreateFromUser, ViewPDFPersonalizacion, ViewPersonalizacion

obj = 'personalizacion'
app_label = 'personalizacion_producto'

urlpatterns = views.create_urls(app_label) + [
    path(
        'enviar-personalizacion/', CreateFromUser.as_view(),
        name="enviar_personalizacion"),
    path(
        'ver-personalizacion/<pk>/', ViewPersonalizacion.as_view(),
        name="ver_personalizacion"),
    path(
        'pdf-personalizacion/<pk>/', ViewPDFPersonalizacion,
        name="pdf_personalizacion"),
]
