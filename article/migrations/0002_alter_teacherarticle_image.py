# Generated by Django 4.0.5 on 2022-07-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherarticle',
            name='image',
            field=models.ImageField(default='default.png', upload_to='teacher/', verbose_name='profile img'),
        ),
    ]
