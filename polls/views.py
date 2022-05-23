from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from .models import Question, Vote
from .forms import VoteForm


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question


@require_POST
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)

    form = VoteForm(request.POST, question=question)
    print("form is", form)
    if form.is_valid():
        answer = form.cleaned_data["answer_select"]
        Vote.objects.create(answer=answer)
        return redirect(reverse("polls:votes", args=[pk]))

    return redirect(reverse("polls:question_detail", args=[pk]))


class QuestionVotesView(DetailView):
    model = Question

    template_name = "polls/question_votes.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("answer_set__vote_set")
