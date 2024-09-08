from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing.forms import MessageForm, CustomerForm, MailingForm, MailingManagerForm
from mailing.models import Message, Customer, Mailing, Attempt


# Create your views here.

class MessageListView(ListView):
    """Класс-контроллер для вывода всех сообщений"""
    model = Message
    template_name = 'mailing/message_list.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллер для создания сообщений для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'mailing/message_form.html'

    def form_valid(self, form):
        """Метод для добавления к сообщениям рассылок их создателей"""
        message = form.save()
        user = self.request.user
        message.creator = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контролер для редактирования сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'mailing/message_form.html'


class MessageDetailView(DetailView):
    """Класс-контроллер для вывода информации о сообщении для рассылки"""
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления сообщения для рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class CustomerListView(ListView):
    """Класс-контроллер для вывода всех клиентов сервиса"""
    model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллер для создания клиентов сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing:customer_list')

    def form_valid(self, form):
        """Метод для добавления к клиенту сервиса его создателя"""
        customer = form.save()
        user = self.request.user
        customer.creator = user
        customer.save()
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контролер для редактирования клиентов сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing:customer_list')


class CustomerDetailView(DetailView):
    """Класс-контроллер для вывода информации о клиентах сервиса"""
    model = Customer


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления клиента сервиса"""
    model = Customer
    success_url = reverse_lazy('mailing:customer_list')


class MailingListView(ListView):
    """Класс-контроллер для вывода всех рассылок"""
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллер для создания рассылок"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        """Метод для добавления к рассылке её создателя"""
        mailing = form.save()
        user = self.request.user
        mailing.creator = user
        mailing.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Метод для того, при создании рассылки можно было выбрать только те сообщения и клиентов, у которых совпадают
        создатели"""
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Mailing(creator=self.request.user)
        print(kwargs['instance'])
        return kwargs


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контролер для редактирования рассылок"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_class(self):
        """В зависимости от роли пользователя будет выводиться определенная форма"""
        user = self.request.user
        if user.has_perm('mailing.can_disable_mailing'):
            return MailingManagerForm
        return MailingForm



class MailingDetailView(DetailView):
    """Класс-контроллер для вывода информации о рассылке"""
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class AttemptListView(ListView):
    """Класс-контроллер для вывода всех попыток рассылки"""
    model = Attempt


class AttemptDetailView(DetailView):
    """Класс-контроллер для вывода информации по попытке рассылки"""
    model = Attempt
