# Generated by Django 3.2.4 on 2021-07-07 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('standard', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=50)),
                ('evaluation', models.CharField(choices=[('fail', 'Fail'), ('pass', 'Pass')], default='pass', max_length=5)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('active', models.BooleanField()),
                ('joined_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GuardianDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('relation', models.CharField(choices=[('mother', 'Mother'), ('father', 'Father'), ('other', 'Other')], default='father', max_length=20)),
                ('address', models.TextField()),
                ('mobile_no', models.PositiveIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guardians', to='app1.studentdetail')),
            ],
        ),
    ]
