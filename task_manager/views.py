from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.translation import activate
from django.shortcuts import redirect


class Index(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Users(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = ['name', 'name_2', 'name_3']
        context['users'] = users
        return context


def set_language(request):
    next = request.GET.get('next', '')
    language = request.GET.get('language', '')
    print(language)
    if language == "English":
        lang = 'en'
    else:
        lang = 'ru'
    activate(lang)
    response = redirect(next)
    return response
