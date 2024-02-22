from django.urls import reverse_lazy
from django.views.generic import TemplateView


class MessageSentView(TemplateView):
    template_name = 'message_sent_view.html'
    success_url = reverse_lazy('message_view')

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     print(instance)
    #     print("Пришло сообщение: ", instance.text, ". Дата отправки:", instance.dt_upload)
    #     return super().form_valid(form)
