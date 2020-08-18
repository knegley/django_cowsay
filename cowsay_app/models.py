from django.db import models

# Create your models here.


class Results(models.Model):
    input_text = models.CharField(max_length=30)

    def __str__(self):
        return self.input_text
