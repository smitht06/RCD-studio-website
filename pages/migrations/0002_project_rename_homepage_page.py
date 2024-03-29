# Generated by Django 5.0.2 on 2024-02-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
            ],
        ),
        migrations.RenameModel(
            old_name='HomePage',
            new_name='Page',
        ),
    ]
