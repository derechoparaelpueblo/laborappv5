# Generated by Django 3.2.7 on 2022-03-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demandaEmpresa', '0005_alter_demandaempresamodel_montototaldemandapersjuri'),
        ('demandaPersonaNatural', '0006_alter_demandapersonanaturalmodel_fechademandapersonanatural'),
        ('contratoLaboral', '0003_contratolaboralmodel_is_active'),
        ('conflictoPagoSalario', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConflictoPagoSalario',
            new_name='ConflictoPagoSalarioModel',
        ),
    ]
