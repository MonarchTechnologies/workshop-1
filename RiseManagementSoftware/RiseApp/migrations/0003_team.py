# Generated by Django 3.1.1 on 2020-11-20 04:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('RiseApp', '0002_auto_20201112_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('Team_Name', models.CharField(max_length=45)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RiseApp.project')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
