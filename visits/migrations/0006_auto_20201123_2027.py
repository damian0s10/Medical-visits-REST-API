# Generated by Django 3.1.1 on 2020-11-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0005_auto_20201121_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='doctor',
            name='about_me',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email',)},
        ),
    ]
