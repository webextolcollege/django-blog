# Generated by Django 4.2.2 on 2025-02-13 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_alter_blog_title_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='auther',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
