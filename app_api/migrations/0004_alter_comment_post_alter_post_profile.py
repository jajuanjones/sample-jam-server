# Generated by Django 4.0.5 on 2022-06-16 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_api.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app_api.profile'),
        ),
    ]