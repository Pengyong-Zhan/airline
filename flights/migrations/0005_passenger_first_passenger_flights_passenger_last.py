# Generated by Django 4.1.4 on 2022-12-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='first',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='last',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
