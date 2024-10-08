# Generated by Django 4.2.2 on 2024-09-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_and_time_of_last_mailing_attempt",
                    models.DateTimeField(
                        verbose_name="Дата и время последней попытки рассылки"
                    ),
                ),
                (
                    "attempt_status",
                    models.TextField(verbose_name="статус попытки(успешно/не успешно)"),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылки",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Контактный email"
                    ),
                ),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "patronymic",
                    models.CharField(max_length=50, verbose_name="Отчество"),
                ),
                ("comment", models.TextField(verbose_name="Комментарий")),
            ],
            options={
                "verbose_name": "Клиент сервиса",
                "verbose_name_plural": "Клиенты сервиса",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=20, verbose_name="Название рассылки"),
                ),
                (
                    "date_and_time_of_first_mailing",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="дата и время первой отправки рассылки",
                    ),
                ),
                (
                    "mailing_status",
                    models.CharField(
                        default="создана", max_length=20, verbose_name="Статус рассылки"
                    ),
                ),
                (
                    "mailing_start_date",
                    models.DateField(verbose_name="Дата начала рассылки"),
                ),
                (
                    "mailing_end_date",
                    models.DateField(verbose_name="Дата окончания рассылки"),
                ),
                (
                    "time_which_newsletter_sent",
                    models.PositiveIntegerField(
                        verbose_name="Час, в который нужно отправить письмо, пример- 01 или 24"
                    ),
                ),
                (
                    "minute_when_newsletter_should_sent",
                    models.PositiveIntegerField(
                        verbose_name="минута, в которую нужно отправитьсообщение, например 01 или 60"
                    ),
                ),
                (
                    "date_letter_was_sent",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Дата когда нужно отправить следующее письмо",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True, verbose_name="Активна рассылка или нет"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "permissions": [
                    ("can_disable_mailing", "can disable mailing"),
                    ("can_view_any_mailing", "can view any mailing lists"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject_of_letter",
                    models.CharField(max_length=100, verbose_name="Тема письма"),
                ),
                ("body_of_letter", models.TextField(verbose_name="Тело письма")),
            ],
            options={
                "verbose_name": "Сообщение для рассылки",
                "verbose_name_plural": "Сообщения для рассылки",
            },
        ),
        migrations.CreateModel(
            name="Periodicity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=20, verbose_name="Периодичность рассылки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Периодичность рассылки",
                "verbose_name_plural": "Периодичности рассылок",
            },
        ),
    ]
