# Generated by Django 3.0.2 on 2020-02-25 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equivalente',
            name='MARCA',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='equivalente',
            name='N_ROD',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='DESCRIPCION',
            field=models.CharField(blank=True, default='N/A', max_length=1000),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_ESP_B',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_ESP_C',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_ESP_T',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_EXT_D',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_EXT_D1',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_INT_A',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='D_INT_A1',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='FK_TIPO_ROD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.ProtectedError, to='mantenedor.Tipo_Rodamiento'),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='N_PARTE_1',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='rodamiento',
            name='N_PARTE_2',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='tipo_rodamiento',
            name='TIPO',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
    ]
