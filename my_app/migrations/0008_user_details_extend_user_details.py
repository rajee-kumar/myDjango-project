# Generated by Django 5.0.6 on 2024-07-03 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(db_column='user_id', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Extend_user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='my_app.user_details')),
            ],
        ),
    ]
