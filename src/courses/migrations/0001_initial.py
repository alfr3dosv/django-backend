# Generated by Django 2.1 on 2018-11-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('category', models.CharField(blank=True, max_length=60, null=True)),
                ('cover_image', models.URLField()),
                ('creator_image', models.URLField()),
                ('url', models.URLField()),
                ('quick_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
