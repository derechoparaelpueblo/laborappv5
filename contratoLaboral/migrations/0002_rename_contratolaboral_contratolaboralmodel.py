# Generated by Django 3.2.7 on 2021-10-10 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_empresamodel_ubicacion'),
        ('persona', '0002_alter_personmodel_lugarresidenciapersona'),
        ('persona_natural', '0003_rename_persona_personanaturalmodel_person'),
        ('contratoLaboral', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContratoLaboral',
            new_name='ContratoLaboralModel',
        ),
    ]
