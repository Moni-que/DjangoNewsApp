# Generated by Django 4.0.4 on 2022-05-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_tags_alter_editor_options_editor_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='image', upload_to='articles/'),
        ),
    ]
