from django import forms
from .widgets import SelectWithDisabled

class MasterSearchForm(forms.Form):
    master_search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder':'Issues, Projects, Folders, etc.', 'class': 'ms-form-style'}
        )
    )


FILTER_CHOICES = [
    ('title', 'Filters'),
    ('open_issues', 'Open Issues'),
    ('closed_issues', 'Closed Issues'),
    ('your_issues', 'Your Issues'),
]

OPEN_CLOSED_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]

AUTHOR_CHOICES = [
    ('title', 'Author'),
    ('project1', 'Project1'),
]

PROJECT_CHOICES = [
    ('title', 'Projects'),
    ('project1', 'Project1'),
]

FOLDER_CHOICES = [
    ('title', 'Folders'),
    ('folder1', 'Folder1'),
]

FILE_CHOICES = [
    ('title', 'Files'),
    ('file1', 'File1'),
]

SORT_CHOICES = [
    ('title', 'Sort'),
    ('newest', 'Newest'),
    ('oldest', 'Oldest'),
    ('recently_updated', 'Recently Updated'),
    ('least_recently_updated', 'Least Recently Updated'),
]


class IssueSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder':'is:issue is:open', 'class': 'issue-search'}
        ))
    filters = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'filter-field'},
            choices=FILTER_CHOICES))
    select_all = forms.BooleanField(
        required=False)
    open_closed = forms.ChoiceField(
        choices=OPEN_CLOSED_CHOICES, 
        widget=forms.RadioSelect(attrs={'class':'test'}))
    author = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'filter-field'},
            choices=AUTHOR_CHOICES))
    projects = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'filter-field'},
            choices=PROJECT_CHOICES))
    sort = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'filter-field'},
            choices=SORT_CHOICES))


class IssueCreateForm(forms.Form):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={'placeholder':'Issue ...'}
        ))
    project_associate = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'associate-field'},
            choices=PROJECT_CHOICES))
    folder_associate = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'associate-field'},
            choices=FOLDER_CHOICES))
    file_associate = forms.CharField(
        required=False, 
        widget=forms.Select(
            attrs={'class':'associate-field'},
            choices=FILE_CHOICES))
    comment = forms.CharField(
        required=False,
        label='Comment',
        widget=forms.Textarea(
            attrs={'placeholder':'Description ...'}))
