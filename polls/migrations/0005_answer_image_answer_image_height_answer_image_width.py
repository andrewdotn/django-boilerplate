# Generated by Django 4.0.4 on 2022-05-22 21:14

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_demo_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="image",
            field=models.ImageField(
                blank=True,
                height_field=models.IntegerField(blank=True, null=True),
                null=True,
                upload_to=polls.models.answer_image_upload_to,
                width_field=models.IntegerField(blank=True, null=True),
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="image_height",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="answer",
            name="image_width",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]