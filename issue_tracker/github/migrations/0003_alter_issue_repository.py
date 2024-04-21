# Generated by Django 5.0.4 on 2024-04-20 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_issue_created_at_issue_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='github.repository'),
        ),
    ]