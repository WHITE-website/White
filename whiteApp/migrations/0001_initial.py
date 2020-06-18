# Generated by Django 2.2.13 on 2020-06-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(default='default')),
            ],
        ),
    ]