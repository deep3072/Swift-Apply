# Generated by Django 5.0.1 on 2024-01-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resume_user_alter_resume_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]
