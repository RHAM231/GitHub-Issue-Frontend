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
    