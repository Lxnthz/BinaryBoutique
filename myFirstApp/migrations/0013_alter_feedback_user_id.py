# Generated by Django 4.1.6 on 2023-12-01 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0012_rename_review_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFirstApp.users'),
        ),
    ]
