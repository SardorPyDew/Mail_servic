# Generated by Django 5.1.3 on 2024-11-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(max_length=254, verbose_name='Kimga')),
                ('subject', models.CharField(max_length=255, verbose_name='Mavzu')),
                ('body', models.TextField(verbose_name='Mazmuni')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mailer',
                'verbose_name_plural': 'Mailers',
            },
        ),
    ]