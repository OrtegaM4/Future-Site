# Generated by Django 2.0.2 on 2018-04-27 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
