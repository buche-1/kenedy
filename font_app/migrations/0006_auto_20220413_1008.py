# Generated by Django 3.2.12 on 2022-04-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('font_app', '0005_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/pics')),
            ],
        ),
        migrations.DeleteModel(
            name='myself',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]