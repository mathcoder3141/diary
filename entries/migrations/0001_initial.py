# Generated by Django 3.0.3 on 2021-04-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('scale_feeling', models.IntegerField()),
                ('goal_today', models.TextField()),
                ('negative', models.TextField()),
                ('overcome', models.TextField()),
                ('goal_tomorrow', models.TextField()),
            ],
        ),
    ]