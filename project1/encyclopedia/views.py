from os import name
from django.shortcuts import render
from django import forms

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title:", max_length=100)
    break_line = "<br>"
    content = forms.CharField(label="Content:", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request):
    return render(request, "encyclopedia/entry.html", {
        "form": NewEntryForm()
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "title": title,
        "content": util.get_entry(title)
    })