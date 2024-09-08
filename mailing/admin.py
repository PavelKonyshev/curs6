from django.contrib import admin

from mailing.models import Message, Customer, Periodicity, Mailing, Attempt


# Register your models here.
@admin.register(Message)
class MessageForMailingAdmin(admin.ModelAdmin):
    """Админка для сообщений для рассылки"""
    list_display = ('id', 'subject_of_letter',)


@admin.register(Customer)
class MessageForMailingAdmin(admin.ModelAdmin):
    """Админка для клиентов сервиса"""
    list_display = ('id', 'last_name', 'contact_email',)


@admin.register(Periodicity)
class PeriodicityAdmin(admin.ModelAdmin):
    """Админка для периодичности рассылки"""
    list_display = ('id', 'name',)


@admin.register(Mailing)
class MailingForMailingAdmin(admin.ModelAdmin):
    """Админка для рассылок"""
    list_display = ('id', 'mailing_status', 'periodicity')


@admin.register(Attempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    """Админка для попыток рассылок"""
    list_display = ('mailing', 'date_and_time_of_last_mailing_attempt')
