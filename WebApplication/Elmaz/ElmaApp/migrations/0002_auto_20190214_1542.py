# Generated by Django 2.1.2 on 2019-02-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElmaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(max_length=20, null=True),
        ),
    ]