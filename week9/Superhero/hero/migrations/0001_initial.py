# Generated by Django 5.1.1 on 2024-10-23 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(default='Me', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identity', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('strength', models.CharField(default='', max_length=100)),
                ('weakness', models.CharField(default='', max_length=100)),
                ('image', models.CharField(default='', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superheroes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]