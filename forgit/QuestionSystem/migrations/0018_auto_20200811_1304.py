# Generated by Django 2.1.15 on 2020-08-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionSystem', '0017_advise_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='response_part',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='suggestion_gen',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='response',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]