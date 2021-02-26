from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse

from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.views import generic
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from snippets.models import Snippet


# def login(request):
#     return render(request, 'login.html', {})

def logout(request):
    return render(request, 'login.html', {})


class IndexListView(generic.ListView):
    model = Snippet
    queryset = Snippet.objects.all().order_by('-updated')
    context_object_name = 'snippets_list'
    template_name = 'index.html'


def language(request):
    return render(request, 'index.html', {})


def user_snippets(request):
    return render(request, 'snippets/user_snippets.html', {})


class SnippetDetail(generic.DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippets/snippet.html'  # Specify your own template name/location


# def snippet_add(request):
#     return render(request, 'snippets/snippet_add.html', {})
class SnippetCreation(CreateView):
    model = Snippet
    context_object_name = 'snippet'   # your own name for the list as a template variable
    fields = '__all__'
    template_name = 'snippets/snippet_add.html'  # Specify your own template name/location
    success_url = reverse_lazy('index')


# def snippet_edit(request):
#     return render(request, 'snippets/snippet_add.html', {})
class SnippetEdit(UpdateView):
    model = Snippet
    context_object_name = 'snippet'
    fields = '__all__'
    template_name = 'snippets/snippet_add.html'
    success_url = reverse_lazy('index')


# def snippet_delete(request):
#     return render(request, 'snippets/user_snippets.html', {})
class SnippetDelete(DeleteView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippets/snippet_delete.html'
    success_url = reverse_lazy('index')
