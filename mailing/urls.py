from django.urls import path
from django.views.decorators.cache import cache_page

from config.settings import CACHE_ENABLED
from mailing.apps import MailingConfig
from mailing.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDetailView, CustomerDeleteView, MailingListView, \
    MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, AttemptListView, \
    AttemptDetailView

app_name = MailingConfig.name
if CACHE_ENABLED:
    urlpatterns = [

        path('message/', MessageListView.as_view(), name='message_list'),
        path('create_message/', MessageCreateView.as_view(), name='message_create'),
        path('edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
        path('info_message/<int:pk>/', MessageDetailView.as_view(), name='info_message'),
        path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),


        path('customer/', CustomerListView.as_view(), name='customer_list'),
        path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
        path('edit_customer/<int:pk>/', CustomerUpdateView.as_view(), name='edit_customer'),
        path('info_customer/<int:pk>/', CustomerDetailView.as_view(), name='info_customer'),
        path('delete_customer/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),


        path('', cache_page(60)(MailingListView.as_view()), name='mailing_list'),
        path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
        path('edit_mailing/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
        path('info_mailing/<int:pk>/', MailingDetailView.as_view(), name='info_mailing'),
        path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),

        path('attempt/', AttemptListView.as_view(), name='attempt_list'),
        path('info_attempt/<int:pk>/', AttemptDetailView.as_view(), name='info_attempt'),
    ]
else:
    urlpatterns = [

        path('message/', MessageListView.as_view(), name='message_list'),
        path('create_message/', MessageCreateView.as_view(), name='message_create'),
        path('edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
        path('info_message/<int:pk>/', MessageDetailView.as_view(), name='info_message'),
        path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),


        path('customer/', CustomerListView.as_view(), name='customer_list'),
        path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
        path('edit_customer/<int:pk>/', CustomerUpdateView.as_view(), name='edit_customer'),
        path('info_customer/<int:pk>/', CustomerDetailView.as_view(), name='info_customer'),
        path('delete_customer/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),


        path('', MailingListView.as_view(), name='mailing_list'),
        path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
        path('edit_mailing/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
        path('info_mailing/<int:pk>/', MailingDetailView.as_view(), name='info_mailing'),
        path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),


        path('attempt/', AttemptListView.as_view(), name='attempt_list'),
        path('info_attempt/<int:pk>/', AttemptDetailView.as_view(), name='info_attempt'),
    ]