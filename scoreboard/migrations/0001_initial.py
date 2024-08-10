# Generated by Django 5.1 on 2024-08-10 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10485)),
                ('description', models.CharField(max_length=10485)),
                ('photo_url', models.CharField(max_length=10485, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='librarycatalogue', to='scoreboard.game')),
                ('library', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='librarycatalogue', to='scoreboard.library')),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='library', to='scoreboard.user'),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='scoreboard.user')),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Catalogue', to='scoreboard.game')),
                ('library', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='library', to='scoreboard.library')),
                ('wishlist', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='scoreboard.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='WishlistCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishlistcatalogue', to='scoreboard.game')),
                ('wishlist', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishlistcatalogue', to='scoreboard.wishlist')),
            ],
        ),
    ]
