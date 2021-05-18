from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

