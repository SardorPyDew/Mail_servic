from django.db import models

from users.models import UserModel


class DomainModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_domains')
    name = models.CharField(max_length=255)
    txt = models.CharField(max_length=255)
    dkim = models.CharField(max_length=255)
    dmarc = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'
