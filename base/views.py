from django.shortcuts import render


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
    return render(request, 'base/project_contents.html')


def folder_contents(request):
    return render(request, 'base/folder_contents')


def file_contents(request):
    return render(request, 'base/file_contents.html')


def issue_create(request):
    return render(request, 'base/issue_create.html')


def issue_read(request):
    return render(request, 'base/issue_read.html')


def issue_update(request):
    return render(request, 'base/issue_update.html')


def issue_delete(request):
    return render(request, 'base/issue_delete.html')


def issue_list(request):
    return render(request, 'base/issue_list.html')