# Generated by Django 2.0.7 on 2020-05-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='img'),
            preserve_default=False,
        ),
    ]