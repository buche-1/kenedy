# Generated by Django 3.2.12 on 2022-05-18 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('font_app', '0009_rename_adress_contact_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='bvn',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='next_of_kin',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='nin',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='state',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150, verbose_name='User Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.TextField(verbose_name='Content')),
                ('created_date', models.TimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='font_app.blog')),
            ],
        ),
    ]
