# Generated by Django 4.2.1 on 2023-06-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthesis', '0003_synthesischemical_proceduresubtype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='synthesischemical',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
