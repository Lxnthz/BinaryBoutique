# Generated by Django 4.1.6 on 2023-11-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0009_alter_certificate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='link_continue',
            field=models.CharField(default='', max_length=200),
        ),
    ]