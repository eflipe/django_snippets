from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.views import generic
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from snippets.models import Snippet, Language
from snippets.tasks import enviar_mail


class IndexListView(generic.ListView):
    model = Snippet
    queryset = Snippet.objects.all().order_by('-updated')
    context_object_name = 'snippets_list'
    template_name = 'index.html'


class LanguageListView(generic.ListView):
    model = Snippet

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.all().order_by('-updated')
        return qs.filter(language__slug=self.kwargs['slug'])

    context_object_name = 'snippets_list'
    template_name = 'index.html'


class UserSnippetsListView(generic.ListView):
    model = Snippet

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.all()
        return qs.filter(user__username=self.kwargs['username'])

    context_object_name = 'snippets_list'
    template_name = 'snippets/user_snippets.html'


class SnippetDetail(generic.DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippets/snippet.html'


class SnippetCreation(LoginRequiredMixin, CreateView):
    model = Snippet
    context_object_name = 'snippet'
    fields = '__all__'
    template_name = 'snippets/snippet_add.html'
    success_url = reverse_lazy('index')
    login_url = '/login/'

    def get_initial(self):
        initial = super(SnippetCreation, self).get_initial()
        initial.update({'user': self.request.user})
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        snippet = self.object.snippet
        enviar_mail.delay("Asunto muy importante", f"Contenido mensaje: {snippet}", f"{self.request.user.email}")

        form.save()
        return super(SnippetCreation, self).form_valid(form)


class SnippetEdit(UpdateView):
    model = Snippet
    context_object_name = 'snippet'
    fields = '__all__'
    template_name = 'snippets/snippet_add.html'
    success_url = reverse_lazy('index')


class SnippetDelete(DeleteView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippets/snippet_delete.html'
    success_url = reverse_lazy('index')
