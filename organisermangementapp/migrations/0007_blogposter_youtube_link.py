# Generated by Django 4.1.7 on 2023-03-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisermangementapp', '0006_rename_images_blogposter_images1_blogposter_images2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposter',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]