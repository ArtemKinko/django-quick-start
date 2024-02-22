from django.urls import reverse_lazy
from django.views.generic import FormView
from message.message_form import MessageForm

from message.message_model import Message


class MessageView(FormView):
    form_class = MessageForm
    template_name = 'message_form_view.html'
    success_url = reverse_lazy('message_view')

    def form_valid(self, form):
        message: Message = form.save(commit=True)
        return super().form_valid(form)
