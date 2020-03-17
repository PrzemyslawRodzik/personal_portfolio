# Generated by Django 3.0.4 on 2020-03-17 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200317_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
