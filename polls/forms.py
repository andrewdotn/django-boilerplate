from django import forms

from polls.models import Answer


class VoteForm(forms.Form):
    answer_select = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, question, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["answer_select"].queryset = question.answer_set.all()
