# Generated by Django 4.0.3 on 2022-06-01 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]