# Generated by Django 4.1.5 on 2023-03-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_room_delete_course_data_delete_entries_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='profID',
            field=models.CharField(default='na', max_length=100),
            preserve_default=False,
        ),
    ]
