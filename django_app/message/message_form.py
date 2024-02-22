from django.forms import ModelForm, DateField, Textarea, CharField
from django.views.generic import FormView, TemplateView, DetailView, ListView, DeleteView
from message.message_model import Message


class MessageForm(ModelForm):
    dt_upload_element = DateField(required=True, input_formats=['%Y-%m-%d'])
    text_element = CharField(max_length=1024, strip=True, required=True)

    class Meta:
        model = Message
        fields = ['dt_upload', 'text']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['dt_upload'] = cleaned_data['dt_upload_element']
        cleaned_data['text'] = cleaned_data['text_element']
        return cleaned_data