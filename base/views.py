from django.shortcuts import render
from .forms import IssueSearchForm, IssueCreateForm


# Create your views here.
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'base/home.html', context)


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