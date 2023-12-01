# Generated by Django 4.1.6 on 2023-11-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0004_users_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('deskripsi', models.CharField(max_length=200)),
                ('link_image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Karakteristik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskripsi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('course_id', models.CharField(max_length=200)),
            ],
        ),
    ]