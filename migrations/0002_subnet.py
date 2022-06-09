# Generated by Django 3.1.6 on 2021-02-27 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subnet_name', models.CharField(max_length=32)),
                ('cidr', models.IntegerField(default=0)),
                ('address_prefix', models.IntegerField(default=0)),
                ('vlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipam.vlan')),
            ],
            options={
                'ordering': ['cidr'],
            },
        ),
    ]