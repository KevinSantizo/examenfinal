from django.db import models

# Create your models here.


class Land(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.country + ' - ' + self.region


class Plot(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    length = models.CharField(max_length=100)

    def __str__(self):
        return 'Parcela: ' + self.name + ' - ' + ' Finca: ' + self.land.name


class Tree(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    diameter = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return 'Plot: ' + self.plot.name + ' - ' + self.diameter + ' - ' + self.height
