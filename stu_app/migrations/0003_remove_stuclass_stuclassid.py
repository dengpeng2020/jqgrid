# Generated by Django 2.0.6 on 2020-04-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0002_stuclass_stuclassid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuclass',
            name='stuclassid',
        ),
    ]