# Generated by Django 5.1.6 on 2025-03-21 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotion',
            options={'verbose_name': 'Promoção', 'verbose_name_plural': 'Promoções'},
        ),
        migrations.AddField(
            model_name='promotion',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
