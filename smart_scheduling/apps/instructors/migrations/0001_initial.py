# Generated by Django 3.1.1 on 2020-09-19 08:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('hour', models.IntegerField(choices=[(1, '1 Jam '), (2, '2 Jam'), (3, '3 Jam')])),
                ('days', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Senin'), (2, 'Selasa'), (3, 'Rabu'), (4, 'Kamis'), (5, 'Jumat'), (6, 'Sabtu')], max_length=11)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
