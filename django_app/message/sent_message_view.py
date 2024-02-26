from django.urls import reverse_lazy
from django.views.generic import TemplateView


class MessageSentView(TemplateView):
    template_name = 'message_sent_view.html'
    success_url = reverse_lazy('message_view')