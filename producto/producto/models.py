import os.path

from django.db import models

from catalogo.models import CategoriaProducto
from configs.settings import BASE_DIR
from configs.settings import MEDIA_ROOT


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.FileField(
        upload_to='producto/',
        help_text="Archivo *.sgv con los elementos en 'id' "
                  "correspondientes a la imagen del producto a personalizar")
    categorias = models.ManyToManyField(
        CategoriaProducto, "productos", blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    @property
    def svg_content(self) -> str:
        imagen = str(self.imagen)
        if imagen and imagen[-4:].lower() == ".svg":
            file = os.path.join(BASE_DIR, MEDIA_ROOT, imagen)
            if os.path.isfile(file):
                with open(file, "r") as f:
                    return f.read()
        return ""
