import os.path

from django.db import models
from django.db.models import CASCADE
from django.http import Http404
from django.utils.crypto import get_random_string

DEFAULT_MAX_LENGTH = 255


class Question(models.Model):
    subject = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def answer_count(self):
        return self.answer_set.count()

    def __str__(self):
        return self.subject


def answer_image_upload_to(instance, filename):
    filename_without_ext, ext = os.path.splitext(filename)
    basename = os.path.basename(filename_without_ext)

    allowed_extensions = [".jpg", ".gif", ".png"]

    if ext.lower() not in allowed_extensions:
        print(f"got {ext!r}")
        raise Http404(
            f"Invalid filename extension on {filename!r}: must be in {allowed_extensions}"
        )

    path = get_random_string(7)
    if instance.id is not None:
        path = f"{path}_{instance.id:04}"
    path = f"{path[0]}/{path[1]}/{path}_{basename}"

    return f"answer_images/{path}{ext}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    subject = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image_width = models.IntegerField(null=True, blank=True)
    image_height = models.IntegerField(null=True, blank=True)
    image = models.ImageField(
        null=True,
        blank=True,
        width_field="image_width",
        height_field="image_height",
        upload_to=answer_image_upload_to,
    )

    def vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.subject


class Vote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
