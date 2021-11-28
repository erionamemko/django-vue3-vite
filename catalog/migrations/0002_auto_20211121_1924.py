# Generated by Django 3.2.9 on 2021-11-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1, verbose_name='gender')),
                ('age', models.IntegerField(verbose_name='age')),
                ('country', models.CharField(max_length=20, verbose_name='country')),
                ('segments', models.CharField(max_length=100, verbose_name='segments')),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='age',
            field=models.IntegerField(verbose_name='age'),
        ),
    ]