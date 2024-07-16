# Generated by Django 5.0 on 2024-03-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0005_verify_pwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('fileurl', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'audio_files',
            },
        ),
        migrations.CreateModel(
            name='kksongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('fileurl', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'kksongs',
            },
        ),
        migrations.CreateModel(
            name='rockfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('fileurl', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'rockfile',
            },
        ),
        migrations.CreateModel(
            name='usersongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('fileurl', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'usersongs',
            },
        ),
    ]