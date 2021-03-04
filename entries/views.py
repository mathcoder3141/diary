from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EntryQuestions
from .models import Entry


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("diary")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


@login_required(login_url='/login')
def entry(request):
    if request.method == 'POST':
        filled_form = EntryQuestions(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('diary')
    form = EntryQuestions()
    return render(request, "entry.html", {'form': form})


@login_required(login_url='/login')
def diary(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'diary.html', {'entries': entries})


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return render(request, 'registration/logged_out.html')