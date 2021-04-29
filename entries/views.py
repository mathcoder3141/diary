from django.shortcuts import render, redirect, HttpResponse
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
def diary(request):
    if Entry.objects.filter(user=request.user).exists():
        latest_entry = Entry.objects.filter(user=request.user)[0]
    else:
        latest_entry = Entry.objects.filter(user=request.user)
    return render(request, 'diary.html', {'latest_entry': latest_entry})


@login_required(login_url='/login')
def entry(request):
    entry = EntryQuestions(request.POST)
    if request.method == 'POST':
        if entry.is_valid():
            # valid entry date is YYYY-MM-DD
            entry = entry.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary')
        else:
            print(entry.errors)
    else:
        entry = EntryQuestions()
    return render(request, "entry.html", {'entry': entry})


@login_required(login_url='/login')
def delete_entry(request, pk):
    del_entry = Entry.objects.get(pk=pk)
    del_entry.delete()
    return redirect('diary')


@login_required(login_url='/login')
def settings(request):
    return render(request, "settings.html")


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return render(request, 'registration/logged_out.html')
