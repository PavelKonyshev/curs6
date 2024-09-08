import random

from django.views.generic import ListView

from blog.models import Blog
from mailing.models import Mailing, Customer


# Create your views here.
class BlogListView(ListView):
    """Класс контроллер для вывода главной страницы"""
    model = Blog

    def get_context_data(self, **kwargs):
        """С помощью этого метода я хочу получить: количество рассылок всего, количество активных рассылок, количество
        уникальных клиентов для рассылок, три случайные статьи из блога"""
        context_data = super().get_context_data(**kwargs)

        # Считаю количество рассылок всего и количество активных рассылок
        number_mailing = Mailing.objects.all()
        number_of_active_mailing = 0
        for score in number_mailing:
            if score.active:
                number_of_active_mailing += 1
        context_data['number_mailing'] = len(number_mailing)
        context_data['number_of_active_mailing'] = number_of_active_mailing

        # Считаю количество уникальных клиентов для рассылок
        number_customer = Customer.objects.all()
        context_data['number_customer'] = len(number_customer)

        # Получаю случайные статьи из блога
        records = Blog.objects.all()
        first_record, second_record, third_record = random.sample(range(1, len(records)+1), 3)
        context_data['first_record'] = first_record
        context_data['second_record'] = second_record
        context_data['third_record'] = third_record

        return context_data
