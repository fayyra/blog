# Generated by Django 4.0.6 on 2022-08-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['data']},
        ),
        migrations.AddField(
            model_name='blog',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
