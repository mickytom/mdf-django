# Generated by Django 4.1.7 on 2023-02-25 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisermangementapp', '0004_remove_blogposter_video_blogposter_image1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogposter',
            old_name='image1',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='blogposter',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='blogposter',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='blogposter',
            name='image4',
        ),
    ]
