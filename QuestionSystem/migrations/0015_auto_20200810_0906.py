# Generated by Django 2.1.15 on 2020-08-10 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionSystem', '0014_auto_20200808_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='user_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionSystem.Answer'),
        ),
    ]
