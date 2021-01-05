# Generated by Django 3.1.5 on 2021-01-05 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], max_length=30)),
                ('access_type', models.CharField(choices=[('Edit', 'Edit'), ('View', 'View')], max_length=30)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=32, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]