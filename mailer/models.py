from django.db import models
from domains.models import DomainModel

class MailerModel(models.Model):
    domain = models.ForeignKey(DomainModel, on_delete=models.CASCADE, related_name='user_mailers')
    recipient = models.EmailField("Kimga")
    subject = models.CharField("Mavzu", max_length=255)
    body = models.TextField("Mazmuni")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Mailer'
        verbose_name_plural = 'Mailers'
