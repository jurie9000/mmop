# Generated by Django 4.1.5 on 2023-01-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0002_entity_instancedentity_actor"),
    ]

    operations = [
        migrations.AddField(
            model_name="actor", name="avatar_id", field=models.IntegerField(default=0),
        ),
    ]
