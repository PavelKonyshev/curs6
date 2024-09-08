from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


# Create your models here.
class Message(models.Model):
    """Модель сообщений для рассылки"""
    subject_of_letter = models.CharField(max_length=100, verbose_name="Тема письма")
    body_of_letter = models.TextField(verbose_name='Тело письма')
    creator = models.ForeignKey(User, verbose_name='Создатель сообщения', on_delete=models.SET_NULL,
                                related_name="creator_message", null=True, blank=True)

    def __str__(self):
        return f'{self.subject_of_letter}'

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"


class Customer(models.Model):
    """Модель клиента сервиса"""
    contact_email = models.EmailField(unique=True, verbose_name='Контактный email')
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    comment = models.TextField(verbose_name='Комментарий')
    creator = models.ForeignKey(User, verbose_name='Создатель клиента', on_delete=models.SET_NULL,
                                related_name="creator_customer", null=True, blank=True)

    def __str__(self):
        return f'{self.contact_email}'

    class Meta:
        verbose_name = "Клиент сервиса"
        verbose_name_plural = "Клиенты сервиса"


class Periodicity(models.Model):
    """Модель периодичности рассылки"""
    name = models.CharField(max_length=20, verbose_name="Периодичность рассылки")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Периодичность рассылки"
        verbose_name_plural = "Периодичности рассылок"


class Mailing(models.Model):
    """Модель рассылки"""
    name = models.CharField(max_length=20, verbose_name='Название рассылки')
    date_and_time_of_first_mailing = models.DateTimeField(null=True, blank=True,
                                                          verbose_name='дата и время первой отправки рассылки')
    periodicity = models.ForeignKey(Periodicity, on_delete=models.SET_NULL, verbose_name="Периодичность рассылки",
                                    related_name="periodicity", null=True, blank=True)
    mailing_status = models.CharField(max_length=20, default='создана', verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name="Сообщение рассылки",
                                related_name="mailing_list_message", null=True, blank=True)
    customers_of_service = models.ManyToManyField(Customer, verbose_name="Пользователи сервиса",
                                                  related_name="customers_of_service")
    mailing_start_date = models.DateField(verbose_name='Дата начала рассылки')
    mailing_end_date = models.DateField(verbose_name='Дата окончания рассылки')
    time_which_newsletter_sent = models.PositiveIntegerField(verbose_name='Час, в который нужно отправить письмо, пример'
                                                                          '- 01 или 24')
    minute_when_newsletter_should_sent = models.PositiveIntegerField(verbose_name='минута, в которую нужно отправить'
                                                                                  'сообщение, например 01 или 60')
    date_letter_was_sent = models.DateField(null=True, blank=True,
                                            verbose_name='Дата когда нужно отправить следующее письмо')
    active = models.BooleanField(default=True, verbose_name='Активна рассылка или нет')
    creator = models.ForeignKey(User, verbose_name='Создатель рассылки', on_delete=models.SET_NULL,
                                related_name="creator_mailing", null=True, blank=True)

    def __str__(self):
        return f'{self.periodicity}'

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ('can_disable_mailing', 'can disable mailing'),
            ('can_view_any_mailing', 'can view any mailing lists')
        ]


class Attempt(models.Model):
    """Модель попытки рассылки"""
    date_and_time_of_last_mailing_attempt = models.DateTimeField(verbose_name='Дата и время последней попытки рассылки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Связь рассылки и информации о её '
                                                                                'статусе')
    attempt_status = models.TextField(verbose_name='статус попытки(успешно/не успешно)')

    def __str__(self):
        return f'{self.attempt_status}'

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
