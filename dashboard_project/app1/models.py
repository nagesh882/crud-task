from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    mobile = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Details"
        verbose_name_plural = "User Data"

    def __str__(self):
        return self.first_name