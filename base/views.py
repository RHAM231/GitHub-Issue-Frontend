from django.shortcuts import render, redirect
from .forms import IssueSearchForm, IssueCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'project_count': 1,
        'folder_count': 12,
        'file_count': 37,
        'issue_count': 63,
    }
    return render(request, 'base/home.html', context)


def confirm_sync(request):
    return render(request, 'base/confirm_sync.html')


def sync_success(request):
    return render(request, 'base/sync_success.html')


def search_results(request):
    context = {
        'title': 'Search Results'
    }
    return render(request, 'base/search_results.html', context)


def project_list(request):
    context = {
        'issue_count': 123,
        'title': 'Projects',
    }
    return render(request, 'base/project_list.html', context)


def project_contents(request):
    context = {
        'issue_count': 0,
        'title': 'Projects',
    }
    return render(request, 'base/project_contents.html', context)


def folder_contents(request):
    context = {
        'title': 'Projects',
    }
    return render(request, 'base/folder_contents.html', context)


def file_contents(request):
    context = {
        'title': 'Projects',
        'issues_present': 3,
    }
    return render(request, 'base/file_contents.html', context)


def issue_create(request):
    form = IssueCreateForm()
    context = {
        'form': form,
        'title': 'Issues',
    }
    return render(request, 'base/issue_create.html', context)


def issue_read(request):
    context = {
        'condition': True,
        'title': 'Issues',
    }
    return render(request, 'base/issue_read.html', context)


def issue_update(request):
    form = IssueCreateForm()
    context = {
        'form': form,
        'title': 'Issues',
    }
    return render(request, 'base/issue_update.html', context)


def issue_delete(request):
    context = {
        'title': 'Issues',
    }
    return render(request, 'base/issue_delete.html', context)


def issue_list(request):
    form = IssueSearchForm()
    context = {
        'form': form,
        'title': 'Issues',
    }
    return render(request, 'base/issue_list.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'base/about.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'base/register.html', {'form': form})


def profile(request):
    return render(request, 'base/profile.html')


def login(request):
    return render(request, 'base/login.html')


def logout(request):
    return render(request, 'base/logout.html')