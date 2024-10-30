# Generated by Django 5.1.2 on 2024-10-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petrock',
            name='classification',
            field=models.CharField(choices=[('IGNEOUS', 'Igneous'), ('SEDIMENTARY', 'Sedimentary'), ('METAMORPHIC', 'Metamorphic')], default='IGNEOUS', max_length=15),
        ),
    ]
