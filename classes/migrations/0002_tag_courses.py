# Generated by Django 4.0.4 on 2022-10-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='courses',
            field=models.ManyToManyField(related_name='tags', to='classes.course'),
        ),
    ]