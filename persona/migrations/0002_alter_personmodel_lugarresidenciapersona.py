# Generated by Django 3.2.7 on 2021-09-30 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='lugarresidenciapersona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.municipios'),
        ),
    ]
