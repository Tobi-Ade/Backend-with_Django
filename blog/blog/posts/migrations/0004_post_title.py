# Generated by Django 4.2.1 on 2023-08-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='title', max_length=1000),
            preserve_default=False,
        ),
    ]