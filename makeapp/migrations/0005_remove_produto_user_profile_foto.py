# Generated by Django 5.1.5 on 2025-01-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeapp', '0004_alter_produto_preco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='user'),
        ),
    ]
