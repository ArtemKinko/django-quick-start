from django.db.models import Model, DateTimeField, TextField



class Message(Model):
    dt_upload = DateTimeField(null=True, blank=True)
    text = TextField(blank=True)