# Generated by Django 3.0.7 on 2020-08-08 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionSystem', '0008_remove_nextanswer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextanswer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='QuestionSystem.Question'),
        ),
    ]
