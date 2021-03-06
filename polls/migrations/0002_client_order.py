# Generated by Django 2.0.9 on 2019-03-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('hpd', models.DecimalField(decimal_places=1, max_digits=3)),
                ('rate', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromDate', models.DateTimeField(verbose_name='From')),
                ('toDate', models.DateTimeField(verbose_name='To')),
                ('hours', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
