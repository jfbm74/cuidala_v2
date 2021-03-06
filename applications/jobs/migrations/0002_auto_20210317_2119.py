# Generated by Django 3.1.7 on 2021-03-17 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='care_category',
            field=models.ManyToManyField(to='users.Skill'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='location_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='service_category',
            field=models.ManyToManyField(to='users.Service'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicants',
            name='caregiver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicants',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs'),
        ),
    ]
