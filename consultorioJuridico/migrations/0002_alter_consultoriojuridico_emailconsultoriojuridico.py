# Generated by Django 3.2.7 on 2021-09-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorioJuridico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultoriojuridico',
            name='emailconsultoriojuridico',
            field=models.EmailField(blank=True, db_column='emailConsultorioJuridico', max_length=100, null=True),
        ),
    ]
