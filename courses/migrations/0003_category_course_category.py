# Generated by Django 5.1 on 2024-09-23 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.category'),
            preserve_default=False,
        ),
    ]
