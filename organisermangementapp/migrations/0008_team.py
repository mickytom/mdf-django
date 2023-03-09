# Generated by Django 4.1.7 on 2023-03-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisermangementapp', '0007_blogposter_youtube_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('position', models.CharField(blank=True, max_length=1000, null=True)),
                ('arabic', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]