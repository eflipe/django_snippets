# Generated by Django 2.2.4 on 2021-02-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20210225_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]