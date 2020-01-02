# Generated by Django 3.0.2 on 2020-01-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('avenue', models.CharField(max_length=191)),
                ('chair', models.CharField(max_length=100)),
                ('secretary', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('report', models.URLField(blank=True, null=True)),
                ('remarks', models.TextField()),
            ],
        ),
    ]