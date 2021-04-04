from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea
from .models import Entry


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EntryQuestions(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('entry_date',
                  'scale_feeling',
                  'goal_today',
                  'negative',
                  'overcome',
                  'goal_tomorrow')
        labels = {
            'entry_date': "Entry Date",
            'scale_feeling': "On a scale from one to five, how do you feel today?",
            "goal_today": "What did you learn or achieve today",
            "negative": "What didn\'t go well today?",
            "overcome": "What did you overcome today?",
            "goal_tomorrow": "What do you plan on learning or achieving tomorrow?"
        }
        widgets = {
            'goal_today' : Textarea(attrs={'cols': 4, 'rows': 2}),
            'negative' : Textarea(attrs={'cols': 4, 'rows': 2}),
            'overcome': Textarea(attrs={'cols': 4, 'rows': 2}),
            'goal_tomorrow' : Textarea(attrs={'cols': 4, 'rows': 2})
        }
