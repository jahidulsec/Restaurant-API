# Generated by Django 4.2.1 on 2023-06-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='imgUrl',
            field=models.CharField(db_index=True, default='', max_length=255),
        ),
    ]
