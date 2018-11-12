# Generated by Django 2.1.3 on 2018-11-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_author', models.CharField(max_length=10)),
                ('book_update', models.DateTimeField(auto_now_add=True)),
                ('book_description', models.CharField(max_length=255)),
                ('book_download_count', models.IntegerField()),
            ],
        ),
    ]
