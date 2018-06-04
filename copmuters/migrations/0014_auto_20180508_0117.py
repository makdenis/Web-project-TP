# Generated by Django 2.0.2 on 2018-05-07 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('copmuters', '0013_auto_20180401_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.BooleanField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='type',
            field=models.CharField(choices=[('Personal Computer', 'Personal computer'), ('Monoblock', 'Monoblock'), ('Laptop', 'Laptop')], default='Personal Computer', max_length=30),
        ),
        migrations.AddField(
            model_name='like',
            name='comp_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copmuters.Computer'),
        ),
        migrations.AddField(
            model_name='like',
            name='like_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('comp_key', 'like_author')},
        ),
    ]
