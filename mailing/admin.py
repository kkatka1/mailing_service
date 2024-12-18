from django.contrib import admin

from mailing.models import Client, Message, Mailing, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fullname",
        "email",
        "comment",
    )
    list_filter = (
        "fullname",
        "email",
    )
    search_fields = (
        "fullname",
        "email",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "topic",
        "body",
    )
    list_filter = ("id",)
    search_fields = ("topic",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date_of_first_dispatch",
        "periodicity",
        "status",
        "created_at",
        "update_at",
        "message_id",
        "is_published",
        Mailing.get_clients,
    )
    list_filter = ("message_id", "status")
    search_fields = ("periodicity",)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "attempt_date",
        "status",
        "server_response",
        "mailing_id",
    )
    list_filter = ("status",)
    search_fields = (
        "attempt_date",
        "server_response",
    )
