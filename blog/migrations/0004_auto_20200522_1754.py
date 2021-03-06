# Generated by Django 2.1.4 on 2020-05-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200522_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('summary', models.CharField(max_length=300)),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images')),
                ('github_link', models.TextField(max_length=512)),
                ('implementation', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'project_info',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='post',
            table='post_info',
        ),
    ]
