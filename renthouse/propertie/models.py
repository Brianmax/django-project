from django.db import models

# Create your models here.
class Casa(models.Model):
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)

    def __str__(self):
        return self.street

class Departamento(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)
    price = models.SmallIntegerField(default=0)
    rooms = models.SmallIntegerField(default=0)
    size = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.price) + " " + str(self.rooms) + " " + str(self.size)


class Recibo(models.Model):
    departamento = models.ForeignKey(Casa, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    cantidad = models.SmallIntegerField(default=0)


class Arrendatario(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)


class Contrato(models.Model):
    arrendatario = models.ForeignKey(Arrendatario, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    adress = models.CharField(max_length=150)
