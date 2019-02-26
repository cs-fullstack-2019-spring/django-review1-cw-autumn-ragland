# Generated by Django 2.0.6 on 2019-02-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='alcoholPercentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='servingGlass',
            field=models.IntegerField(default=0),
        ),
    ]