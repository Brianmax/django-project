# Generated by Django 4.1.7 on 2023-02-20 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('cantidad', models.SmallIntegerField(default=0)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propertie.casa')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.SmallIntegerField(default=0)),
                ('rooms', models.SmallIntegerField(default=0)),
                ('rooms_available', models.SmallIntegerField(default=0)),
                ('size', models.SmallIntegerField(default=0)),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propertie.casa')),
            ],
        ),
    ]
