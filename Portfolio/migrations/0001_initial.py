# Generated by Django 3.2.5 on 2022-02-11 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('email', models.EmailField(default='', max_length=254)),
                ('inquiry', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]