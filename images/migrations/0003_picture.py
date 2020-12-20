# Generated by Django 3.1.4 on 2020-12-18 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.location')),
            ],
        ),
    ]
