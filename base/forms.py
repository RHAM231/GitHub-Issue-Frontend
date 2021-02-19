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
    ('open_issues', 'Open Issues'),
    ('closed_issues', 'Closed Issues'),
    ('your_issues', 'Your Issues'),
]

SORT_CHOICES = [
    ('newest', 'Newest'),
    ('oldest', 'Oldest'),
    ('recently_updated', 'Recently Updated'),
    ('least_recently_updated', 'Least Recently Updated'),
]

OPEN_CLOSED_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]


class IssueSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder':'is:issue is:open', 'class': 'issue-search'}
        ))
    filters = forms.CharField(
        required=False, 
        widget=forms.SelectWithDisabled(
            attrs={'class':'filter-field'},
            choices=FILTER_CHOICES))
    select_all = forms.BooleanField(
        required=False)
    open_closed = forms.ChoiceField(
        choices=OPEN_CLOSED_CHOICES, 
        widget=forms.RadioSelect(attrs={'class':'test'}))
    author = forms.CharField(
        required=False, 
        widget=forms.Select(choices=FILTER_CHOICES))
    projects = forms.CharField(
        required=False, 
        widget=forms.Select(choices=FILTER_CHOICES))
    sort = forms.CharField(
        required=False, 
        widget=forms.Select(choices=SORT_CHOICES))
    