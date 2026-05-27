import base64
import json

from django.db.models import Max
from django.test import Client
from django.urls import reverse

from polls.models import Question, Answer, Vote


def test_voting(db):
    q = Question.objects.create(subject="Pick a letter")

    answers = [Answer.objects.create(question=q, subject=c) for c in "ABC"]

    client = Client()
    client.post(
        reverse("polls:vote", args=[q.id]), data={"answer_select": answers[1].id}
    )

    assert answers[1].vote_count() == 1


def test_vote_ignored_if_question_and_answer_id_dont_match(db):
    q1 = Question.objects.create(subject="a")
    a1 = Answer.objects.create(question=q1, subject="a1")

    q2 = Question.objects.create(subject="b")
    b1 = Answer.objects.create(question=q2, subject="b1")

    client = Client()
    response = client.post(
        reverse("polls:vote", args=[q1.id]), data={"answer_select": b1.id}
    )
    assert response.status_code == 302
    assert a1.vote_count() == 0
    assert b1.vote_count() == 0


def test_voting_gives_404_when_question_id_invalid(db):
    invalid_id = Question.objects.aggregate(max=Max("id"))["max"] + 1

    client = Client()
    response = client.post(
        reverse("polls:vote", args=[invalid_id]), data={"answer_select": 12}
    )
    assert response.status_code == 404


def test_votes_json_base64_response(db):
    q = Question.objects.create(subject="q")
    for i, x in enumerate("abc"):
        answer = Answer.objects.create(question=q, subject=x)
        for j in range(i + 1):
            Vote.objects.create(answer=answer)

    assert [["a", 1], ["b", 2], ["c", 3]] == json.loads(
        base64.b64decode(q.vote_set_json_base64().encode("US-ASCII")).decode("UTF-8")
    )
