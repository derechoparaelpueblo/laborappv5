# Generated by Django 3.2.7 on 2021-10-07 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0002_alter_personmodel_lugarresidenciapersona'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NItEmpresa', models.CharField(blank=True, max_length=255, null=True)),
                ('nombreEmpresaRS', models.CharField(blank=True, max_length=255, null=True)),
                ('direccionEmpresa', models.CharField(blank=True, max_length=255, null=True)),
                ('telefonoEmpresa', models.CharField(blank=True, max_length=255, null=True)),
                ('emailEmpresa', models.EmailField(blank=True, max_length=254, null=True)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.personmodel')),
            ],
        ),
    ]
