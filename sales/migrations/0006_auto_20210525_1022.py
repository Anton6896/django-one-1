# Generated by Django 3.2.3 on 2021-05-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20210525_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='file_csv',
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(null=True, upload_to='csv_files'),
        ),
    ]
