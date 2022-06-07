# Generated by Django 4.0.4 on 2022-05-02 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0001_initial'),
        ('aplicatie2', '0003_remove_companies_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aplicatie1.location'),
            preserve_default=False,
        ),
    ]