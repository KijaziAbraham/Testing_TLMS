# Generated by Django 4.2.5 on 2023-09-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='level_of_education',
            field=models.CharField(choices=[('PRIMARY SCHOOL', 'PRIMARY SCHOOL'), ('SECONDARY SCHOOL', 'SECONDARY SCHOOL')], default=' ', max_length=50),
        ),
    ]