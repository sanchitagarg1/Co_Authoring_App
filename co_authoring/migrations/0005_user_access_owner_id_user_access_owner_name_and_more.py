# Generated by Django 4.2 on 2023-05-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_authoring', '0004_alter_file_record_abstract_alter_file_record_authors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_access',
            name='owner_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user_access',
            name='owner_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user_access',
            name='paper_title',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user_access',
            name='suggestion',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='user_access',
            name='user_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]