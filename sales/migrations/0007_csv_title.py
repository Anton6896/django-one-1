# Generated by Django 3.2.3 on 2021-05-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20210525_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
