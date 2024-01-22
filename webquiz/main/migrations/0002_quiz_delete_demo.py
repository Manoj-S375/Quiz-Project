# Generated by Django 4.1.7 on 2023-09-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('qno', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=1)),
                ('opt1', models.CharField(max_length=35)),
                ('opt2', models.CharField(max_length=35)),
                ('opt3', models.CharField(max_length=35)),
                ('opt4', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'quiz',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='demo',
        ),
    ]