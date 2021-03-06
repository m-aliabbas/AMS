# Generated by Django 2.1.15 on 2020-08-11 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QuestionSystem', '0015_auto_20200810_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=django.utils.timezone.now, max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useranswer',
            name='advise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='QuestionSystem.Advise'),
        ),
    ]
