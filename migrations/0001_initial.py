# Generated by Django 3.1.6 on 2021-02-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlan_id', models.IntegerField(default=0)),
                ('vlan_name', models.CharField(max_length=32)),
                ('vlan_desc', models.CharField(max_length=200)),
            ],
        ),
    ]
