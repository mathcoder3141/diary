from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EntryQuestions
from .models import Entry


def index(request):
    return render(request, 'index.html')


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
        form = EntryQuestions(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary')
    else:
        form = EntryQuestions()
    return render(request, "entry.html", {'form': form})


@login_required(login_url='/login')
def diary(request):
    latest_entry = Entry.objects.filter(user=request.user).order_by("-entry_date")[0]
    return render(request, 'diary.html', {'latest_entry': latest_entry})


@login_required(login_url='/login')
def settings(request):
    return render(request, "settings.html")


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return render(request, 'registration/logged_out.html')
