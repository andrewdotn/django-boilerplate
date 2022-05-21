from django.contrib import admin

from . import models


class AnswerInline(admin.TabularInline):
    model = models.Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("subject", "created_at", "answer_count")
    inlines = [AnswerInline]


admin.site.register(models.Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "subject", "created_at", "vote_count")
    list_display_links = ("subject",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("vote_set", "question")


admin.site.register(models.Answer, AnswerAdmin)


admin.site.register(models.Vote)
