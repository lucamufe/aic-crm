from django.db import models

class CostoProyectos(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60)
    producto = models.CharField(max_length=60)
    medida = models.CharField(max_length=60)
    cantidad = models.DecimalField(max_digits=7, decimal_places=1)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    gastos = models.DecimalField(max_digits=8, decimal_places=2)
    usuario = models.CharField(max_length=60)

    def __str__(self):
        return(f"{self.ubicacion} {self.producto}")
    
    @property
    def tot_bruto(self):
        return "{0:.2f}".format(self.cantidad * self.precio)

    @property
    def tot_neto(self):
        return "{0:.2f}".format((self.cantidad * self.precio) - self.gastos)

