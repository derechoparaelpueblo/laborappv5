# Generated by Django 3.2.7 on 2022-03-10 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conflictoDespidoSJC', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conflictodespidosjcmodel',
            old_name='idDemandaEmpresa',
            new_name='demandaEmpresa',
        ),
        migrations.RenameField(
            model_name='conflictodespidosjcmodel',
            old_name='idDemandaPersonaNatural',
            new_name='demandaPersonaNatural',
        ),
    ]