# Generated by Django 2.2.4 on 2020-01-31 12:40

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner_chat', '0006_remove_player_chat_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chat_start_time',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
