# Generated by Django 5.0.4 on 2024-04-19 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_comment='This field stores the time when the record was created.', help_text='This field stores the time when the record was created.')),
                ('timestamp_updated', models.DateTimeField(auto_now=True, db_comment='This field stores the time when the record was last updated.', help_text='This field stores the time when the record was last updated.')),
                ('username', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_comment='This field stores the time when the record was created.', help_text='This field stores the time when the record was created.')),
                ('timestamp_updated', models.DateTimeField(auto_now=True, db_comment='This field stores the time when the record was last updated.', help_text='This field stores the time when the record was last updated.')),
                ('name', models.CharField(max_length=255)),
                ('github_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github.githubuser')),
            ],
            options={
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_comment='This field stores the time when the record was created.', help_text='This field stores the time when the record was created.')),
                ('timestamp_updated', models.DateTimeField(auto_now=True, db_comment='This field stores the time when the record was last updated.', help_text='This field stores the time when the record was last updated.')),
                ('issue_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github.repository')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]