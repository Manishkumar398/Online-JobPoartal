# Generated by Django 4.1.7 on 2023-04-04 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
    ]