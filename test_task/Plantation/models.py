from django.db import models

class Country(models.Model):
    name = models.CharField("Country_name", max_length=150,unique=True)
    description = models.TextField("Description")

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class Plant(models.Model):
    name = models.CharField("Plant_name", max_length=150, unique=True)
    PLANT_TYPES = (
        (1,'Однолетнее'),
        (2, 'Многолетнее'),
        (3, 'Кустовое'),
        (4, 'Древовидное'),
    )
    plant_type =models.IntegerField("Plant_type",choices=PLANT_TYPES)
    description = models.TextField("Description")
    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"


class Plantation(models.Model):
    name = models.CharField("Plantation_name", max_length=150, unique=True)
    description = models.TextField("Description")
    country = models.ForeignKey(
        Country, verbose_name="Country",on_delete=models.SET_NULL, null=True
    )
    plants =  models.ManyToManyField(
        Plant,verbose_name="Plants"
    )
    class Meta:
        verbose_name = "Plantation"
        verbose_name_plural = "Plantations"


