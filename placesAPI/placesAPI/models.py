from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=2, default='NA')

    def __str__(self):
        return self.name + "(" + self.code + ")"


class State(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=2, default='NA')
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name + ", " + self.country.code
    #country = models.CharField(max_length=200)


class Location(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name + ", " + self.state.code
