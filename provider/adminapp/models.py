from django.db import models

class AdminMOdel(models.Model):
    a_email = models.EmailField()
    a_idno = models.IntegerField()
    a_password = models.CharField(max_length=20)