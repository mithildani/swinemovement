# Generated by Django 4.1 on 2022-08-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swinemovement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(db_index=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='movement',
            name='reason',
            field=models.CharField(choices=[('FINISH TO FINISH', 'FINISH TO FINISH'), ('SOW TO FINISH', 'SOW TO FINISH'), ('SOW TO NURSERY', 'SOW TO NURSERY'), ('WTF TO FINISH', 'WTF TO FINISH'), ('SOW TO WTF', 'SOW TO WTF'), ('OTHER', 'OTHER')], default='OTHER', max_length=30),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(db_index=True, max_length=30, unique=True),
        ),
    ]
