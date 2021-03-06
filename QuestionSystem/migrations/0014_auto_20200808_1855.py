# Generated by Django 3.0.7 on 2020-08-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionSystem', '0013_useranswer_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='suggestion',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='user_response',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
