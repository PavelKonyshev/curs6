# Generated by Django 4.2.2 on 2024-09-08 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="creator_message",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель сообщения",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="creator_mailing",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель рассылки",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="customers_of_service",
            field=models.ManyToManyField(
                related_name="customers_of_service",
                to="mailing.customer",
                verbose_name="Пользователи сервиса",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="mailing_list_message",
                to="mailing.message",
                verbose_name="Сообщение рассылки",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="periodicity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="periodicity",
                to="mailing.periodicity",
                verbose_name="Периодичность рассылки",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="creator_customer",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель клиента",
            ),
        ),
        migrations.AddField(
            model_name="attempt",
            name="mailing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing.mailing",
                verbose_name="Связь рассылки и информации о её статусе",
            ),
        ),
    ]
