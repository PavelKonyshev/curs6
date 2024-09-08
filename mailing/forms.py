from django.forms import ModelForm, BooleanField

from mailing.models import Message, Customer, Mailing


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class MessageForm(StyleFormMixin, ModelForm):
    """Класс форма для сообщений для рассылки"""
    class Meta:
        model = Message
        exclude = ('creator',)


class CustomerForm(StyleFormMixin, ModelForm):
    """Класс форма для клиентов сервиса"""
    class Meta:
        model = Customer
        exclude = ('creator',)


class MailingForm(StyleFormMixin, ModelForm):
    """Класс форма для рассылок"""
    class Meta:
        model = Mailing
        exclude = ('date_and_time_of_first_mailing', 'mailing_status', 'date_letter_was_sent', 'creator')

    def __init__(self, *args, **kwargs):
        """Переопределяю метод для того, чтобы в поля клиенты и сообщения выводились только те, у которых с рассылкой
        совпадают создатели"""
        super().__init__(*args, **kwargs)
        self.fields['customers_of_service'].queryset = Customer.objects.filter(creator=self.instance.creator)
        self.fields['message'].queryset = Message.objects.filter(creator=self.instance.creator)


class MailingManagerForm(StyleFormMixin, ModelForm):
    """Класс форма для редактирования рассылки менеджером"""
    class Meta:
        model = Mailing
        fields = ('active',)