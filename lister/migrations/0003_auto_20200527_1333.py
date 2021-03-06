# Generated by Django 3.0.6 on 2020-05-27 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lister', '0002_info_hostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lister.Client'),
        ),
        migrations.AlterField(
            model_name='info',
            name='type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lister.Type'),
        ),
    ]
