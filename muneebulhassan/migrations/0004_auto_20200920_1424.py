# Generated by Django 3.1.1 on 2020-09-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muneebulhassan', '0003_auto_20200919_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='p_framework',
            field=models.CharField(default='123123', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='p_description',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_name',
            field=models.CharField(max_length=30),
        ),
    ]