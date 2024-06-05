from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.translation import activate


class Index(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Users(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users_1 = [{'id': 1, 'name': 'name_1', 'f_name': 'fname_1', 'date': '2022-01-01'},
                   {'id': 2, 'name': 'name_2', 'f_name': 'fname_2', 'date': '2023-01-01'},
                   {'id': 3, 'name': 'name_3', 'f_name': 'fname_3', 'date': '2024-01-01'},
                   ]

        context['users'] = users_1
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
