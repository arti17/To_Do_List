# Generated by Django 2.2.5 on 2019-09-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('status', models.TextField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done')], default='new', max_length=50, verbose_name='Статус')),
                ('date', models.DateField(default=None, null=True, verbose_name='Дата')),
            ],
        ),
    ]
