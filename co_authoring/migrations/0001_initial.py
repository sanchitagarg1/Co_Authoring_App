# Generated by Django 4.1 on 2023-05-15 16:01

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
            name='file_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=100, null=True)),
                ('abstract', models.CharField(max_length=100)),
                ('introduction', models.CharField(max_length=250)),
                ('user_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_profile', models.CharField(max_length=100)),
                ('profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('access_type', models.CharField(max_length=100, null=True)),
                ('suggestion', models.CharField(max_length=100)),
                ('file_record_access_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='co_authoring.file_record')),
            ],
        ),
    ]
