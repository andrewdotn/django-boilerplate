from django.urls import path

from . import views
from .apps import PollsConfig

app_name = PollsConfig.name

urlpatterns = [
    # URLs go here
    path("", views.QuestionListView.as_view(), name="question_list"),
    path("q/<int:pk>", views.QuestionDetailView.as_view(), name="question_detail"),
    path("q/<int:pk>/vote", views.vote, name="vote"),
    path("q/<int:pk>/votes", views.QuestionVotesView.as_view(), name="votes"),
]
