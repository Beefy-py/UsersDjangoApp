# Generated by Django 3.1.2 on 2020-10-12 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_person_color_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-date_joined']},
        ),
    ]