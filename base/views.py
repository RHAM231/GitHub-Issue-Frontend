from django.shortcuts import render
from .forms import IssueSearchForm, IssueCreateForm


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def search_results(request):
    return render(request, 'base/search_results.html')


def project_list(request):
    context = {
        'issue_count': 123
    }
    return render(request, 'base/project_list.html', context)


def project_contents(request):
    context = {
        'issue_count': 0
    }
    return render(request, 'base/project_contents.html', context)


def folder_contents(request):
    return render(request, 'base/folder_contents.html')


def file_contents(request):
    return render(request, 'base/file_contents.html')


def issue_create(request):
    form = IssueCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'base/issue_create.html', context)


def issue_read(request):
    context = {
        'condition': True,
    }
    return render(request, 'base/issue_read.html', context)


def issue_update(request):
    form = IssueCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'base/issue_update.html', context)


def issue_delete(request):
    return render(request, 'base/issue_delete.html')


def issue_list(request):
    form = IssueSearchForm()
    context = {
        'form': form,
    }
    return render(request, 'base/issue_list.html', context)