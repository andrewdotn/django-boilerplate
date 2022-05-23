# Generated by Django 4.0.4 on 2022-05-23 01:27
from django.core.files import File
from django.db import migrations

from polls.demo_data import DEFAULT_QUESTIONS, DEMO_DATA_DIR


def up(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Answer = apps.get_model("polls", "Answer")

    for q_subject, answers in DEFAULT_QUESTIONS.items():
        q = Question.objects.get(subject=q_subject)
        for a in answers:
            image_file = DEMO_DATA_DIR / f"{a.lower()}.jpg"

            if image_file.exists():

                a_obj = Answer.objects.get(question=q, subject=a)
                with image_file.open("rb") as f:
                    a_obj.image.save(image_file.name, File(f))


def down(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Answer = apps.get_model("polls", "Answer")

    for q_subject, answers in DEFAULT_QUESTIONS.items():
        q = Question.objects.get(subject=q_subject)
        for a in answers:
            image_file = DEMO_DATA_DIR / f"{a.lower()}.jpg"

            if image_file.exists():
                a_obj = Answer.objects.get(question=q, subject=a)
                a_obj.image.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_alter_answer_image"),
    ]

    operations = [migrations.RunPython(up, down)]