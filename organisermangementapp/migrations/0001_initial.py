# Generated by Django 4.1.7 on 2023-02-19 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('back_ground_img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('writer_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('cause_sub_heading', models.CharField(blank=True, max_length=1000, null=True)),
                ('cause_sub_heading_img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('cause_sub_heading_img_title', models.TextField(blank=True, max_length=1000, null=True)),
                ('article', models.TextField(blank=True, max_length=1000, null=True)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisermangementapp.activity')),
            ],
        ),
    ]
