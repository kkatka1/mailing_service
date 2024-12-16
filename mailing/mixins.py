from django.http import HttpResponseForbidden

class OwnerAssignmentMixin:
    """
    Миксин для автоматического добавления владельца объекта.
    """
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            obj = form.save(commit=False)
            obj.owner = self.request.user
            obj.save()
            return super().form_valid(form)
        else:
            return HttpResponseForbidden("Вы должны быть авторизованы.")
