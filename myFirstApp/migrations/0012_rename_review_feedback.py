# Generated by Django 4.1.6 on 2023-12-01 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0011_remove_courses_link_continue_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Feedback',
        ),
    ]
