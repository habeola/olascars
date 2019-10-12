# Generated by Django 2.2 on 2019-10-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20191010_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='maker',
        ),
        migrations.AddField(
            model_name='feature',
            name='body_style',
            field=models.CharField(default='Hello', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='cylinders',
            field=models.CharField(blank=True, default='Hello', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='doors',
            field=models.CharField(default='Hello', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='drivetrain',
            field=models.CharField(default='Hello', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='engine',
            field=models.CharField(default='Hello', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='fuel',
            field=models.CharField(default='Hello', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='make',
            field=models.CharField(default='Hello', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='model',
            field=models.CharField(default='Hello', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='transmission',
            field=models.CharField(default='Hello', max_length=100),
        ),
        migrations.AlterField(
            model_name='feature',
            name='price',
            field=models.IntegerField(default='Hello', null=True),
        ),
    ]
