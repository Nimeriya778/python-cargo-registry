from django.db import models


class Crates(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date updated")


