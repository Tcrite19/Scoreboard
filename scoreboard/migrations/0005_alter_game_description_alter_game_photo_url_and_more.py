# Generated by Django 5.1 on 2024-08-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_alter_game_description_alter_game_photo_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=10485),
        ),
        migrations.AlterField(
            model_name='game',
            name='photo_url',
            field=models.CharField(max_length=10485, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=10485),
        ),
    ]
