# Generated by Django 3.2.7 on 2022-03-10 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contratoLaboral', '0003_contratolaboralmodel_is_active'),
        ('demandaPersonaNatural', '0006_alter_demandapersonanaturalmodel_fechademandapersonanatural'),
        ('demandaEmpresa', '0005_alter_demandaempresamodel_montototaldemandapersjuri'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConflictoDespidoSJCModel',
            fields=[
                ('fechaInicioContrato', models.DateTimeField(blank=True, null=True)),
                ('tipoContrato', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('fechaDespido', models.DateTimeField(blank=True, null=True)),
                ('montoDinero_DSJC', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratoLaboral.contratolaboralmodel')),
                ('idDemandaEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demandaEmpresa.demandaempresamodel')),
                ('idDemandaPersonaNatural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demandaPersonaNatural.demandapersonanaturalmodel')),
            ],
        ),
    ]
