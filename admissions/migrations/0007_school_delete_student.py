# Generated by Django 4.2.3 on 2023-08-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0006_remove_student_age_alter_student_classname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('founded_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
